from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from component.CusNormalLabel import CusNormalLabel


class PingItemElement(QWidget):
    def __init__(self, icon_url="--", title="--", value="--"):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.icon_label = QLabel()
        self.icon = QPixmap(icon_url).scaled(50, 50)
        self.icon_label.setPixmap(self.icon)
        self.title = CusNormalLabel(title)
        self.value = CusNormalLabel(f'{value}')

        self.layout.addWidget(self.icon_label)
        self.layout.addWidget(self.title)
        self.layout.addStretch(1)
        self.layout.addWidget(self.value)
    def setValue(self, value):
        self.value.setText(value)


