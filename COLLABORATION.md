# Clisonix Collaboration Workflow

## 🎯 Ziel: Edit → Approve → Deploy
Investoren/Partner **ändern Inhalte** → **Du prüfst/merged via Git** → **Live Update**

## 1. GitHub Repo Setup (5 min)
```
1. github.com/new → Clisonix-Pitchdeck (Private)
2. Settings → Collaborators → Add: investor-email@gmail.com (Write Access)
3. Branch Protection: Require PR approval (Dein Account)
```

## 2. Partner bearbeitet online (No Git needed!)
**Partner öffnet:** `https://github.com/YOURUSER/Clisonix-Pitchdeck`  
**Klickt:** `docs/1-pager.md` → ✏️ Edit → Änderungen → **Create Pull Request**  

**Du siehst:** PR mit Changes → **Approve & Merge** → **Auto-Deploy GitHub Pages**

## 3. Workflow-Beispiel
```
Partner: "Pre-Money €4M statt €3.5M"
↓
Editiert docs/term-sheet.md online
↓
Du: Review PR → Merge (30s)
↓
Live: https://YOURUSER.github.io/Clisonix-Pitchdeck/ aktualisiert
```

## 4. Dateien für Kollaboration (Partner ändert)
| Datei | Partner ändert | Du mergst |
|-------|----------------|-----------|
| `docs/1-pager.md` | Zahlen, Team | ✅ |
| `docs/term-sheet.md` | Terms | ✅ |
| `financials/assumptions.csv` | Prognosen | ✅ |
| `pitchdeck/slides.md` | Slides | ✅ |

## 5. Live Demo Links (teilen)
```
Dashboard: https://YOURUSER.github.io/Clisonix-Pitchdeck/
Edit Pitchdeck: https://github.com/YOURUSER/Clisonix-Pitchdeck/blob/main/pitchdeck/slides.md
Financials: https://github.com/YOURUSER/Clisonix-Pitchdeck/tree/main/financials
```

## 6. GitHub Pages Auto-Deploy
```
Settings → Pages → Source: main → / (root)
→ Live nach jedem Merge (60s)
```

## 🚀 Sofort Start
1. **Repo erstellen:** github.com/new  
2. **Files uploaden:** Drag & Drop alle 16 Dateien  
3. **Collaborator adden:** investor@company.com  
4. **Pages aktivieren** → **Live unter 5min!**

**Pro:** Partner editiert **ohne Git-Kenntnisse** | **Du kontrollierst** | **Auto Live** 🚀

**Frage:** Welcher Investor soll zuerst Collaborator werden?

