import sys

from PySide6.QtWidgets import QApplication

from screens.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    widget.show()
    app.exec()
