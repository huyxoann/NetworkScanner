import socket
import time

from PySide6 import QtCore, QtCharts
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QScrollArea

from assets.icon import CustomIcon as icon
from assets.theme import CustomTheme as theme
from component.CusButton import CusButton
from component.CusTextInput import CusTextInput
from component.PingItemElement import PingItemElement
from model.Device import Device
from component.CusTitleLabel import CusTitleLabel
from component.CusToolButton import CusToolButton
from assets.icon import CustomIcon

from controller.ping import ping_to_device


class PingToolWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = None
        self.app_bar = None
        self.app_bar_layout = None
        self.back_arrow_icon = None
        self.back_button = None
        self.device = None
        self.setupUI(self)

    def setupUI(self, window):

        if not window.objectName():
            window.setObjectName(u"Widget")
        window.resize(1080, 720)
        window.setWindowTitle("Network Scanner")
        window.setStyleSheet(f'background-color: {theme.backgroundColor};')


        self.layout = QVBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Tạo appbar
        self.app_bar = QWidget()
        self.app_bar_layout = QHBoxLayout()
        self.app_bar_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.back_arrow_icon = QIcon(icon.back_arrow)
        self.back_button = CusToolButton(self.back_arrow_icon, "<==")
        self.back_button.setIcon(self.back_arrow_icon)

        self.title = CusTitleLabel(f"Ping")

        self.refresh = CusButton("Refresh")
        self.refresh.clicked.connect(lambda: self.display_ping_chart())

        self.app_bar_layout.addWidget(self.back_button)
        self.app_bar_layout.addStretch(1)
        self.app_bar_layout.addWidget(self.title)
        self.app_bar_layout.addStretch(1)
        self.app_bar_layout.addWidget(self.refresh)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.content_box = QWidget()
        self.content_box_layout = QVBoxLayout()

        self.ip_input = CusTextInput()
        self.target_host_box = PingItemElement(CustomIcon.desktop_icon, "Target host", self.ip_input.text())
        self.average_ping_box = PingItemElement(CustomIcon.trend_up_icon, "Average ping")
        self.minimum_ping_box = PingItemElement(CustomIcon.arrow_down, "Minimum ping")
        self.maximum_ping_box = PingItemElement(CustomIcon.arrow_up, "Maximum ping")
        self.packet_lost_box = PingItemElement(CustomIcon.cancel, "Packet lost")
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setFixedHeight(400)

        # Create a chart and set its title
        self.chart = QtCharts.QChart()
        # Create a line self.series
        self.series = QtCharts.QLineSeries()

        self.display_ping_chart()

        # Add the self.series to the chart
        self.chart.addSeries(self.series)

        # Set the axis for the chart
        self.axis_x = QtCharts.QValueAxis()
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setLabelFormat("%.2f ms")

        self.chart.addAxis(self.axis_x, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(self.axis_y, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)
        self.chart.legend().setVisible(False)
        self.axis_x.hide()

        # Set the chart on the chart view
        self.chart_view.setChart(self.chart)

        # Add the chart view to the layout
        self.app_bar.setLayout(self.app_bar_layout)

        self.content_box.setLayout(self.content_box_layout)
        self.content_box_layout.addWidget(self.ip_input)
        self.content_box_layout.addWidget(self.target_host_box)
        self.content_box_layout.addWidget(self.average_ping_box)
        self.content_box_layout.addWidget(self.minimum_ping_box)
        self.content_box_layout.addWidget(self.maximum_ping_box)
        self.content_box_layout.addWidget(self.packet_lost_box)
        self.content_box_layout.addWidget(self.chart_view)

        self.scroll_area.setWidget(self.content_box)

        self.layout.addWidget(self.app_bar)
        self.layout.addWidget(self.scroll_area)

        window.setLayout(self.layout)

    # def display_ping_chart(self):
    #
    #     self.series.clear()
    #
    #     maximum_ping = 0.0
    #     minimum_ping = 0.0
    #     average = 0.0
    #     sum = 0.0
    #     packet_lost = 0
    #     counter = 0
    #
    #     for i in range(10):
    #         data = ping_to_device(self.ip_input.text())
    #
    #         if data:
    #             counter += 1
    #             sum += data[2]
    #             if minimum_ping == 0.0: minimum_ping = data[2]
    #             if data[2] >= maximum_ping: maximum_ping = data[2]
    #             if data[2] <= minimum_ping: minimum_ping = data[2]
    #             average = sum/counter
    #
    #             self.maximum_ping_box.setValue(f'{maximum_ping:.2f} ms')
    #             self.minimum_ping_box.setValue(f'{minimum_ping:.2f} ms')
    #             self.average_ping_box.setValue(f'{average:.2f} ms')
    #
    #             # self.axis_y.setRange(minimum_ping, maximum_ping)
    #
    #             self.series.append(i, data[2])
    #
    #             self.chart_view.repaint()
    #             time.sleep(0.5)
    #         else:
    #             break
    #
    #         self.packet_lost_box.setValue(f'{packet_lost / 1 * 100} %')
