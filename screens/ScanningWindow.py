import threading

from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QAbstractItemView)

from assets.theme import CustomTheme as theme
from component.CusButton import CusButton
from component.CusListWidgetItem import DeviceItem
from component.CusNormalLabel import CusNormalLabel
from component.CusTabWidget import CusTabWidget
from component.CusTitleLabel import CusTitleLabel
from controller.MainController import MainController
from model.Device import Device


class ScanningWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
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
        self.network_ip = CusNormalLabel(f"Mạng đang kết nối: {MainController.get_network_name()}")
        self.subTitle = CusNormalLabel("Nhấn 'Scan' để quét các thiết bị trong mạng")
        self.scan_btn = CusButton("Scan")
        self.scan_btn.clicked.connect(lambda: self.display_devices())

        self.num_devices = CusNormalLabel("Số thiết bị hoạt động: Nhấn Scan để xem")

        self.header_horizontal_vertical.addWidget(self.network_ip)
        self.header_horizontal_vertical.addWidget(self.subTitle)

        self.header_horizontal_vertical.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.header_horizontal_vertical.setSpacing(20)

        self.tabWidget = CusTabWidget()
        self.deviceTab = QWidget()
        self.deviceTabLayout = QVBoxLayout(self.deviceTab)
        self.deviceList = QListWidget()
        self.deviceList.setSelectionMode(QListWidget.SelectionMode.SingleSelection)

        self.deviceTabLayout.addWidget(self.deviceList)
        self.tabWidget.addTab(self.deviceTab, "Devices")

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
        self.num_devices.setText(f'Số thiết bị đang hoạt động: {len(self.devices_info_list)} thiết bị.')

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
