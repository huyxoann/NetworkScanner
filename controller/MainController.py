import os
import socket
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

from model.Device import Device
from component.CusListWidget import CusListWidget


class MainController:
    def scan_network(router_ip):
        # arp = ARP(pdst=router_ip + "/24")
        #
        # broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        # arp_request_broadcast = broadcast / arp
        #
        # result = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        #
        # devices = []
        #
        # for sent, received in result:
        #     device = Device(ip=received.psrc, mac=received.hwsrc)
        #     devices.append(device)
        #     print(device.__str__())
        # return devices
        # Tạo một gói tin ARP request
        arp = ARP(pdst=router_ip + "/24")
        # Thay đổi subnet mạng cần quét tại đây

        # Tạo một gói tin Ethernet để bọc gói tin ARP
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")

        # Kết hợp gói tin Ethernet và ARP request
        packet = ether / arp

        # Gửi gói tin và nhận phản hồi
        result = srp(packet, timeout=1, verbose=0)[0]
        device_info = []

        # In thông tin về các thiết bị đã kết nối
        for sent, received in result:
            device_info_item = [received.psrc, received.hwsrc]
            device_info.append(device_info_item)
            print(f"IP: {received.psrc}, MAC: {received.hwsrc}")
        return device_info

    def get_router_ip(self=None):
        sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sk.connect(("8.8.8.8", 80))
        local_ip = sk.getsockname()[0]

        parts = local_ip.split('.')
        router_ip = f'{parts[0]}.{parts[1]}.{parts[2]}.1'
        return router_ip

    def get_network_name(self=None):
        output = os.popen('netsh wlan show interfaces').read()
        start = output.find('SSID') + 7
        end = output.find('\n', start)
        return output[start:end].strip()

    def get_ip(self=None):
        sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sk.connect(('8.8.8.8', 80))
        local_ip = sk.getsockname()[0]
        return local_ip
