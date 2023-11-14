from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout


class ScanningDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        self.setFixedSize(500, 200)

        self.setWindowTitle("Scanning...")

        label = QLabel("Đang quét, vui lòng đợi...")

        layout.addWidget(label)

        self.setLayout(layout)

