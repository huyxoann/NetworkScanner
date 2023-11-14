from PySide6.QtWidgets import QLabel
from assets.theme import CustomTheme as theme
class CusTitleLabel(QLabel):
    def __init__(self, content):
        super().__init__()
        self.setText(content)
        self.setStyleSheet(
            f'font-size: {theme.titleTextSize}px; color: {theme.textColor}; font-family: {theme.titleFont}')
        self.setWordWrap(True)
