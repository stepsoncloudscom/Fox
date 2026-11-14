#!/usr/bin/env bash
# Fox — durum dosyası boyut kapısı (SessionStart hook'unun ilk adımı)
# 14 Kas 2026 dersi: fox-durum.md 41 satırda kaldı ama 12,9 KB'a şişti; oturum başı çıktısı
# kesildi ve yeni oturum yalnız ilk ~2 KB'ı gördü. Tavan: 40 satır VE 6144 bayt.
# Kullanım: fox-durum-boyut.sh <dosya> — tavan aşılırsa tek satır uyarı, aşılmazsa sessiz. Her zaman 0.
set -u
DOSYA="${1:-/Users/ayhanerden/Fox/fox-durum.md}"
TAVAN=6144
[ -f "$DOSYA" ] || exit 0
BAYT=$(stat -f %z "$DOSYA" 2>/dev/null || echo 0)
if [ "$BAYT" -gt "$TAVAN" ]; then
  echo "⚠️ fox-durum.md ${BAYT} bayt — tavan ${TAVAN} bayt, oturum başında kesiliyor. Ayrıntıyı raporlar/oturum-gunlugu.md'ye indir."
fi
exit 0
