# Teknik Spesifikasyonlar (Technical Specs)

## 1. Modül Tanımı: Service Monitor
Bu modül, Linux `systemd` servislerini izler ve durumlarını raporlar.

### 1.1. Fonksiyonel Gereksinimler
- **Durum Kontrolü:** Belirtilen servisin (örn: sshd, nginx) `ActiveState` bilgisini `systemctl` üzerinden çekmelidir.
- **Log Filtreleme:** `journalctl` kullanarak son 10 log kaydı içindeki "ERROR" veya "WARNING" etiketli satırları ayrıştırmalıdır.
- **Oto-Restart (Self-Healing):** Eğer servis durumu `failed` veya `inactive` ise, script servisi otomatik olarak yeniden başlatmayı denemelidir.

### 1.2. Otomasyon Yetenekleri (Auto Test Ability)
- Script çalıştırıldığında önce çalıştığı işletim sistemini (Linux) ve yetkilerini (root/sudo) kontrol etmelidir (Self-Check).
- Çıktılar insan okuması için değil, makine okuması için **JSON** formatında üretilmelidir (JSON-first yaklaşımı).

### 1.3. Kullanılacak Araçlar
- **Python:** Ana mantık ve süreç yönetimi.
- **Subprocess:** Terminal komutlarını çalıştırmak için.
- **Systemd & Journald:** Veri kaynakları.
