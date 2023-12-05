from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from assets.icon import CustomIcon as icon
from assets.theme import CustomTheme as theme
from model.Device import Device
from component.CusTitleLabel import CusTitleLabel
from component.CusToolButton import CusToolButton


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

        # Set layout cho appbar và thêm vào layout
        self.app_bar.setLayout(self.app_bar_layout)
        self.content_box.setLayout(self.content_box_layout)
        self.layout.addWidget(self.app_bar)
        self.layout.addWidget(self.content_box)

        window.setLayout(self.layout)





