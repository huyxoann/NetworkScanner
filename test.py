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

# Hàm tìm kiếm và trả về dòng chứa chuỗi trong file
# def find_line_containing_string(file_path, search_string):
#     with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
#         lines = file.readlines()
#         for line in lines:
#             if search_string in line:
#                 return line.strip()
#     return None
#
# file_path = 'data/manuf.txt'
# search_string = '00:00:04'
#
#
#
# result_line = find_line_containing_string(file_path, search_string)
# if result_line:
#     print("Dòng chứa chuỗi:")
#     print(result_line)
# else:
#     print("Không tìm thấy chuỗi trong file.")
#
# shorted_name = result_line.split("\t")
# print(shorted_name)



