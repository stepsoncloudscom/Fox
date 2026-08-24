# Wix yükleme durumu — Özgür Protez / Levitate hattı (24 Ağu 2026)

siteId: 6e57503f-4b11-4ac2-8912-9a46e160abf8 · Stores **V3** · Draft · TRY
Medya kök klasörü: `Levitate-Temiz` = ff2147cc799549b4a489f22f2d0fd732

## Yapılan
- 13 ürün oluşturuldu (bulk create, 13/13 başarılı). Fiyat 0.00, visible, PHYSICAL,
  açıklama metinleri yerleşti. Hepsi şu an yalnız "All Products" kategorisinde.
- Görselleri bağlanan: **2/13** (Forever 6", Forever 7")

## Ürün ID ↔ medya klasörü ID eşlemesi
| Ürün | productId | medya klasörü | görsel |
|---|---|---|---|
| Cam Elyaf Protez Ayak 6inç | 381ab9fc-4fa1-49dd-820a-fbd4e0d779f8 | 989dfd9797e746a19617df96ff7bfe3b | ✅ 3 |
| Cam Elyaf Protez Ayak 7inç | 1f2a78c7-67f0-4bd7-be9b-93a45e9cec2e | 53f98740e34d42a780edfa31e0716748 | ✅ 3 |
| Cam Elyaf Protez Ayak 9inç | 95add8da-cd04-4dbe-8792-a8678a16ccb6 | 8bc4c1b50b6d45759f7d780811af9896 | ⬜ |
| Protez Ayak Alçak Profil | 09052003-d474-40c4-bb8a-d3aecbc4fe42 | 1ce6fb28cc344bfe88803b1bffb75f3c | ⬜ |
| Protez Ayak Kompakt | bda9a993-a39a-4cf0-99aa-65953fe7db62 | fce42492bb534701b5cab503e1a07771 | ⬜ |
| Koşu Bıçağı 10inç | 9e433b23-bab4-4283-b11d-7be9b6f5265b | 8eaa70b861d54e7b8ba5a5e893e598ca | ⬜ |
| Koşu Bıçağı 8inç | 2cd561b6-0ddd-4dc2-bf4e-6adfcd6b19e4 | fc52cabdfcc240338205f9c477165b65 | ⬜ |
| Koşu Bıçağı Seti 10inç | 285d9abc-27ff-44ef-a29c-67014d4f4c39 | 1815619cf971421c8c196ea17be2cdf1 | ⬜ |
| Koşu Bıçağı Seti 8inç | f8678fdb-2d3b-4e13-9ee3-170d66f7b5db | afa934e8c92c4b7289a1b6c7fddda216 | ⬜ |
| Ayak Kılıfı — Günlük | 181dfbab-5ab0-4f2d-af48-c401bd113116 | 2a06ad22cbe842c485d1146995e11e74 | ⬜ |
| Ayak Kılıfı — Tabanlı | d5fe786c-af4b-4227-b00c-447ccbf92c2d | ffcc4948c7f6445c9cd0cd622adb8ff7 | ⬜ |
| Taban — Şehir Zemini | bbf9603a-4176-41ce-a63e-77babf7e8c9a | a6664ee72d034139bb0430459b3c324f | ⬜ |
| Taban — Engebeli Zemin | 4c949766-60ce-4b9b-9ad5-a9a8034baa9c | 3ee9850f4baa45a3a41d5e4c9120e343 | ⬜ |

## Doğrulanmış yöntem (kalan 11 için aynısı)
1. `GET /site-media/v1/files?parentFolderId=<klasör>&mediaTypes=IMAGE&sort.fieldName=displayName&sort.order=ASC&paging.limit=3`
   → 3 dosyanın `url` alanını al (yanıt hacimli: renk paleti + otomatik etiket)
2. `PATCH /stores/v3/products/<productId>` body:
   `{"product":{"revision":"1","media":{"itemsInfo":{"items":[{"url":"...","altText":"..."}]}}}}`
   revision ilk güncellemede "1", sonra artar.

## Kalan işler
- 11 ürünün görsel bağlantısı
- Kategori ataması: Ayaklar 05cada7e-334e-428c-b7bb-d0b4b09c7ec8 (9 ürün) ·
  Kılıflar 72895830-9c38-4394-8a11-5915e2c58533 (2) · Tabanlıklar 12bbbaa4-677b-43ba-be4c-d7afb0557f94 (2)
  — kategori atama endpoint'i henüz doğrulanmadı, tahminle çağrılmayacak
- ÜTS/TİTCK teyidi (yayın kapısı) · 4 açık teknik teyit
