import socket

from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from assets.icon import CustomIcon as icon
from assets.theme import CustomTheme as theme
from component.CusButton import CusButton
from component.CusNormalLabel import CusNormalLabel
from model.Device import Device
from component.CusTitleLabel import CusTitleLabel
from component.CusToolButton import CusToolButton

from controller.get_mac_vendor import get_mac_vendor
from controller.get_hostname_by_ip import get_hostname_by_ip
from controller.get_os_using_scapy import get_os_using_scapy

from screens.PingWindow import PingWindow


class DeviceDetail(QWidget):
    def __init__(self, device: Device):
        super().__init__()
        self.layout = None
        self.app_bar = None
        self.app_bar_layout = None
        self.back_arrow_icon = None
        self.back_button = None
        self.device = None
        self.setupUI(self, device)

    def setupUI(self, window, device: Device):

        if not window.objectName():
            window.setObjectName(u"Widget")
        window.resize(1080, 720)
        window.setWindowTitle("Network Scanner")
        window.setStyleSheet(f'background-color: {theme.backgroundColor};')

        self.device = device
        self.load_device_information(device)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Tạo appbar
        self.app_bar = QWidget()
        self.app_bar_layout = QHBoxLayout()
        self.app_bar_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.back_arrow_icon = QIcon(icon.back_arrow)
        self.back_button = CusToolButton(self.back_arrow_icon, "<==")
        self.back_button.setIcon(self.back_arrow_icon)

        self.title = CusTitleLabel(f"Device Detail: ")

        self.app_bar_layout.addWidget(self.back_button)
        self.app_bar_layout.addWidget(self.title)

        self.content_box = QWidget()
        self.content_box_layout = QVBoxLayout()

        self.host_name = CusTitleLabel(f'{self.device.hostname}')
        self.content_box_layout.addWidget(self.host_name)

        os = CusNormalLabel(f'{self.device.os}')
        self.content_box_layout.addWidget(os)

        # Manage the device
        self.manage_device_widget = QWidget()
        self.manage_device_layout = QVBoxLayout()
        self.manage_device_widget.setLayout(self.manage_device_layout)
        self.manage_device_label = CusTitleLabel("Manage Device:")
        self.manage_device_layout.addWidget(self.manage_device_label)
        self.manage_device_items_layout = QHBoxLayout()
        self.manage_device_layout.addLayout(self.manage_device_items_layout)
        self.manage_device_items_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        # Ping button
        self.ping_button = CusButton("Ping")
        self.manage_device_items_layout.addWidget(self.ping_button)

        # Traceroute button
        self.traceroute = CusButton("Traceroute")
        self.manage_device_items_layout.addWidget(self.traceroute)

        # Find open ports
        self.find_open_ports = CusButton("Find open ports")
        self.manage_device_items_layout.addWidget(self.find_open_ports)

        # Wake on LAN
        self.wake_on_lan = CusButton("Wake on LAN")
        self.manage_device_items_layout.addWidget(self.wake_on_lan)

        # Network Details Box
        self.network_details_widget = QWidget()
        self.network_details_widget_layout = QVBoxLayout()
        self.network_details_widget.setLayout(self.network_details_widget_layout)

        network_details_title = CusTitleLabel("Network details:")
        self.network_details_widget_layout.addWidget(network_details_title)

        self.ndw = QHBoxLayout()
        self.network_details_widget_layout.addLayout(self.ndw)

        self.ndw_label_box = QVBoxLayout()
        self.ndw_value_box = QVBoxLayout()

        self.ndw.addLayout(self.ndw_label_box)
        self.ndw.addLayout(self.ndw_value_box)

        # IP Address
        ip_address_label = CusNormalLabel("IP Address")
        self.ndw_label_box.addWidget(ip_address_label)
        ip_address_value = CusNormalLabel(f'{self.device.ip}')
        self.ndw_value_box.addWidget(ip_address_value)

        # Mac Address
        mac_address_label = CusNormalLabel("MAC Address")
        self.ndw_label_box.addWidget(mac_address_label)
        mac_address_label = CusNormalLabel(f'{self.device.mac.upper()}')
        self.ndw_value_box.addWidget(mac_address_label)

        # Mac Vendor
        mac_vendor_label = CusNormalLabel("MAC Vendor")
        self.ndw_label_box.addWidget(mac_vendor_label)
        mac_split = self.device.mac.split(":")
        mac_prefix = f"{mac_split[0]}:{mac_split[1]}:{mac_split[2]}".upper()
        self.device.mac_vendor = get_mac_vendor(mac_prefix)
        mac_vendor_value = CusNormalLabel(f'{self.device.mac_vendor}')
        self.ndw_value_box.addWidget(mac_vendor_value)

        # NetBIOS Name
        netbios_name_label = CusNormalLabel("NetBIOS Name")
        self.ndw_label_box.addWidget(netbios_name_label)
        netbios_name_value = CusNormalLabel(f'{self.device.netbios_name}')
        self.ndw_value_box.addWidget(netbios_name_value)

        # Set layout cho appbar và thêm vào layout
        self.app_bar.setLayout(self.app_bar_layout)
        self.content_box.setLayout(self.content_box_layout)

        self.layout.addWidget(self.app_bar)
        self.layout.addWidget(self.content_box)
        self.layout.addWidget(self.manage_device_widget)
        self.layout.addWidget(self.network_details_widget)

        window.setLayout(self.layout)

    def load_device_information(self, device: Device):
        device.hostname = get_hostname_by_ip(device.ip)

        device.netbios_name = device.hostname if device.hostname != "Generic" else "--"

        device.os = get_os_using_scapy(device.ip)



