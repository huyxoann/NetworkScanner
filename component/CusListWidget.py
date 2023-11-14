import PySide6
from PySide6.QtWidgets import QListWidget


class CusListWidget(QListWidget):
    def __init__(self):
        super().__init__()

    def addItemToList(self, device):
        self.addItem(device)