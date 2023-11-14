from PySide6.QtWidgets import QLabel
from assets.theme import CustomTheme as theme

class TabLabel(QLabel):
    def __init__(self, content):
        super().__init__()
        self.setText(content)
        self.setStyleSheet(
            f'font-size: {theme.titleTextSize}px; color: {theme.textColor}; font-family: {theme.semiBoldFont}')
        self.setWordWrap(True)