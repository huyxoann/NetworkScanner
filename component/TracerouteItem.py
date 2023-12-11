from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from component.CusNormalLabel import CusNormalLabel


class TracerouteItem(QWidget):
    def __init__(self, icon_url="--", reply_src="--", hop_id="--"):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.status_icon = QLabel().setPixmap(QPixmap(icon_url))
        self.reply_src = CusNormalLabel(reply_src)
        self.hop_id = CusNormalLabel(f'{hop_id}')

        self.layout.addWidget(self.status_icon)
        self.layout.addWidget(self.reply_src)

    # def setValue(self, value):
    #     self.value.setText(value)


