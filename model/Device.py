import socket


class Device:
    def __init__(self, ip, hostname="", mac="", port="", os="", connect_status="", network_protocol=""):
        self.ip = ip
        self.hostname = hostname
        self.mac = mac
        self.port = port
        self.os = os
        self.connect_status = connect_status
        self.network_protocol = network_protocol

    def __str__(self):
        return f'{self.ip}'
