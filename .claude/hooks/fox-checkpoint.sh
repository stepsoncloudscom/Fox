#!/usr/bin/env bash
# Fox — oturum sonu otomatik checkpoint (SessionEnd hook)
# CLAUDE.md "Süreklilik döngüsü" emrinin makine ayağı: çek → çalış → YEDEKLE.
# Fox unutsa bile iş kaybolmaz. Değişiklik yoksa hiçbir şey yapmaz.
set -u
REPO="/Users/ayhanerden/Fox"
cd "$REPO" || exit 0

# Değişiklik yoksa sessizce çık
if [ -z "$(git status --porcelain)" ]; then
  exit 0
fi

DEGISEN=$(git status --porcelain | wc -l | tr -d ' ')

git add -A
git commit -q -m "Otomatik checkpoint — oturum sonu $(date '+%d.%m.%Y %H:%M') (${DEGISEN} dosya)

SessionEnd hook tarafından üretildi. Fox'un elle yaptığı commit'lerin
yerine geçmez — yalnızca hiçbir oturumun kaybolmamasını garanti eder.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" || exit 0

git push -q origin main 2>/dev/null || true
exit 0
