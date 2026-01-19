# Teknik Araştırma ve Karar Raporu (Deep Research)

## 1. Proje Kapsamı
Bu doküman, Linux `systemd` servislerini izleyen ve "Service Manager Wrapper" olarak çalışan otomasyon aracının teknik analizini içerir.
- **Odak Alanı:** SecOps & Monitoring.
- **Standart:** JSON-First Parsing ve Terminal Automation.

## 2. Teknoloji Karşılaştırması (5 Language Comparison)
Proje gereksinimlerinde belirtilen dillerin "Concurrency" (Eşzamanlılık) modelleri ve I/O performansları analiz edilmiştir:

| Dil | Yöntem / Kütüphane | Analiz Sonucu | Karar |
| :--- | :--- | :--- | :--- |
| **Bash** | Process Subst. | Basit işlemler için en hızlısı ancak karmaşık JSON işlemede zayıf. | ❌ (Yardımcı) |
| **Python** | **asyncio** / Threads | Geliştirme hızı yüksek, `subprocess` modülü ile terminal kontrolü güçlü. | ✅ **SEÇİLDİ** |
| **Go** | **Goroutines** | Çok yüksek performanslı ancak bu ölçekteki bir wrapper için maliyetli. | ❌ |
| **Node.js**| **Streams** | I/O non-blocking yapısı güçlü fakat runtime bağımlılığı (node_modules) dezavantaj. | ❌ |
| **Rust** | **Tokio** | Bellek güvenliği (Memory Safety) en iyi olan dil, öğrenme eğrisi dik. | ❌ |

**Sonuç:** Hızlı prototipleme ve güçlü kütüphane desteği (sys, json, subprocess) nedeniyle **Python 3.10+** ana geliştirme dili olarak seçilmiştir.

## 3. Unix I/O Mimarisi ve Veri Akışı
Otomasyonun terminal ile sağlıklı haberleşmesi için aşağıdaki Unix standartları uygulanacaktır:

- **File Descriptors (0/1/2):**
  - Script, `stdin (0)` girdisine ihtiyaç duymaz.
  - Servis çıktıları `stdout (1)` üzerinden JSON olarak basılır.
  - Hata mesajları `stderr (2)` kanalına yönlendirilir.
  
- **TTY vs Pipes:**
  - `journalctl` komutu çalıştırılırken, interaktif moddan kaçınmak için `--no-pager` parametresi kullanılır (Pipe dostu çıktı).
  - Python `subprocess.PIPE` kullanılarak alt süreçlerin çıktıları yakalanır ve parse edilir.

## 4. Güvenlik ve İzleme (Monitoring & Logging)
- **Self-Check:** Script başlangıçta UID kontrolü yaparak yetki seviyesini doğrular.
- **Filtreleme:** `journalctl` logları içinde "ERROR" ve "WARNING" seviyeleri filtrelenerek gürültü azaltılır.
- **JSON-First:** Tüm çıktılar, başka araçların (SIEM vb.) okuyabilmesi için ham metin yerine JSON formatında üretilir.
