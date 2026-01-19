# QLineSec

# Linux Service Monitor Wrapper

Bu proje, Linux sistemlerinde çalışan `systemd` servislerini (SSH, Cron vb.) izleyen, loglarını analiz eden ve JSON formatında raporlayan bir otomasyon aracıdır.

## Özellikler
- **Servis Kontrolü:** Servislerin aktif/pasif durumunu anlık sorgular.
- **Log Analizi:** Hataları ayıklamak için `journalctl` kayıtlarını okur.
- **Güvenlik:** Root yetkisi kontrolü (Self-Check) yapar.
- **JSON-First:** Çıktıları makine okunabilir formatta (JSON) verir.

## Kurulum
```bash
git clone [https://github.com/blmezel/Monitoringlogging.git](https://github.com/blmezel/Monitoringlogging.git)
cd Monitoringlogging
sudo python3 src/monitor.py
