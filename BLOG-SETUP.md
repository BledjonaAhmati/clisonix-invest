# 🚀 Clisonix Investment Blog - Deployment Instructions

## Quick Start: GitHub Pages Setup

Dein Blog ist bereit! Folge diesen Schritten um live zu gehen.

### 1️⃣ GitHub Repository erstellen

```bash
# 1. Initialisiere Git
git init
git add .
git commit -m "Initial blog setup - Clisonix Investment Blog"

# 2. Erstelle Repository auf GitHub
# Gehe zu github.com/new
# Name: clisonix-blog (or dein preferred name)
# Description: "Clisonix Investment Blog & Resources"
# Visibility: Public (für GitHub Pages)

# 3. Push zu GitHub
git remote add origin https://github.com/username/clisonix-blog.git
git branch -M main
git push -u origin main
```

### 2️⃣ GitHub Pages aktivieren

```
1. Gehe zu: Settings → Pages
2. Source: Deploy from branch
3. Branch: main, Folder: / (root)
4. Save
```

### 3️⃣ Custom Domain (Optional)

```
1. Settings → Pages → Custom domain
2. Trage deine Domain ein: clisonix-blog.com
3. Folge DNS-Anweisungen (CNAME Record)
```

---

## 📁 Projekt-Struktur

```
clisonix-blog/
├── _config.yml              # Jekyll Configuration
├── _layouts/
│   ├── default.html        # Main layout template
│   └── post.html           # Blog post template
├── _posts/                 # Blog posts (YYYY-MM-DD-title.md)
│   ├── 2026-04-12-pitchdeck-investor-ready.md
│   ├── 2026-04-10-financial-model.md
│   └── 2026-04-08-1-pager.md
├── assets/
│   └── style.css           # Global styles
├── index.html              # Blog homepage
├── blog.html               # Blog listing page
├── docs/                   # Keep existing docs
├── financials/             # Keep existing financials
├── pitchdeck/              # Keep existing pitchdeck
├── funding/                # Keep existing funding
├── scripts/                # Keep existing scripts
├── .gitignore
├── README.md
└── COLLABORATION.md
```

---

## 📝 Neue Blog-Posts schreiben

Erstelle neue Markdown-Datei im `_posts/` Ordner:

### Format:
```
_posts/YYYY-MM-DD-title-slug.md
```

### Beispiel:
```markdown
---
title: "Mein Blog Post Titel"
date: 2026-04-15
categories: [Pitchdeck, Fundraising]
author: Ledjan Ahmati
excerpt: "Kurze Zusammenfassung des Posts..."
---

## Heading 2

Dein Inhalt hier...

### Heading 3

Mehr Inhalte...
```

### Frontmatter (YAML Header):
- `title` - Post Titel
- `date` - Publikationsdatum (YYYY-MM-DD)
- `categories` - Tags/Kategorien (Array)
- `author` - Autor (optional)
- `excerpt` - Kurze Zusammenfassung (optional)

---

## 🎨 Styling Anpassen

### Farben ändern (Global)
Bearbeite `_layouts/default.html`:

```css
:root {
    --bg: #0A1929;              /* Background */
    --accent: #00B4D8;          /* Accent Color */
    --text: #FFFFFF;            /* Text */
    --text-secondary: #E0E0E0;  /* Secondary Text */
    --card-bg: rgba(255,255,255,0.05);  /* Card Background */
    --border: rgba(0,180,216,0.3);      /* Border Color */
}
```

### Layout ändern
- `_layouts/default.html` - Main layout für alle Seiten
- `_layouts/post.html` - Template für blog posts

---

## 📊 Existing Content Integration

Dein bestehendes Content ist integriert:

| Ordner | Verwendung |
|--------|-----------|
| `docs/` | Key Documents (1-Pager, Executive Summary, etc.) |
| `financials/` | Excel-ready CSVs |
| `pitchdeck/` | Slides.md & Design Guidelines |
| `funding/` | VC List, Förderanträge |
| `scripts/` | Teaser Video Script |

Links zu diesen bleiben funktional im Blog.

---

## 🔍 Local Testing (Optional)

Falls du Jekyll lokal testen möchtest:

```bash
# 1. Installiere Ruby & Jekyll
# https://jekyllrb.com/docs/installation/

# 2. Bundle install
bundle install

# 3. Starte local server
bundle exec jekyll serve

# 4. Öffne Browser
# http://localhost:4000
```

---

## 📤 Deployment Checklist

- [ ] Repository auf GitHub erstellt
- [ ] Code gepushed (git push)
- [ ] GitHub Pages aktiviert (Settings → Pages)
- [ ] Domain konfiguriert (optional)
- [ ] Blog Posts verifyied (http://yourdomain.com/blog)
- [ ] Navigation funktioniert (Home, Blog, Resources, Contact)

---

## 📚 Blog Post Examples

Ich habe 3 Beispiel-Posts erstellt:

1. **Pitchdeck Post** (`2026-04-12-...`)
   - 10 Slides Overview
   - Canva/PowerPoint Integration
   - Design Guidelines

2. **Financial Model Post** (`2026-04-10-...`)
   - Key Metrics Table
   - Unit Economics Breakdown
   - Valuation & Financing

3. **1-Pager Post** (`2026-04-08-...`)
   - Problem/Solution
   - Traction & Metrics
   - Contact Info

Du kannst diese Posts editieren oder neue hinzufügen!

---

## 🎯 Next Steps

1. **Pushe Code zu GitHub** `git push origin main`
2. **Aktiviere GitHub Pages** (Settings → Pages)
3. **Schreibe neue Posts** (`_posts/YYYY-MM-DD-title.md`)
4. **Share mit Investoren** - dein Blog ist live! 🚀

---

## 🆘 Troubleshooting

### Blog lädt nicht richtig
- Stelle sicher, dass GitHub Pages aktiviert ist
- Warte 2-3 Minuten nach dem Push
- Prüfe Browser Cache (Ctrl+F5)

### Posts erscheinen nicht
- Prüfe Dateinamen: `YYYY-MM-DD-slug.md`
- Prüfe YAML Frontmatter Syntax
- Stelle sicher, dass Datum nicht in der Zukunft liegt

### Styling/CSS fehlt
- Prüfe, dass `assets/style.css` existiert
- Prüfe, dass `_config.yml` richtig ist
- Rebuilde mit: Settings → Pages → Custom domain (speichern)

---

## 📞 Support & Contact

**Fragen zum Blog?**
- Ledjan Ahmati: clisonix@pm.me
- Website: https://www.clisonix.com

**Jekyll Help:**
- Docs: https://jekyllrb.com/docs/
- Theme: Minima (GitHub Pages default)

---

**Happy Blogging! 🚀📝**

*Last Updated: April 12, 2026*
