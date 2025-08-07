# Jokes Web App

A lightweight jokes website that runs **Python in the browser** via [PyScript](https://pyscript.net/).  
Jokes come from the excellent [`pyjokes`](https://pypi.org/project/pyjokes/) package. Users can pick a category, rate jokes, view their local history, and see stats — all stored in the browser (no server needed).

---

## ✨ Features

- 🐍 **Python in the browser** with PyScript (no backend required)
- 🎭 Category picker: `auto` (default), `neutral`, `chuck`, `all`
- ⭐ Rate jokes (1–5), with **persistent history** and **average rating**
- 🔊 Optional **text‑to‑speech** using the browser’s Speech Synthesis API
- 🎨 Clean UI that mixes **Bootstrap 5** components and **Tailwind utilities** (prefixed with `tw-` to avoid conflicts)

---
# [📺 Demo](https://priyanshuth.github.io/Jokes/)

## 🧱 Tech Stack

- **HTML** + **CSS**
- **Bootstrap 5** (layout/components)
- **Tailwind CSS** via CDN with `tw-` prefix (utility classes)
- **PyScript** to run **Python** (`pyjokes`) directly in the browser

---

## 📁 Project Structure

```
.
├── index.html      # Main page (loads PyScript & CDNs; links style.css and jokes.py)
├── style.css       # Custom styles for dark UI and layout
├── jokes.py        # Python logic: jokes, history, ratings, stats, voice hooks
├── .gitignore      # Common ignores for editors/builds
├── LICENSE         # MIT license
└── README.md       # You are here
```

---

## 🚀 Quick Start

1. **Clone or download** this repo.
2. Open **`index.html`** in a modern browser (Chrome/Edge/Firefox).
   > Internet is required on first load because PyScript, Bootstrap, and Tailwind are loaded from CDNs.
3. Click **“Tell me a joke”** and have fun!

> Tip: You can also host this as a static site (e.g., GitHub Pages). See **Deploy** below.

---

## 🕹️ How to Use

- **Name (optional):** enter your name for a friendly greeting.
- **Category:** pick `neutral`, `chuck`, or `all`, or leave **Auto**.
- **Buttons:**
  - **Tell me a joke** – fetches a new joke.
  - **Repeat last** – speaks/shows the previous joke again.
  - **Show history** – lists jokes from this browser (persisted).
  - **Show stats** – shows total count and average rating.
  - **Clear history** – wipes jokes & ratings from local storage.
  - **Voice On/Off** – toggles text‑to‑speech.
- **Rate (1–5):** records your rating and updates the stats.

All state is stored in `localStorage` on your device/browser.

---

## 🛠️ Customization

- **Styling:** Use Bootstrap + Tailwind utilities (`tw-*`) and tweak `style.css` for colors and layout.
- **Default category:** Change the default `<option>` in `index.html` or the category handling in `jokes.py`.
- **Voice behavior:** The helper `speak()` function in `index.html` controls rate/pitch/volume—adjust as you like.
- **Categories:** `jokes.py` uses `pyjokes` categories. Extend or change the `CATEGORIES` list if needed.

---

## ♿ Accessibility

- The main joke box uses `aria-live="polite"` so screen readers announce new jokes.
- Buttons have clear labels; rating buttons are simple numeric controls.

---

## 📜 License

MIT © 2025 Priyanshu Thakur
