import requests
import time
import os

# Список бирж для проверки (берем из переменной окружения или ставим дефолт)
EXCHANGES = os.getenv("EXCHANGES", "binance.com,bybit.com,okx.com").split(",")

def check_status():
    print("--- Start checking exchanges status ---")
    for url in EXCHANGES:
        try:
            # Делаем запрос (как браузер)
            response = requests.get(f"https://{url}", timeout=5)
            # Если код ответа 200 - всё супер
            status = "✅ ONLINE" if response.status_code == 200 else f"⚠️ ISSUE ({response.status_code})"
            print(f"{url:15} : {status}")
        except Exception as e:
            print(f"{url:15} : ❌ OFFLINE")
    print("--- Check finished ---\n")

if __name__ == "__main__":
    while True:
        check_status()
        # Ждем время из настроек (по умолчанию 60 сек)
        time.sleep(int(os.getenv("CHECK_INTERVAL", 60)))
