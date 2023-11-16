from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from assets.theme import CustomTheme as theme
from screens.DeviceDetailWindow import DeviceDetail
from screens.ScanningWindow import ScanningWidget


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scanning_widget = None
        self.central_layout = None
        self.stacked_widget = None
        self.setupUI(self)




    def setupUI(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Widget")
        Window.resize(1080, 720)
        Window.setWindowTitle("Network Scanner")
        Window.setStyleSheet(f'background-color: {theme.backgroundColor};')

        self.stacked_widget = QStackedWidget()
        self.central_layout = QVBoxLayout(self)
        self.central_layout.addWidget(self.stacked_widget)

        # Màn hình scan widget
        self.scanning_widget = ScanningWidget()
        self.scanning_widget.deviceList.itemClicked.connect(self.open_device_info)

        # Màn hình device device detail
        self.device_detail = DeviceDetail()

        self.stacked_widget.addWidget(self.scanning_widget)
        self.stacked_widget.addWidget(self.device_detail)

    def open_device_info(self):
        self.stacked_widget.setCurrentWidget(self.device_detail)
