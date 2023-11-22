from PySide6.QtWidgets import QPushButton

from assets.theme import CustomTheme as theme


class CusButton(QPushButton):
    def __init__(self, label=None):
        super().__init__()
        self.setText(label)
        self.setFixedSize(150, 50)
        self.setStyleSheet(
            f'background-color: {theme.surfaceColor}; color: {theme.textColor}; border-radius: {theme.borderButtonRadius};font-size: {theme.titleTextSize}px; font-family: {theme.titleFont}')
