from PySide6.QtWidgets import QPushButton


class SideBarButton(QPushButton):
    def __init__(self, label=None):
        super().__init__(label)
        self.setMinimumSize(100, 100)
        self.setMaximumSize(200, 200)
        self.setText(label)



