# Clisonix Invest Blog – Deployment Guide

## Option 1: GitHub Pages (Free, 5 min)

1. Create the repository on GitHub: `clisonix-invest`.
2. Open PowerShell in the project folder.
3. Run:

```powershell
cd "c:\Users\Admin\Invest Clisonix\Clisonix-Pitchdeck"
.\scripts\publish-github.ps1
```

1. In GitHub: `Settings > Pages`.
2. Choose `Deploy from a branch`.
3. Select `main` and `/(root)`.
4. Wait for the Pages URL to become active.

Live URL pattern:

```text
https://BledjonaAhmati.github.io/clisonix-invest/
```

Main routes:

- `/`
- `/blog/`
- `/blog/2026/04/12/pitchdeck-investor-ready/`

✅ Cost: 0€ | Good default for investor sharing

## Option 2: Hetzner VPS (€3.29/Monat CX11)

**Hetzner Cloud** → New Project → Create Server:

```text
Server: CX11 (€3.29/Mo)
Location: Falkenstein (DE)
OS: Ubuntu 22.04
SSH-Key: (optional)
```

**Deploy Commands (nach SSH):**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install nginx git -y

# Clone & Serve
cd /var/www/html
sudo git clone https://github.com/YOURUSER/Clisonix-Pitchdeck.git .
sudo chown -R www-data:www-data /var/www/html
sudo systemctl restart nginx

# HTTPS (Let's Encrypt)
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d YOURDOMAIN.com
```

**Domain Setup:**  

1. Hetzner DNS → A-Record `YOURDOMAIN.com` → Server IPv4  
2. **Live:** `https://YOURDOMAIN.com`  

✅ **Kosten:** €3.29/Monat | **Custom Domain** | **Profi-Look**

## Option 3: Vercel/Netlify (Free Tier)

1. **vercel.com** → Import GitHub Repo  
2. **Auto-deploy** auf Push  
3. **Custom Domain** möglich  

**Empfehlung:** Start with GitHub Pages. Move later only if you need a custom stack or private infrastructure.

## Pre-Publish Check

Verify these files before pushing:

- `index.html`
- `blog/index.html`
- `_layouts/default.html`
- `_posts/`
- `assets/style.css`

**Kontakt:** <clisonix@pm.me>
