from PySide6.QtWidgets import QLabel
from assets.theme import CustomTheme as theme
class CusNormalLabel(QLabel):
    def __init__(self, content=None):
        super().__init__()
        self.setText(content)
        # self.setWordWrap(True)
        self.setStyleSheet(
            f'font-size: {theme.normalTextSize}px; color: {theme.textColor}; font-family: {theme.normalFont}')