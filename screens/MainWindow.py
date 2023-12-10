from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from assets.theme import CustomTheme as theme
from screens.DeviceDetailWindow import DeviceDetail
from screens.PingWindow import PingWindow
from screens.ScanningWindow import ScanningWidget
from screens.TracerouteWindow import TracerouteWindow


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.device_detail = None
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

        self.page_stack = []

        # Màn hình scan widget
        self.scanning_widget = ScanningWidget()
        self.scanning_widget.deviceList.itemDoubleClicked.connect(
            lambda: self.open_device_info(self.scanning_widget.get_device()))

        self.page_stack.append(self.scanning_widget)

        self.stacked_widget.addWidget(self.scanning_widget)

    def open_device_info(self, device):
        # Màn hình device device detail
        self.device_detail = DeviceDetail(device)
        self.device_detail.device = self.scanning_widget.get_device()

        self.device_detail.back_button.clicked.connect(lambda: self.go_back())

        self.stacked_widget.addWidget(self.device_detail)
        self.page_stack.append(self.device_detail)
        self.stacked_widget.setCurrentWidget(self.device_detail)

        self.device_detail.ping_button.clicked.connect(lambda: self.open_ping_window())

    def go_back(self):
        if self.page_stack:
            previous_page = self.page_stack.pop()
            self.stacked_widget.setCurrentWidget(self.page_stack[len(self.page_stack)-1])

    def open_ping_window(self):
        self.ping_window = PingWindow(self.device_detail.device)
        self.ping_window.back_button.clicked.connect(lambda: self.go_back())
        self.stacked_widget.addWidget(self.ping_window)
        self.page_stack.append(self.ping_window)
        self.stacked_widget.setCurrentWidget(self.ping_window)

    def open_traceroute(self):
        self.traceroute_window = TracerouteWindow(self.device_detail.device)
        self.traceroute_window.back_button.clicked.connect(lambda: self.go_back())
        self.stacked_widget.addWidget(self.traceroute_window)
        self.page_stack.append(self.traceroute_window)
        self.stacked_widget.setCurrentWidget(self.traceroute_window)
