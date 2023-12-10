import socket


class Device:
    def __init__(self, ip="", hostname="", mac="", mac_vendor="", os="", netbios_name="", network_protocol=""):
        self.ip = ip
        self.hostname = hostname
        self.mac = mac
        self.mac_vendor = mac_vendor
        self.os = os
        self.netbios_name = netbios_name
        self.network_protocol = network_protocol

    def __str__(self):
        return f'{self.ip}: {self.mac}'
