param(
    [string]$Remote = "git@github.com:BledjonaAhmati/clisonix-invest.git",
    [string]$Branch = "main",
    [string]$Message = "Publish Clisonix invest blog"
)

$ErrorActionPreference = "Stop"

Write-Host "Publishing repository from $PWD" -ForegroundColor Cyan

if (-not (Test-Path ".git")) {
    git init
}

$existingRemote = git remote 2>$null
if ($existingRemote -notcontains "origin") {
    git remote add origin $Remote
} else {
    git remote set-url origin $Remote
}

git add .

git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m $Message
}

git branch -M $Branch
git push -u origin $Branch

Write-Host "Publish complete." -ForegroundColor Green
