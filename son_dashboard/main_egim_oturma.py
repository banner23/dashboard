import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import *


from ui_oturma_egim import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.horizontalSliderDikey.valueChanged.connect(self.dikey_egim)

        labelCizgi0 = QLabel(self.ui.egimAnaFrame)
        labelCizgi0.move(500, 348)
        labelCizgi0.resize(25, 12)
        labelCizgi0.setScaledContents(True)
        labelCizgi0.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi0 = QPixmap("aa.png")
        xformCizgi0 = QTransform()
        xformCizgi0.rotate(105)
        xformed_pixmapCizgi0 = pixmapCizgi0.transformed(
            xformCizgi0, Qt.SmoothTransformation)
        labelCizgi0.setPixmap(xformed_pixmapCizgi0)

        labelCizgi5 = QLabel(self.ui.egimAnaFrame)
        labelCizgi5.move(480, 400)
        labelCizgi5.resize(25, 18)
        labelCizgi5.setScaledContents(True)
        labelCizgi5.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi5 = QPixmap("aa.png")
        xformCizgi5 = QTransform()
        xformCizgi5.rotate(130)
        xformed_pixmapCizgi5 = pixmapCizgi5.transformed(xformCizgi5)
        labelCizgi5.setPixmap(xformed_pixmapCizgi5)

        self.show()

    def dikey_egim(self):
        value = self.ui.horizontalSliderDikey.value()
        egim = (100-value) /100
        print(str(value)+" egim: "+str(egim))

        styleSheet = """
            QFrame{
                background-color: qconicalgradient(cx:0, cy:0, angle:0, stop:{STOP_1} rgba(85, 170, 255, 0), stop:{STOP_2} rgba(252, 201, 109, 255));
                border-bottom-right-radius: 230px;
            }
        """

        stop_1 = str(egim - 0.001)
        stop_2 = str(egim)

        basdeger = 0
        azaltma = 0.0
        bas = 0

        hizGosterge = value * 1.44

        newStyleSheet = styleSheet.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        hizGosterge = int(hizGosterge)
        self.ui.sagaltProgress.setStyleSheet(newStyleSheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

