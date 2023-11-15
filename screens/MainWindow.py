import socket
import threading

from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QProgressBar,
                               QListWidget)
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

from assets.theme import CustomTheme as theme
from component.CusButton import CusButton
from component.CusListWidgetItem import DeviceItem
from component.CusNormalLabel import CusNormalLabel
from component.CusTabWidget import CusTabWidget
from component.CusTitleLabel import CusTitleLabel
from component.ScanningDialog import ScanningDialog
from controller.MainController import MainController
from model.Device import Device


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI(self)

    def setupUI(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Widget")
        MainWindow.resize(1080, 720)
        MainWindow.setWindowTitle("Network Scanner")
        MainWindow.setStyleSheet(f'background-color: {theme.backgroundColor};')

        self.router_ip = MainController.get_router_ip()
        self.devices = []

        self.window_layout = QHBoxLayout()

        self.layout = QVBoxLayout()
        self.header_horizontal = QHBoxLayout()

        self.title = CusTitleLabel("Network Scanner Application")

        self.header_horizontal_vertical = QVBoxLayout()
        self.network_ip = CusNormalLabel(f"Mạng đang kết nối: {MainController.get_network_name()}")
        self.subTitle = CusNormalLabel("Nhấn 'Scan' để quét các thiết bị trong mạng")
        self.scan_btn = CusButton("Scan")
        self.scan_btn.clicked.connect(lambda: self.display_devices())

        self.num_devices = CusNormalLabel("Số thiết bị hoạt động: Nhấn Scan để xem")

        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.hide()

        self.header_horizontal_vertical.addWidget(self.network_ip)
        self.header_horizontal_vertical.addWidget(self.subTitle)

        self.header_horizontal_vertical.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.header_horizontal_vertical.setSpacing(20)

        self.tabWidget = CusTabWidget()
        self.deviceTab = QWidget()
        self.deviceTabLayout = QVBoxLayout(self.deviceTab)
        self.deviceList = QListWidget()
        self.deviceTabLayout.addWidget(self.deviceList)
        self.tabWidget.addTab(self.deviceTab, "Devices")

        self.header_horizontal.addWidget(self.title)
        self.header_horizontal.addLayout(self.header_horizontal_vertical)
        self.header_horizontal.addWidget(self.scan_btn)
        self.header_horizontal.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft.AlignTop)

        self.layout.addLayout(self.header_horizontal)
        self.layout.addWidget(self.num_devices)
        self.layout.addWidget(self.tabWidget)
        self.layout.addWidget(self.progress_bar)

        self.window_layout.addLayout(self.layout)

        MainWindow.setLayout(self.window_layout)

    def display_devices(self):
        self.deviceList.clear()
        self.devices = MainController.scan_network(MainController.get_router_ip())

        for device_info in self.devices:
            my_thread = threading.Thread(target=self.add_item, args=(device_info, ))
            my_thread.start()
        print("Scan Done!")

        # self.scanningDialog.close()
        self.progress_bar.setValue(100)
        self.display_num_devices()

    def add_item(self, device_info):
        device = Device(ip=device_info[0], mac=device_info[1])
        item = DeviceItem(device)
        self.deviceList.addItem(item)

    def display_num_devices(self):
        self.num_devices.setText(f'Số thiết bị đang hoạt động: {len(self.devices)} thiết bị.')

    def get_router_ip(self):
        local_ip = MainController.get_ip()
        parts = local_ip.split('.')
        router_ip = f'{parts[0]}.{parts[1]}.{parts[2]}.1'
        return router_ip
