from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QTextEdit, QPushButton, QSizePolicy,
    QToolButton, QWidget, QVBoxLayout, QHBoxLayout)
class Ui_Widget(object):
    def setupUI(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"App")
        Widget.resize(1080, 720)
        Widget.setWindowTitle("Network Scanner")
        self.layout = QVBoxLayout()
        
