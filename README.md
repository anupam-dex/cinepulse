# CinePulse 🍿 — Today's Cinema & Watch Radar

A cinema radar, watch schedule, and personal watched diary web application built with HTML5, Tailwind CSS, and vanilla JavaScript.

![CinePulse Preview](https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1200&auto=format&fit=crop&q=80)

---

## ✨ Key Features

- 👤 **Profile Creation & Email Sign-In**:
  - Create personalized cinema profiles with avatar customization, email ID, and cinema vibe preference.
  - Multi-profile support with local storage persistence and quick profile switching.
- ⚡ **Open Movie Database & Zero-Duplication ID Indexing**:
  - Search any film or series by title, genre, or unique IMDb ID (e.g., `tt0111161`).
  - Movies are indexed by unique identifier (`cinepulse_movie_index`).
  - When another user or search looks for an already-indexed film, the app retrieves it instantly from the database index without duplicate API queries.
  - Option to dynamically index any new movie ID on the fly.
- 🎬 **Ambient Auto-Playing Trailer Marquee**:
  - The hero marquee auto-plays the featured film's official YouTube trailer / teaser in high definition.
  - Includes a floating **"🔊 Unmute / Mute"** toggle button for sound control.
  - Fullscreen trailer modal available anytime.
- 📅 **Visual Festival Calendar**:
  - Day-by-day September 2026 cinema schedule with visual indicators for removals, language study, and watched screenings.
- 🎬 **Watched Movie Vault & Diary**:
  - Filterable catalogue of completed films and series with IMDb and Rotten Tomatoes ratings and curator impressions.
- 🎲 **Interactive Roulette Shuffle**:
  - Web Audio synthesized chime effects with randomized recommendations across the entire indexed database.

---

## 🚀 Quick Start (Local Preview)

Run the local web server on port **8090**:

```bash
cd /Users/mcdex/.gemini/antigravity/scratch/cinepulse

# Start local server on free port 8090
python3 -m http.server 8090
```

Then open your browser to:
👉 **[http://localhost:8090](http://localhost:8090)**

*(Port 8090 was chosen to avoid port conflicts with already-running local services).*

---

## 🔄 Sync with GitHub

### Step 1: Create a new repository on GitHub
1. Go to [github.com/new](https://github.com/new).
2. Name your repository (e.g., `cinepulse` or `cinema-radar`).
3. Leave **"Add a README file" unchecked** (we already created one).
4. Click **Create repository**.

### Step 2: Push your local repo to GitHub
Run these commands in your terminal (replace `<REPO_NAME>` with your repository name):

```bash
cd /Users/mcdex/.gemini/antigravity/scratch/cinepulse

# Link to your new repository (replace <REPO_NAME> with your repo name)
git remote add origin https://github.com/anupam-dex/<REPO_NAME>.git

# Push changes to main
git branch -M main
git push -u origin main
```

---

## 🌐 Deploy Live with GitHub Pages (Free)

Because this app is self-contained in `index.html`, you can host it live on the web instantly:

1. In your GitHub repository, navigate to **Settings** > **Pages** (in the left sidebar).
2. Under **Build and deployment** > **Source**, select **Deploy from a branch**.
3. Under **Branch**, select `main` and root `/ (root)`, then click **Save**.
4. In a few seconds, your site will be live at:
   ```
   https://anupam-dex.github.io/<REPO_NAME>/
   ```

---

## 🛠️ Tech Stack
- **HTML5 & Vanilla JavaScript (ES6+)**
- **Tailwind CSS CDN**
- **Web Audio API** (Sound effects synthesized client-side)
- **YouTube Iframe API** (Ambient autoplay background trailers)
- **Local Database Indexing** (`localStorage` caching by Movie ID)
