import os
import requests
import time

API_KEY = os.environ.get("API_KEY")
SERVICE_ID = 701
QUANTITY = 100

API_URL = "https://1xpanel.com/api/v2"

CHANNELS = [
    "Prices_Tracker",
    "WhalesActivtiy"
]

def send_views(link):
    payload = {
        "key": API_KEY,
        "action": "add",
        "service": SERVICE_ID,
        "link": link,
        "quantity": QUANTITY
    }
    try:
        resp = requests.post(API_URL, data=payload, timeout=30)
        resp.raise_for_status()
        print(f"✅ {link}: تم إرسال {QUANTITY} مشاهدة")
        return True
    except Exception as e:
        print(f"❌ {link}: فشل - {e}")
        return False

if __name__ == "__main__":
    if not API_KEY:
        raise SystemExit("❌ لم يتم العثور على API_KEY")
    
    for channel in CHANNELS:
        send_views(channel)
        time.sleep(2)
    
    print("✅ انتهى!")
