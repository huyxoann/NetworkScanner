from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import QListWidgetItem

from assets.theme import CustomTheme as theme


class DeviceItem(QListWidgetItem):
    def __init__(self, device):
        super().__init__()
        self.setText(device.__str__())
        self.setFont(QFont(theme.normalFont, 25))
        self.setForeground(QColor(theme.textColor))

