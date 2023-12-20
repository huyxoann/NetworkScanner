from PySide6.QtWidgets import QMessageBox

from assets.theme import CustomTheme as theme


class MessageDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText("Đã gửi Wake on LAN thành công!")
        self.setStyleSheet(f'font-size: {theme.normalTextSize}px; color: {theme.textColor}; font-family: {theme.normalFont}')
        self.setWindowTitle("Thông báo")
