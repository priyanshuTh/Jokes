# Jokes Web App — PyScript + Bootstrap + Tailwind

A simple jokes website that runs **Python in the browser** via [PyScript](https://pyscript.net/).  
Jokes are provided by the [`pyjokes`](https://pypi.org/project/pyjokes/) package. Users can rate jokes, view history, and see stats — all stored in browser `localStorage`.

## Features

- 🐍 Python in the browser (PyScript) — no server needed
- 🎭 Joke categories (`auto`, `neutral`, `chuck`, `all`)
- ⭐ Rate jokes (1–5), persistent history + average rating
- 🔊 Optional text-to-speech
- 🎨 UI with **Bootstrap** + **Tailwind** (Tailwind utility classes are prefixed with `tw-` to avoid conflicts)

## Tech Stack

- **HTML** + **CSS**
- **Bootstrap 5** (layout/components)
- **Tailwind CSS** via CDN with `tw-` prefix (extra utilities)
- **PyScript** (loads Python + `pyjokes` in the browser)

## Project Structure

```
.
├── index.html      # main page (loads PyScript + CDs + links to style.css and jokes.py)
├── style.css       # custom styles
└── jokes.py        # Python code executed by PyScript in the browser
```

## Customize

- **Voice on/off:** toggle the Voice button.
- **Default category:** change the default `<option>` in `index.html` or tweak selection handling in `jokes.py`.
- **Styling:** Mix Bootstrap classes with Tailwind utilities (`tw-*`) + custom CSS in `style.css`.

## License

MIT © 2025 Priyanshu Thakur
