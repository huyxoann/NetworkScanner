from PySide6 import QtCore
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QVBoxLayout, QPushButton

from assets .icon import CustomIcon as icon
from component.SideBarButton import SideBarButton


class SideBar(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.main_window_btn = SideBarButton()
        self.menu_icon = QIcon(icon.menuIcon)
        self.main_window_btn.setIcon(self.menu_icon)


        self.addWidget(self.main_window_btn)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

