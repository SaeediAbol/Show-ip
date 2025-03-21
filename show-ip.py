import requests
import json

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'success':
            print("\n📡 اطلاعات آی‌پی:")
            print(f"🌍 کشور: {data['country']} ({data['countryCode']})")
            print(f"🏙 منطقه: {data['regionName']}")
            print(f"🏢 شهر: {data['city']}")
            print(f"📶 ISP: {data['isp']}")
            print(f"🕸 سازمان: {data['org']}")
            print(f"📍 مختصات: {data['lat']}, {data['lon']}")
            print(f"🕒 منطقه زمانی: {data['timezone']}")
        else:
            print("❌ خطا در دریافت اطلاعات!")
            
    except Exception as e:
        print(f"❌ خطای ارتباطی: {e}")

if __name__ == "__main__":
    ip = input("لطفاً آی‌پی را وارد کنید (یا Enter برای آی‌پی خودتان): ").strip()
    
    if not ip:
        # دریافت آی‌پی عمومی کاربر
        ip = requests.get('https://api.ipify.org').text
    
    get_ip_info(ip)
