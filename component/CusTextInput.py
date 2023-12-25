from PySide6.QtWidgets import QLineEdit

from assets.theme import CustomTheme as theme


class CusTextInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f'background-color: {theme.surfaceColor}; color: {theme.textColor}; border-radius: {theme.borderButtonRadius};font-size: {theme.titleTextSize}px; font-family: {theme.titleFont}')