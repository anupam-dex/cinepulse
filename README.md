# CinePulse 🍿 — Today's Cinema & Watch Radar

A cinema planner, calendar schedule, and personal watched diary web application built with HTML5, Tailwind CSS, and vanilla JavaScript.

![CinePulse Preview](https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=1200&auto=format&fit=crop&q=80)

---

## ✨ Features

- 🌟 **Tonight's Screening Marquee**: Dynamic spotlight showcasing today's film with IMDb and Rotten Tomatoes scores, streaming platform tags, Hindi dialect notes, and official trailer player.
- 📅 **Visual Festival Calendar**: Day-by-day September 2026 cinema schedule with visual indicators for removals, language study, and watched screenings.
- 🎬 **Watched Movie Vault & Diary**: Filterable catalogue of completed films and series with ratings and curator impressions.
- 🎲 **Interactive Roulette Shuffle**: Built-in Web Audio chime synthesizer with randomized recommendation generator.
- 📱 **Fully Responsive**: Optimized for desktop, tablet, and mobile browsers with zero external build step dependencies.

---

## 🚀 Quick Start (Local Preview)

Run a local server from the project directory:

```bash
# Python 3
python3 -m http.server 8080

# Or with npx
npx serve .
```

Then visit [http://localhost:8080](http://localhost:8080) in your browser.

---

## 🔄 Sync with GitHub

### Step 1: Create a new repository on GitHub
1. Go to [github.com/new](https://github.com/new).
2. Name your repository (e.g., `cinepulse` or `cinema-radar`).
3. Leave **"Initialize this repository with a README" unchecked** (we already created one).
4. Click **Create repository**.

### Step 2: Push your local repo to GitHub
Run these commands in your terminal:

```bash
cd /Users/mcdex/.gemini/antigravity/scratch/cinepulse

# Link to your new repository (replace <REPO_NAME> with your repo name)
git remote add origin https://github.com/anupam-dex/<REPO_NAME>.git

# Push to main
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
- **HTML5 & Vanilla JavaScript** (ES6+)
- **Tailwind CSS CDN** (Styling)
- **Web Audio API** (Sound synthesized in-browser, no external audio assets needed)
- **Google Fonts** (Plus Jakarta Sans & Bebas Neue)
