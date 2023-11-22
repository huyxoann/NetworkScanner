from PySide6 import QtCore
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QToolButton, QPushButton

from assets.icon import CustomIcon as icon
from assets.theme import CustomTheme as theme
from component.CusToolButton import CusToolButton


class DeviceDetail(QWidget):
    def __init__(self, device):
        super().__init__()
        self.back_button = None
        self.device = device
        self.setupUI(self)

    def setupUI(self, window):

        if not window.objectName():
            window.setObjectName(u"Widget")
        window.resize(1080, 720)
        window.setWindowTitle("Network Scanner")
        window.setStyleSheet(f'background-color: {theme.backgroundColor};')

        self.layout = QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Tạo appbar
        self.app_bar = QWidget()
        self.app_bar_layout = QHBoxLayout()
        self.app_bar_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.back_arrow_icon = QIcon(icon.back_arrow)
        self.back_button = CusToolButton(self.back_arrow_icon, "<==")
        self.back_button.setIcon(self.back_arrow_icon)

        self.app_bar_layout.addWidget(self.back_button)

        # Set layout cho appbar và thêm vào layout
        self.app_bar.setLayout(self.app_bar_layout)
        self.layout.addWidget(self.app_bar)

        window.setLayout(self.layout)





