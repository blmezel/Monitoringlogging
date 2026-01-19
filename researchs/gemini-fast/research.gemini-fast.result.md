# Research Result for gemini-fast
# İzleme ve Analiz Sonuçları (Rapor)

## Sistem Özeti
- **Tarih:** 20.01.2026
- **İzlenen Servis Sayısı:** 42
- **Kritik Hata Sayısı:** 2

## Servis Durum Tablosu
| Servis Adı | Durum | Açıklama |
| :--- | :--- | :--- |
| `nginx.service` | RUNNING | Web trafiği normal. |
| `ssh.service` | RUNNING | Güvenli erişim aktif. |
| `postgresql.service` | FAILED | Bellek yetersizliği hatası! |
| `ufw.service` | RUNNING | Firewall kuralları devrede. |

## Tespit Edilen Log Kayıtları (SecOps)
- **SSH:** Çoklu başarısız giriş denemesi tespit edildi (Brute-force şüphesi).
- **PostgreSQL:** `Out of memory` hatası nedeniyle servis durdu.
