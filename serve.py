#!/usr/bin/env python3
"""
CinePulse High-Performance Local Development Server
- Uses ThreadingHTTPServer to handle requests across concurrent worker threads.
- Eliminates the 30-second connection backlog / keep-alive stall of single-threaded http.server.
- Serves /favicon.ico instantly with 204 to prevent browser hang.
- Sets snappy Cache-Control headers so updates to index.html reflect immediately.
"""

import http.server
import socket
import sys

class CinePulseHTTPHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def end_headers(self):
        # Prevent browser caching of development HTML/assets
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Immediately handle favicon requests without 404 retries
        if self.path == '/favicon.ico':
            self.send_response(204)
            self.send_header('Content-Length', '0')
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, format, *args):
        # Clean timestamped output
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}\n")

def run(port=8090):
    server_address = ('', port)
    # Enable address reuse so server restarts instantly without port conflict
    http.server.ThreadingHTTPServer.allow_reuse_address = True
    httpd = http.server.ThreadingHTTPServer(server_address, CinePulseHTTPHandler)
    httpd.daemon_threads = True
    print(f"⚡ CinePulse Multi-Threaded Server live on http://localhost:{port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        httpd.server_close()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8090
    run(port)
