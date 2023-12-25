from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from assets.theme import CustomTheme as theme
from screens.DeviceDetailWindow import DeviceDetail
from screens.PingToolWindow import PingToolWindow
from screens.PingWindow import PingWindow
from screens.ScanningWindow import ScanningWidget
from screens.TracerouteWindow import TracerouteWindow
from screens.FindOpenPort import FindOpenPort
from wakeonlan import send_magic_packet

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

        self.scanning_widget.ping_button.clicked.connect(lambda: self.open_ping_tool_window())

        self.page_stack.append(self.scanning_widget)

        self.stacked_widget.addWidget(self.scanning_widget)

    def open_ping_tool_window(self):
        self.ping_tool_window = PingToolWindow()

    def open_device_info(self, device):
        # Màn hình device device detail
        self.device_detail = DeviceDetail(device)
        self.device_detail.device = self.scanning_widget.get_device()

        self.device_detail.back_button.clicked.connect(lambda: self.go_back())

        self.stacked_widget.addWidget(self.device_detail)
        self.page_stack.append(self.device_detail)
        self.stacked_widget.setCurrentWidget(self.device_detail)

        self.device_detail.ping_button.clicked.connect(lambda: self.open_ping_window())
        self.device_detail.traceroute.clicked.connect(lambda: self.open_traceroute())
        self.device_detail.find_open_ports.clicked.connect(lambda: self.open_find_open_ports())
        self.device_detail.wake_on_lan.clicked.connect(lambda: self.device_detail.run_wake_on_lan())


    def go_back(self):
        if self.page_stack:
            previous_page = self.page_stack.pop()
            self.stacked_widget.setCurrentWidget(self.page_stack[len(self.page_stack) - 1])

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

    def open_find_open_ports(self):
        self.find_open_ports = FindOpenPort(self.device_detail.device)
        self.find_open_ports.back_button.clicked.connect(lambda: self.go_back())
        self.stacked_widget.addWidget(self.find_open_ports)
        self.page_stack.append(self.find_open_ports)
        self.stacked_widget.setCurrentWidget(self.find_open_ports)

    # def wake_on_lan(self):

