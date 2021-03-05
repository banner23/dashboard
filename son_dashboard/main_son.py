import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import *

from alt_iconlu_gosterge import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.verticalSlider.valueChanged.connect(self._trigger_refresh)
        self.ui.verticalSlider_2.valueChanged.connect(self.hiz_refresh)

        self.show()

    def hiz_refresh(self):
        value = self.ui.verticalSlider_2.value()
        progress = (100 - value) / 100
        print(str(progress))
        print("value: "+str(value))

        styleSheetProgress = """ 
            QFrame{ 
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:242.2, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgba(64, 249, 243, 255));\n
                border-radius: 125px;
            }
        """
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        basdeger = 0
        azaltma = 0.0
        bas = 0

        hizGosterge = value*((bas-(value-basdeger)*azaltma))
        print(bas - (value - basdeger)*azaltma)

        hizGosterge = value * 1.44

        newStyleSheet = styleSheetProgress.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        hizGosterge = int(hizGosterge)
        self.ui.hLabel.setText(str(hizGosterge))
        self.ui.hizProgress.setStyleSheet(newStyleSheet)

    def _trigger_refresh(self):
        deger = self.ui.verticalSlider.value()
        progress = (100 - deger) / 100.0
        print(str(progress))
        print("value: "+str(deger))

        if deger < 8:
            bas = 50
            azaltma = 0
            basdeger = 0
        elif deger >= 8 and deger < 18:
            bas = 62.5
            azaltma = 0.411
            basdeger = 8
        elif deger >= 18 and deger < 31:
            bas = 58.8
            azaltma = 0.6769
            basdeger = 18
        elif deger >= 31 and deger < 43:
            bas = 50
            azaltma = 0.2
            basdeger = 31
        elif deger >= 43 and deger < 56:
            bas = 47.6
            azaltma = 0.1692
            basdeger = 43
        elif deger >= 56 and deger < 68:
            bas = 45.4
            azaltma = 0.05833
            basdeger = 56
        elif deger >= 68 and deger < 77:
            bas = 44.7
            azaltma = -0.0777
            basdeger = 68
        elif deger >= 77 and deger < 86:
            bas = 45.4
            azaltma = -0.275
            basdeger = 77

        deger1 = deger*((bas-(deger-basdeger)*azaltma)) + \
            (deger-basdeger) * 0.02
        print(bas - (deger - basdeger)*azaltma)


        styleSheetProgress = """ 
            QFrame{ 
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:242.2, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgba(64, 249, 243, 255));\n
                border-radius: 125px;
            }
        """
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStyleSheet1 = styleSheetProgress.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        deger1 = int(deger1)
        self.ui.dLabel.setText(str(deger1+1))

        self.ui.devirProgress.setStyleSheet(newStyleSheet1)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
