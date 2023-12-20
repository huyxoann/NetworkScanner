import math

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QToolButton, QLabel
from assets.theme import CustomTheme as theme
from assets.icon import CustomIcon as iconpack


class CusToolButton(QToolButton):
    def __init__(self, icon=None, label=None):
        super().__init__()
        icon_img = QIcon(icon)
        self.setIcon(icon_img)
        self.setText(label)
        button_size = 100
        self.setFixedSize(button_size, button_size)
        self.setToolTip(label)
        icon_size = math.floor(button_size / 100 * 90)
        self.setIconSize(QSize(icon_size, icon_size))
        self.setStyleSheet(
            f'background-color: {theme.surfaceColor};'
            f' color: {theme.textColor};'
            f' border-radius: {theme.borderButtonRadius};'
            f'font-size: {theme.titleTextSize}px;'
            f' font-family: {theme.titleFont};'
            )
