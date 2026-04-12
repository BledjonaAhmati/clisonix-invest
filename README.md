# Clisonix Invest Blog

## Overview

This repository contains the Clisonix investor blog and fundraising material prepared for GitHub Pages. It combines blog posts, pitch assets, financial models, and supporting documents in one publishable site.

**Key Components:**

- **Homepage**: Jekyll landing page in `index.html`
- **Blog**: Jekyll posts in `_posts/` and listing page in `blog/index.html`
- **Pitchdeck**: Investor slides in `pitchdeck/slides.md`
- **Financial Model**: CSV tables in `financials/`
- **Supporting Docs**: Executive Summary, 1-Pager, Due Diligence Checklist, Term Sheet
- **Funding**: Förderantrag sketches and VC list

## Quick Start

1. Open `index.html` and review the landing page content.
2. Add or edit blog posts in `_posts/`.
3. Keep investor files in `docs/`, `financials/`, `pitchdeck/`, and `funding/`.
4. Run the publish helper in `scripts/publish-github.ps1` when ready.
5. Enable GitHub Pages in the repository settings.

## Structure

```text
Clisonix-Pitchdeck/
├── README.md                 # Project overview
├── _config.yml               # Jekyll configuration
├── _layouts/                 # Shared layouts
├── _posts/                   # Blog posts
├── assets/                   # Shared CSS
├── blog/
│   └── index.html            # Blog listing page
├── index.html                # Homepage
├── pitchdeck/
│   └── slides.md             # Investor slides
├── docs/
│   ├── executive-summary.md
│   ├── 1-pager.md
│   ├── due-diligence.md
│   └── term-sheet.md
├── financials/
│   ├── assumptions.csv
│   ├── revenue.csv
│   ├── pnl.csv
│   └── dcf.csv
├── funding/
│   ├── foerderantrag.md
│   └── vc-list.md
├── scripts/
│   ├── teaser-video.md
│   ├── publish-github.ps1    # Publish helper
│   └── enable-pages-checklist.txt
```

## Publishing

### Push to GitHub

PowerShell:

```powershell
cd "c:\Users\Admin\Invest Clisonix\Clisonix-Pitchdeck"
.\scripts\publish-github.ps1
```

The script will:

- initialize git if needed
- set the `origin` remote
- add all files
- create a commit if there are staged changes
- push to `main`

### Enable GitHub Pages

Follow `scripts/enable-pages-checklist.txt` after the first push.

### Add a New Blog Post

Create a file in `_posts/` with this format:

```markdown
---
title: "Post title"
date: 2026-04-12
categories: [Fundraising, Product]
author: Ledjan Ahmati
excerpt: "Short summary"
---

Write the article here.
```

## Notes

- `blog/index.html` is the public post listing page.
- Individual posts are generated from `_posts/`.
- Static markdown resources remain accessible directly from the site.

## Funding Ask

### €1.2M Seed Round

- Pre-Money: €3.5M
- Use: 50% R&D, 25% Marketing, 15% Ops, 10% Infra
- Traction: Live platform, 99.9% uptime, €424k ARR proj. 2026
- Exit: 5-7y Trade Sale (IRR 65%)

## Contact

**Ledjan Ahmati** - Founder & CEO  
✉️ <clisonix@pm.me>  
📞 +491713031616 
🌐 <https://www.clisonix.com>  
📍 Bochum, NRW  

**ABA GmbH** (Tech Partner)  
✉️ <contact@clisonix.com>  
📞 +49 171 3031616  

**Confidential** - For investors & funding institutions only © 2026 Clisonix
