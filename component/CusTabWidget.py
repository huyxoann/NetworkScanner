from PySide6.QtWidgets import QTabWidget, QWidget, QVBoxLayout

from component.CusListWidget import CusListWidget


class CusTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        # self.deviceTab = QWidget()
        # # self.deviceTabLabel = TabLabel("Device")
        # self.deviceTabLayout = QVBoxLayout(self.deviceTab)
        # # self.layoutDeviceTab.addWidget(self.deviceTabLabel)
        # self.deviceList = CusListWidget()
        # self.deviceTabLayout.addWidget(self.deviceList)
        # self.addTab(self.deviceTab, "Device")
        #
        # self.networkTab = QWidget()
        # self.networkTabLayout = QVBoxLayout(self.networkTab)
        # self.addTab(self.networkTab, "Network")

    def addDevicesToList(self, devices):
        self.deviceList.addItem(devices)

