#!/usr/bin/env bash
# Fox — context dolarken durum-tazeliği uyarısı (PreCompact hook)
# 14 Ağu 2026 dersi: fox-durum.md 15 gün bayat kaldı, yeni oturum yanlış devraldı.
set -u
REPO="/Users/ayhanerden/Fox"
cd "$REPO" || exit 0

SON=$(git log -1 --format=%ct -- fox-durum.md 2>/dev/null || echo 0)
SIMDI=$(date +%s)
if [ "$SON" -gt 0 ]; then
  GUN=$(( (SIMDI - SON) / 86400 ))
else
  GUN="?"
fi
DEGISEN=$(git status --porcelain | wc -l | tr -d ' ')

echo "=== FOX SÜREKLİLİK KAPISI (context doluyor — compact öncesi) ==="
echo "fox-durum.md son commit: ${GUN} gün önce · commit'siz dosya: ${DEGISEN}"
echo "EMİR (CLAUDE.md Süreklilik döngüsü): compact'tan ÖNCE fox-durum.md'yi"
echo "bu oturumda değişen gerçekliğe göre güncelle, sonra commit + push et."
echo "Kural: fox-durum.md 40 satırı geçmez — biriken geçmiş"
echo "raporlar/oturum-gunlugu.md'ye iner. Ayhan'ın ek izni beklenmez."
exit 0
