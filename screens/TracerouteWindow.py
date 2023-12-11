import time

from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtStateMachine import QStateMachine, QState
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QLabel, QTextEdit

from assets.icon import CustomIcon as iconpack
from assets.theme import CustomTheme as theme
from component.CusButton import CusButton
from component.CusNormalLabel import CusNormalLabel
from component.CusTitleLabel import CusTitleLabel
from component.CusToolButton import CusToolButton
from model.Device import Device

from controller.traceroute import traceroute


class TracerouteWindow(QWidget):
    def __init__(self, device):
        super().__init__()
        self.layout = None
        self.app_bar = None
        self.app_bar_layout = None
        self.back_arrow_icon = None
        self.back_button = None
        self.device = None
        self.setupUI(self, device=device)

    def setupUI(self, window, device: Device):
        if not window.objectName():
            window.setObjectName(u"Widget")
        window.resize(1080, 720)
        window.setWindowTitle("Network Scanner")
        window.setStyleSheet(f'background-color: {theme.backgroundColor};')

        self.device = device

        self.layout = QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # State management
        self.state_machine = QStateMachine()
        self.state1 = QState()
        self.state2 = QState()

        # Thêm trạng thái vào máy trạng thái
        self.state_machine.addState(self.state1)
        self.state_machine.addState(self.state2)

        # Đặt trạng thái khởi tạo
        self.state_machine.setInitialState(self.state1)



        # Tạo appbar
        self.app_bar = QWidget()
        self.app_bar_layout = QHBoxLayout()
        self.app_bar_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.back_arrow_icon = QIcon(iconpack.back_arrow)
        self.back_button = CusToolButton(self.back_arrow_icon, "<==")
        self.back_button.setIcon(self.back_arrow_icon)

        self.title = CusTitleLabel(f"Traceroute")
        self.run_button = CusButton("Run")
        # self.run_button.clicked.connect(lambda: self.run_traceroute())

        self.app_bar_layout.addWidget(self.back_button)
        self.app_bar_layout.addStretch(1)
        self.app_bar_layout.addWidget(self.title)
        self.app_bar_layout.addStretch(1)
        self.app_bar_layout.addWidget(self.run_button)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.content_box = QWidget()
        self.content_box_layout = QVBoxLayout()

        # Chứa target host và hop point
        self.general_widget = QWidget()
        self.general_layout = QHBoxLayout()
        self.general_widget.setLayout(self.general_layout)
        self.general_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Target host
        self.target_host_widget = QWidget()
        self.target_host_layout = QVBoxLayout()
        self.target_host_widget.setLayout(self.target_host_layout)

        self.target_host_label = CusNormalLabel("Target host")
        self.target_host_layout.addWidget(self.target_host_label)

        self.target_host_value_widget = QWidget()
        self.target_host_value_layout = QHBoxLayout()
        self.target_host_value_widget.setLayout(self.target_host_value_layout)
        self.target_host_layout.addWidget(self.target_host_value_widget)
        self.target_host_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        label = QLabel()
        icon = QPixmap(iconpack.desktop_icon)
        label.setPixmap(icon)
        self.host_name_value = CusNormalLabel(self.device.hostname)
        self.target_host_value_layout.addWidget(label)
        self.target_host_value_layout.addWidget(self.host_name_value)

        # Hop
        self.hops_widget = QWidget()
        self.hops_layout = QVBoxLayout()
        self.hops_widget.setLayout(self.hops_layout)

        self.hops_label = CusNormalLabel("# Hops")
        self.hops_layout.addWidget(self.hops_label)

        self.hops_value_widget = QWidget()
        self.hops_value_layout = QHBoxLayout()
        self.hops_value_widget.setLayout(self.hops_value_layout)
        self.hops_layout.addWidget(self.hops_value_widget)
        self.hops_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        label = QLabel()
        icon = QPixmap(iconpack.internet)
        label.setPixmap(icon)
        self.hops_data = CusNormalLabel("--")
        self.hops_value_layout.addWidget(label)
        self.hops_value_layout.addWidget(self.hops_data)

        # Results
        self.results_value = QTextEdit(self)
        self.results_value.setPlainText("")
        self.results_value.setReadOnly(True)
        self.results_value.setStyleSheet("font-size: 30px")

        # Thiết lập chuyển đổi giữa các trạng thái khi nút được nhấn
        self.transition_to_running = self.state1.addTransition(self.run_button.clicked, self.state2)
        self.transition_to_normal = self.state2.addTransition(self.run_button.clicked, self.state1)

        # Kết nối signal để thực hiện hành động khi vào mỗi trạng thái
        self.state1.entered.connect(self.on_state1_entered)
        self.state2.entered.connect(self.on_state2_entered)


        self.app_bar.setLayout(self.app_bar_layout)
        self.scroll_area.setWidget(self.content_box)
        self.content_box.setLayout(self.content_box_layout)
        self.content_box_layout.addWidget(self.general_widget)
        self.content_box_layout.addWidget(self.results_value)

        self.general_layout.addWidget(self.general_widget)
        self.general_layout.addWidget(self.target_host_widget)
        self.general_layout.addWidget(self.hops_widget)

        self.layout.addWidget(self.app_bar)
        self.layout.addWidget(self.scroll_area)

        # Bắt đầu máy trạng thái
        self.state_machine.start()

        window.setLayout(self.layout)

    def run_traceroute(self):
        self.results_value.setPlainText(f"Traceroute to {self.device.ip}, 30 hops max")
        ttl = 1
        max_hops = 30

        while ttl <= max_hops:
            result = traceroute(self.device.ip, ttl)
            self.results_value.setPlainText(self.results_value.toPlainText() + "\n" + result)
            self.results_value.repaint()
            if result.__contains__("Destination Reached"):
                self.hops_data.setText(f"{ttl}")
                break
            ttl += 1
            time.sleep(1)

    def on_state1_entered(self):
        # Cập nhật nội dung khi vào trạng thái 1
        self.run_button.setText("Run")
        self.run_button.setEnabled(True)

    def on_state2_entered(self):
        # Cập nhật nội dung khi vào trạng thái 2
        self.run_button.setText("Pause")
        self.run_button.setEnabled(False)

        self.run_traceroute()

        self.on_state1_entered()
