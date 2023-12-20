import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            public_ip = data['ip']
            return public_ip
        else:
            print("Không thể lấy được địa chỉ IP công cộng.")
    except Exception as e:
        print("Đã xảy ra lỗi:", e)

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        print("Địa chỉ IP công cộng của bạn là:", public_ip)
