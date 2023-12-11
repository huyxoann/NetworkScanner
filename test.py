# import socket
# import netifaces
#
# # Lấy địa chỉ IP của thiết bị
# ip = socket.gethostbyname('192.168.1.5')
#
# # Lấy tên host
# host = socket.gethostbyaddr(ip)[0]
#
# print(f"Tên host: {host}")
#
#
# def get_device_type(interface):
#     # Kiểm tra nếu giao diện không có địa chỉ MAC
#     if netifaces.AF_LINK not in netifaces.ifaddresses(interface):
#         return "Không thể xác định"
#
#     # Lấy địa chỉ MAC của giao diện mạng
#     mac_address = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr'].upper()
#     print(mac_address)
#
#     # Kiểm tra địa chỉ MAC để xác định loại thiết bị
#     if mac_address.startswith('74:4C:A1'):
#         return "OUI"
#     elif mac_address.startswith('08:00:27'):
#         return "Loại thiết bị B"
#     else:
#         return "Không xác định"
#
#
# interfaces = netifaces.interfaces()
#
# for interface in interfaces:
#     device_type = get_device_type(interface)
#     print(f"Giao diện: {interface}, Loại thiết bị: {device_type}")
import time

# Hàm tìm kiếm và trả về dòng chứa chuỗi trong file

# import scapy.all as scapy
#
# def ping(ip):
#     """Gửi một gói ICMP Echo Request đến một địa chỉ IP.
#
#     Args:
#         ip: Địa chỉ IP của thiết bị cần ping.
#
#     Returns:
#         Kết quả của lệnh ping.
#     """
#     packet = scapy.IP(dst=ip) / scapy.ICMP()  # Tạo gói tin ICMP Echo Request
#
#     try:
#         reply = scapy.sr1(packet, timeout=2, verbose=False)  # Gửi và nhận phản hồi
#
#         if reply:
#             return f"Reply from {reply.src}: bytes={len(reply)}, time={reply.time*1000:.2f} ms"
#         else:
#             return "Request timed out."
#     except Exception as e:
#         return f"Error: {str(e)}"
#
# result = ping("192.168.1.10")
# print(result)
#
# import scapy.all as scapy
#
#
# def ping_to_device(ip):
#     packet = scapy.IP(dst=ip) / scapy.ICMP()  # Tạo gói tin ICMP Echo Request
#
#     try:
#         sent_time = time.time()
#         reply = scapy.sr1(packet, timeout=5, verbose=False)  # Gửi và nhận phản hồi
#         received_time = time.time()
#         if reply:
#             print(f"Reply from {reply.src}: bytes={len(reply)}, time={(received_time - sent_time) * 1000:.2f} ms")
#         else:
#             print("Request timed out.")
#     except Exception as e:
#         print(f"Error: {str(e)}")
#
#     time.sleep(1)
#
#
# result = ping_to_device("192.168.1.3")
# print(result)

import sys
from scapy.all import *
from scapy.layers.inet import ICMP, IP


def traceroute(target, max_hops=30):
    ttl = 1
    while ttl <= max_hops:
        pkt = IP(dst=target, ttl=ttl) / ICMP()
        reply = sr1(pkt, verbose=False, timeout=5)

        if reply is None:
            print(f"{ttl}. *")
        elif reply.type == 11:
            print(f"{ttl}. {reply.src} (Intermediate Router)")
        elif reply.type == 0:
            print(f"{ttl}. {reply.src} (Destination Reached)")
            break

        ttl += 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python traceroute.py <target>")
    else:
        target = sys.argv[1]
        print(f"Traceroute to {target}, 30 hops max\n")
        traceroute(target)

