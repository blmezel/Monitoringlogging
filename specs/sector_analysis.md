# 🌐 Sektörel Konumlandırma (Atlas Studio Analizi)

**Proje Kategorisi:** DevSecOps & Infrastructure Security
**Odak Alanı:** System Observability (Sistem Gözlenebilirliği) ve Log Management.

**Endüstriyel Karşılıklar:**
Bu proje, sektörde kullanılan profesyonel araçların (Atlas Studio listesindeki) terminal tabanlı ve "hafif sıklet" (lightweight) bir simülasyonudur:

1.  **Monitoring (İzleme):** Sektörde **Prometheus** veya **Nagios** kullanılır. Biz bu projede bunu `systemctl` sorguları ile sağladık.
2.  **Log Analysis (Log Analizi):** Sektörde **Wazuh**, **Splunk** veya **ELK Stack** kullanılır. Biz bunu `journalctl` filtreleme motoru ile yaptık.
3.  **Alerting (Uyarı):** Sektörde **PagerDuty** kullanılır. Biz bunu Shell Script uyarı mekanizması ile çözdük.
