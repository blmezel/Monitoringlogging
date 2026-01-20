# 🛡️ Advanced Pentest Monitoring & Logging Projesi

Bu proje, **İleri Sızma Testi** dersi kapsamında; Kali Linux ortamında sistem servislerinin durumunu izlemek, logları analiz etmek ve kritik servis kesintilerinde uyarı veren otomatize bir araç geliştirmek amacıyla hazırlanmıştır.

## 👤 Hazırlayan

* **İsim Soyisim:** Ezel Balım Atik
* **Üniversite:** İstinye Üniversitesi
* **Bölüm:** Bilişim Güvenliği Teknolojisi

## 🎯 Proje Amacı

Sızma testi ortamlarında sistemin (Kali Linux) stabilitesini korumak kritik öneme sahiptir. Bu projenin temel amacı; `systemd` servislerini anlık olarak denetleyen, `journalctl` üzerinden hata ve uyarı loglarını filtreleyen ve herhangi bir kesinti durumunda güvenlik uzmanını uyaran **otonom bir bash script** mimarisi oluşturmaktır.

---

## 🛠️ 1. Monitoring & Logging (Teknik Mimari)

Projenin kalbi olan `src/monitor.sh`, Unix I/O mimarisini kullanarak sistemin "kalp atışlarını" dinler ve raporlar.

### Özellikler:

* **Service Status Monitoring:** SSH, Apache2, Tor gibi kritik servislerin `active/passive` durumunu anlık denetler.
* **Log Filtering Engine:** Sistemdeki binlerce log arasından sadece `Error (p-3)` ve `Warning (p-4)` seviyesindeki kayıtları süzer.
* **Critical Alert System:** İzlenen bir servis durduğunda (fail/inactive), terminal üzerinden görsel ve yazılı "CRITICAL" uyarısı verir.
* **Auto Self-Check:** Script çalışmadan önce root yetkisi ve gerekli bağımlılıkları (dependencies) otomatik kontrol eder.

---

## 📂 2. Proje Yapısı ve Entegrasyon

Proje, endüstri standardı klasör yapısına ve Git iş akışına uygun olarak geliştirilmiştir:

* `src/`: Kaynak kodlar ve otomasyon scriptleri (monitor.sh).
* `specs/`: Proje gereksinimleri ve `project_info.json` dosyası.
* `docs/`: Ekran görüntüleri (screenshots) ve teknik dokümantasyon.
* `researchs/`: Yapılan ön araştırmalar ve analiz çıktıları.

---

## 🚀 Nasıl Çalıştırılır?

Projeyi terminal üzerinden test etmek ve çalıştırmak için aşağıdaki komutları kullanabilirsiniz:

**1. Yetkilendirme:**
Scriptin çalışabilmesi için çalıştırma izninin verilmesi gerekir.

```bash
chmod +x src/monitor.sh
2. Başlatma (Initialization): Script, sistem servislerine ve loglarına (journalctl) erişeceği için root (sudo) yetkisiyle çalıştırılır.

Bash

sudo ./src/monitor.sh
3. Doğrulama (Verification): Proje meta verilerinin doğruluğunu teyit etmek için bilgi dosyası okunur.

Bash

cat specs/project_info.json
Sistem Çıktısı
Otomasyon başarıyla tamamlandığında, terminal ekranında aşağıdaki durum raporu oluşur. Bu çıktı, servislerin ayakta olduğunu ve kritik hata bulunmadığını doğrular:

Plaintext

[INFO] Monitoring Process Started...
----------------------------------------
[OK] SSH Service is ACTIVE (Running).
[OK] Apache2 Service is ACTIVE (Running).
----------------------------------------
[LOGS] Scanning System Journal for Errors (Last Boot)...
-- No Critical Errors Found --
----------------------------------------
[STATUS] System check completed successfully at: Tue Jan 20 17:05:00 2026
