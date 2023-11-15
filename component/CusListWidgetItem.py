import socket

from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QListWidgetItem

from assets.theme import CustomTheme as theme


class DeviceItem(QListWidgetItem):
    def __init__(self, device):
        super().__init__()
        self.device = device
        self.setText(f"{self.get_host_from_ip()}: {self.device.ip}")
        self.setFont(QFont(theme.normalFont, 25))
        self.setForeground(QColor(theme.textColor))

    def get_host_from_ip(self):
        temp = self.device.ip.split(".")[3]
        if temp == "1":
            return "Router"
        try:
            hostname, _, _ = socket.gethostbyaddr(self.device.ip)
            return hostname
        except socket.herror:
            return "Generic"


