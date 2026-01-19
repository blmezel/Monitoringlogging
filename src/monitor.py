import platform
import os
import sys
import json
import subprocess

def run_command(command):
    """Terminal komutunu calistirir ve ciktisini alir."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def check_service_status(service_name):
    """Belirtilen servisin (systemd) durumunu kontrol eder."""
    # Active/Inactive durumunu sor
    status = run_command(f"systemctl is-active {service_name}")
    
    # Detayli bilgi al ve JSON icin basit status don
    if status == "active":
        return {"service": service_name, "status": "running", "is_active": True}
    else:
        return {"service": service_name, "status": "stopped", "is_active": False}

def check_recent_logs(service_name, lines=5):
    """Servise ait son loglari ceker (Hata ayiklama icin)."""
    # journalctl ile son satirlari al, --no-pager ile takilmasini engelle
    logs = run_command(f"journalctl -u {service_name} -n {lines} --no-pager")
    return logs.split('\n') if logs else []

def main_monitor():
    """Ana izleme fonksiyonu."""
    report = {
        "meta": {
            "os": platform.system(),
            "root_user": (os.geteuid() == 0)
        },
        "services": [],
        "system_health": "stable"
    }

    # Hedef Servisler (Ornegin SSH ve Cron servislerine bakalim)
    target_services = ["ssh", "cron"]

    for svc in target_services:
        # 1. Servis Durumunu Al
        svc_data = check_service_status(svc)
        
        # 2. Eger calisiyorsa son loglari da ekle
        if svc_data["is_active"]:
            svc_data["recent_logs"] = check_recent_logs(svc, lines=2)
        
        report["services"].append(svc_data)

    return report

if __name__ == "__main__":
    # Once Root kontrolu
    if os.geteuid() != 0:
        print(json.dumps({"error": "Lutfen sudo ile calistirin (Root yetkisi gerekli)."}, indent=4))
        sys.exit(1)

    # Raporu uret ve JSON olarak bas
    print(json.dumps(main_monitor(), indent=4))
