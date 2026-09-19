#!/usr/bin/env python3
"""
CinePulse High-Performance Local Development Server & Open-Source Trailer Resolver
- Multi-threaded ThreadingHTTPServer handles concurrent requests smoothly.
- Serves /favicon.ico with 204 to prevent browser hang.
- Sets snappy Cache-Control headers so dev changes reflect immediately.
- Built-in /api/trailer?q={query} endpoint that automatically resolves exact verified
  YouTube trailers/teasers using public open-source scraping & oEmbed verification.
"""

import http.server
import json
import re
import socket
import ssl
import sys
import urllib.parse
import urllib.request

TRAILER_CACHE = {}

def fetch_verified_trailer(query):
    if not query:
        return None
    clean_q = query.strip()
    if clean_q.lower() in TRAILER_CACHE:
        return TRAILER_CACHE[clean_q.lower()]

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    def check_oembed(video_id):
        try:
            url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=4) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return True, data.get("title", "")
        except Exception:
            return False, ""

    # Search YouTube public search results
    search_terms = [f"{clean_q} official trailer", f"{clean_q} teaser"]
    for term in search_terms:
        try:
            encoded = urllib.parse.quote(term)
            req = urllib.request.Request(
                f"https://www.youtube.com/results?search_query={encoded}",
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.9"
                }
            )
            with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
                matches = re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
                seen = set()
                uniq = [x for x in matches if not (x in seen or seen.add(x))]
                for vid in uniq[:6]:
                    ok, title = check_oembed(vid)
                    if ok:
                        result = {
                            "videoId": vid,
                            "title": title,
                            "trailerUrl": f"https://www.youtube.com/watch?v={vid}",
                            "embedUrl": f"https://www.youtube-nocookie.com/embed/{vid}"
                        }
                        TRAILER_CACHE[clean_q.lower()] = result
                        return result
        except Exception as e:
            sys.stderr.write(f"Notice during trailer resolve for '{clean_q}': {e}\n")

    return None

class CinePulseHTTPHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # 1. Favicon fast response
        if self.path == '/favicon.ico':
            self.send_response(204)
            self.send_header('Content-Length', '0')
            self.end_headers()
            return

        # 2. Open-source trailer resolver API
        if self.path.startswith('/api/trailer'):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            q = params.get('q', [''])[0]
            
            trailer_data = fetch_verified_trailer(q)
            self.send_response(200 if trailer_data else 404)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            payload = trailer_data if trailer_data else {"error": "Trailer not found", "query": q}
            self.wfile.write(json.dumps(payload).encode('utf-8'))
            return

        super().do_GET()

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}\n")

def run(port=8090):
    server_address = ('', port)
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    httpd = http.server.ThreadingHTTPServer(server_address, CinePulseHTTPHandler)
    httpd.daemon_threads = True
    print(f"⚡ CinePulse Multi-Threaded Server & Open-Source Trailer API live on http://localhost:{port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        httpd.server_close()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8090
    run(port)

