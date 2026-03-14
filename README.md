# Tubalar

A personal catalogue of everything I do, in one place.
Built with plain HTML, CSS, and JavaScript, no frameworks.

🌐 Live at: https://enchantrar.github.io/portfolio

## Project Structure

```
tubalar.com/
├── index.html        # Home page with hero & image gallery
├── about.html        # About me
├── contact.html      # Contact form (powered by Formspree)
└── static/
    ├── css/
    │   └── style.css
    └── images/
        ├── photo1.png
        ├── photo2.png
        └── photo3.png
```

## Features

- Responsive image gallery with lightbox
- Contact form connected to email via Formspree
- Custom typography using Google Fonts (Bricolage Grotesque + DM Serif Display)
- Smooth scroll animations
- Hosted on GitHub Pages

## Local Development

No build step needed. Just open `index.html` in your browser directly, or use a simple local server:

```bash
npx serve .
```

## Deployment

Pushed to `main` branch → GitHub Pages deploys automatically.
