import threading

from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QAbstractItemView, QGridLayout)

from assets.theme import CustomTheme as theme
from assets.icon import CustomIcon as icon
from component.CusButton import CusButton
from component.CusListWidgetItem import DeviceItem
from component.CusNormalLabel import CusNormalLabel
from component.CusTabWidget import CusTabWidget
from component.CusTextInput import CusTextInput
from component.CusTitleLabel import CusTitleLabel
from component.CusToolButton import CusToolButton
from controller.MainController import MainController
from controller.get_public_ip import get_public_ip
from controller.get_bssid import get_bssid
from model.Device import Device


class ScanningWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ip_input = None
        self.deviceTabLayout = None
        self.tabWidget = None
        self.deviceTab = None
        self.num_devices = None
        self.scan_btn = None
        self.subTitle = None
        self.network_ip = None
        self.header_horizontal_vertical = None
        self.title = None
        self.header_horizontal = None
        self.layout = None
        self.window_layout = None
        self.devices_info_list = []
        self.router_ip = None
        self.setupUI(self)

    def setupUI(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Widget")
        MainWindow.resize(1080, 720)
        MainWindow.setWindowTitle("Network Scanner")
        MainWindow.setStyleSheet(f'background-color: {theme.backgroundColor};')

        # Lưu thông tin IP đang kết nối
        self.router_ip = MainController.get_router_ip()
        self.devices_info_list = []
        self.devices = []

        self.window_layout = QHBoxLayout()

        # Layout cho phần Header
        self.layout = QVBoxLayout()
        self.header_horizontal = QHBoxLayout()

        self.title = CusTitleLabel("Network Scanner Application")

        # Layout này nằm trong phần layout heading
        self.header_horizontal_vertical = QVBoxLayout()
        self.network_ip = CusNormalLabel(f"Network is connecting: {MainController.get_network_name()}")
        self.subTitle = CusNormalLabel("Press 'Scan' to scan devices in network")
        self.scan_btn = CusToolButton(icon.scanIcon, "Scan")
        self.scan_btn.clicked.connect(lambda: self.display_devices())

        self.num_devices = CusNormalLabel("Devices are available: Press Scan to see")

        self.header_horizontal_vertical.addWidget(self.network_ip)
        self.header_horizontal_vertical.addWidget(self.subTitle)

        self.header_horizontal_vertical.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.header_horizontal_vertical.setSpacing(20)

        self.tabWidget = CusTabWidget()
        # Device Tab
        self.deviceTab = QWidget()
        self.deviceTabLayout = QVBoxLayout(self.deviceTab)
        self.deviceList = QListWidget()
        self.deviceList.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.deviceTabLayout.addWidget(self.deviceList)

        # Network Tab
        self.networkTab = QWidget()
        self.networkTabLayout = QVBoxLayout(self.networkTab)
        self.networkTabLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.network_name = CusTitleLabel(f'{MainController.get_network_name()}')
        self.public_ip = CusNormalLabel(f'Public IP: {get_public_ip()}')

        self.access_points_label = CusTitleLabel("Access Points")
        self.access_points_widget = QWidget()
        self.access_points_layout = QGridLayout(self.access_points_widget)

        self.ssid_label = CusNormalLabel("SSID")
        self.ssid_value = CusNormalLabel(f'{MainController.get_network_name()}')
        self.bssid_label = CusNormalLabel("BSSID")
        self.bssid_value = CusNormalLabel(f'{get_bssid()}')

        self.access_points_layout.addWidget(self.ssid_label, 0, 0)
        self.access_points_layout.addWidget(self.ssid_value, 0, 1)
        self.access_points_layout.addWidget(self.bssid_label, 1, 0)
        self.access_points_layout.addWidget(self.bssid_value, 1, 1)

        self.network_setup_label = CusTitleLabel("Network Setup")
        self.network_setup_widget = QWidget()
        self.network_setup_layout = QGridLayout(self.network_setup_widget)

        self.netmask_label = CusNormalLabel("Netmask")
        self.netmask_value = CusNormalLabel(f'192.168.1.0/24')
        self.gateway_label = CusNormalLabel("Gateway")
        self.gateway_value = CusNormalLabel(f'192.168.1.1')

        self.network_setup_layout.addWidget(self.netmask_label, 0, 0)
        self.network_setup_layout.addWidget(self.netmask_value, 0, 1)
        self.network_setup_layout.addWidget(self.gateway_label, 1, 0)
        self.network_setup_layout.addWidget(self.gateway_value, 1, 1)

        self.networkTabLayout.addWidget(self.network_name)
        self.networkTabLayout.addWidget(self.public_ip)
        self.networkTabLayout.addWidget(self.access_points_label)
        self.networkTabLayout.addWidget(self.access_points_widget)
        # self.networkTabLayout.addWidget(self.network_setup_label)
        # self.networkTabLayout.addWidget(self.network_setup_widget)

        # Tool tab
        self.toolTab = QWidget()
        self.toolTabLayout = QVBoxLayout(self.toolTab)
        self.toolTabLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.ping_widget = QWidget()
        self.ping_layout = QHBoxLayout(self.ping_widget)
        self.ip_input = CusTextInput()
        self.ping_button = CusButton("Ping!")
        self.traceroute_button = CusButton("Traceroute!")
        self.ping_layout.addWidget(self.ping_button)
        self.ping_layout.addWidget(self.traceroute_button)

        # self.toolTabLayout.addWidget(self.ip_input)
        self.toolTabLayout.addWidget(self.ping_widget)

        self.tabWidget.addTab(self.deviceTab, "Devices")
        self.tabWidget.addTab(self.networkTab, "Network")
        # self.tabWidget.addTab(self.toolTab, "Tool")

        self.header_horizontal.addWidget(self.title)
        self.header_horizontal.addLayout(self.header_horizontal_vertical)
        self.header_horizontal.addWidget(self.scan_btn)
        self.header_horizontal.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignTop)

        self.layout.addLayout(self.header_horizontal)
        self.layout.addWidget(self.num_devices)
        self.layout.addWidget(self.tabWidget)

        self.window_layout.addLayout(self.layout)

        MainWindow.setLayout(self.window_layout)

    def display_devices(self):
        self.deviceList.clear()
        self.devices_info_list = MainController.scan_network(MainController.get_router_ip())

        for device_info in self.devices_info_list:
            my_thread = threading.Thread(target=self.add_item, args=(device_info,))
            my_thread.start()
        print("Scan Done!")

        self.display_num_devices()

    def add_item(self, device_info):
        device = Device(ip=device_info[0], mac=device_info[1])
        self.devices.append(device)
        item = DeviceItem(device)
        self.deviceList.addItem(item)

    def display_num_devices(self):
        self.num_devices.setText(f'Devices are available: {len(self.devices_info_list)} devices.')

    def get_router_ip(self):
        local_ip = MainController.get_ip()
        parts = local_ip.split('.')
        router_ip = f'{parts[0]}.{parts[1]}.{parts[2]}.1'
        return router_ip

    def get_device(self):
        current_item = self.deviceList.selectedItems()[0]
        data = str(current_item.data(0))
        data = data.split(' ')[1]

        for i in range(len(self.devices)):
            item = self.devices[i]
            if data == item.ip:
                return self.devices[i]
