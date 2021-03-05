import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import *

from ui_stack_dashboard import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.ui.verticalSlider_5.valueChanged.connect(self._trigger_refresh)
        self.ui.verticalSlider_6.valueChanged.connect(self.hiz_refresh)
        self.ui.verticalSliderYarim_3.valueChanged.connect(
            self.aku_yakit_refresh)
        self.ui.verticalSliderYarim_3.valueChanged.connect(
            self.yag_hararet_refresh)
        self.ui.pushButtonSag.clicked.connect(self.sayfaDegis)
        self.ui.pushButtonGeri.clicked.connect(self.sayfaDegis2)

        self.ui.sliderSolUst.valueChanged.connect(self.yanal_egim_sol)
        self.ui.sliderSolAlt.valueChanged.connect(self.dikey_egim_sol)
        self.ui.sliderSagUst.valueChanged.connect(self.yanal_egim_sag)
        self.ui.sliderSagAlt.valueChanged.connect(self.dikey_egim_sag)

    ####### EGİM GOSTERGE ÇİZGİLERİ #########
        labelCizgiSolU10 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolU10.move(80, 240)
        labelCizgiSolU10.resize(25, 14)
        labelCizgiSolU10.setScaledContents(True)
        labelCizgiSolU10.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi10 = QPixmap("aa.png")
        xformCizgi10 = QTransform()
        xformCizgi10.rotate(115)
        xformed_pixmapCizgi10 = pixmapCizgi10.transformed(
            xformCizgi10, Qt.SmoothTransformation)
        labelCizgiSolU10.setPixmap(xformed_pixmapCizgi10)

        labelCizgiSolU20 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolU20.move(135, 147)
        labelCizgiSolU20.resize(25, 15)
        labelCizgiSolU20.setScaledContents(True)
        labelCizgiSolU20.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi20 = QPixmap("aa.png")
        xformCizgi20 = QTransform()
        xformCizgi20.rotate(137)
        xformed_pixmapCizgi20 = pixmapCizgi20.transformed(
            xformCizgi20, Qt.SmoothTransformation)
        labelCizgiSolU20.setPixmap(xformed_pixmapCizgi20)

        labelCizgiSolU30 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolU30.move(225, 85)
        labelCizgiSolU30.resize(14, 22)
        labelCizgiSolU30.setScaledContents(True)
        labelCizgiSolU30.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi30 = QPixmap("aa.png")
        xformCizgi30 = QTransform()
        xformCizgi30.rotate(155)
        xformed_pixmapCizgi30 = pixmapCizgi30.transformed(xformCizgi30)
        labelCizgiSolU30.setPixmap(xformed_pixmapCizgi30)

        labelCizgiSolU40 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolU40.move(320, 62)
        labelCizgiSolU40.resize(12, 30)
        labelCizgiSolU40.setScaledContents(True)
        labelCizgiSolU40.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi40 = QPixmap("E:\QT Çalışmaları\son_dashboard\hjd.png")
        xformCizgi40 = QTransform()
        xformCizgi40.rotate(0)
        xformed_pixmapCizgi40 = pixmapCizgi40.transformed(xformCizgi40)
        labelCizgiSolU40.setPixmap(xformed_pixmapCizgi40)

        labelCizgiSagA10 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA10.move(605, 420)
        labelCizgiSagA10.resize(25, 14)
        labelCizgiSagA10.setScaledContents(True)
        labelCizgiSagA10.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi10 = QPixmap("aa.png")
        xformCizgi10 = QTransform()
        xformCizgi10.rotate(115)
        xformed_pixmapCizgi10 = pixmapCizgi10.transformed(
            xformCizgi10, Qt.SmoothTransformation)
        labelCizgiSagA10.setPixmap(xformed_pixmapCizgi10)

        labelCizgiSagA20 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA20.move(583, 470)
        labelCizgiSagA20.resize(25, 15)
        labelCizgiSagA20.setScaledContents(True)
        labelCizgiSagA20.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi20 = QPixmap("aa.png")
        xformCizgi20 = QTransform()
        xformCizgi20.rotate(125)
        xformed_pixmapCizgi20 = pixmapCizgi20.transformed(xformCizgi20)
        labelCizgiSagA20.setPixmap(xformed_pixmapCizgi20)

        labelCizgiSagA30 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA30.move(552, 520)
        labelCizgiSagA30.resize(24, 16)
        labelCizgiSagA30.setScaledContents(True)
        labelCizgiSagA30.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi30 = QPixmap("aa.png")
        xformCizgi30 = QTransform()
        xformCizgi30.rotate(135)
        xformed_pixmapCizgi30 = pixmapCizgi30.transformed(xformCizgi30)
        labelCizgiSagA30.setPixmap(xformed_pixmapCizgi30)

        labelCizgiSagA40 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA40.move(515, 550)
        labelCizgiSagA40.resize(18, 25)
        labelCizgiSagA40.setScaledContents(True)
        labelCizgiSagA40.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi40 = QPixmap("aa.png")
        xformCizgi40 = QTransform()
        xformCizgi40.rotate(140)
        xformed_pixmapCizgi40 = pixmapCizgi40.transformed(xformCizgi40)
        labelCizgiSagA40.setPixmap(xformed_pixmapCizgi40)

        labelCizgiSagA50 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA50.move(460, 590)
        labelCizgiSagA50.resize(15, 25)
        labelCizgiSagA50.setScaledContents(True)
        labelCizgiSagA50.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi50 = QPixmap("aa.png")
        xformCizgi50 = QTransform()
        xformCizgi50.rotate(155)
        xformed_pixmapCizgi50 = pixmapCizgi50.transformed(xformCizgi50)
        labelCizgiSagA50.setPixmap(xformed_pixmapCizgi50)

        labelCizgiSagA60 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA60.move(380, 600)
        labelCizgiSagA60.resize(12, 30)
        labelCizgiSagA60.setScaledContents(True)
        labelCizgiSagA60.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi60 = QPixmap("E:\QT Çalışmaları\son_dashboard\hjd.png")
        xformCizgi60 = QTransform()
        xformCizgi60.rotate(0)
        xformed_pixmapCizgi60 = pixmapCizgi60.transformed(xformCizgi60)
        labelCizgiSagA60.setPixmap(xformed_pixmapCizgi60)

        labelCizgiSolA10 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolA10.move(75, 410)
        labelCizgiSolA10.resize(24, 16)
        labelCizgiSolA10.setScaledContents(True)
        labelCizgiSolA10.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi10 = QPixmap("aa.png")
        xformCizgi10 = QTransform()
        xformCizgi10.rotate(60)
        xformed_pixmapCizgi10 = pixmapCizgi10.transformed(xformCizgi10)
        labelCizgiSolA10.setPixmap(xformed_pixmapCizgi10)

        labelCizgiSolA20 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolA20.move(95, 472)
        labelCizgiSolA20.resize(24, 16)
        labelCizgiSolA20.setScaledContents(True)
        labelCizgiSolA20.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi20 = QPixmap("aa.png")
        xformCizgi20 = QTransform()
        xformCizgi20.rotate(50)
        xformed_pixmapCizgi20 = pixmapCizgi20.transformed(xformCizgi20)
        labelCizgiSolA20.setPixmap(xformed_pixmapCizgi20)

        labelCizgiSolA30 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolA30.move(140, 525)
        labelCizgiSolA30.resize(24, 16)
        labelCizgiSolA30.setScaledContents(True)
        labelCizgiSolA30.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi30 = QPixmap("aa.png")
        xformCizgi30 = QTransform()
        xformCizgi30.rotate(40)
        xformed_pixmapCizgi30 = pixmapCizgi30.transformed(xformCizgi30)
        labelCizgiSolA30.setPixmap(xformed_pixmapCizgi30)

        labelCizgiSolA40 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolA40.move(192, 565)
        labelCizgiSolA40.resize(18, 25)
        labelCizgiSolA40.setScaledContents(True)
        labelCizgiSolA40.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi40 = QPixmap("aa.png")
        xformCizgi40 = QTransform()
        xformCizgi40.rotate(35)
        xformed_pixmapCizgi40 = pixmapCizgi40.transformed(xformCizgi40)
        labelCizgiSolA40.setPixmap(xformed_pixmapCizgi40)

        labelCizgiSolA50 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolA50.move(255, 590)
        labelCizgiSolA50.resize(14, 25)
        labelCizgiSolA50.setScaledContents(True)
        labelCizgiSolA50.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi50 = QPixmap("aa.png")
        xformCizgi50 = QTransform()
        xformCizgi50.rotate(15)
        xformed_pixmapCizgi50 = pixmapCizgi50.transformed(xformCizgi50)
        labelCizgiSolA50.setPixmap(xformed_pixmapCizgi50)

        labelCizgiSolA60 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSolA60.move(320, 600)
        labelCizgiSolA60.resize(12, 30)
        labelCizgiSolA60.setScaledContents(True)
        labelCizgiSolA60.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi60 = QPixmap("E:\QT Çalışmaları\son_dashboard\hjd.png")
        xformCizgi60 = QTransform()
        xformCizgi60.rotate(0)
        xformed_pixmapCizgi60 = pixmapCizgi60.transformed(xformCizgi60)
        labelCizgiSolA60.setPixmap(xformed_pixmapCizgi60)

        labelCizgiSagU10 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagU10.move(587, 242)
        labelCizgiSagU10.resize(26, 12)
        labelCizgiSagU10.setScaledContents(True)
        labelCizgiSagU10.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi10 = QPixmap("aa.png")
        xformCizgi10 = QTransform()
        xformCizgi10.rotate(70)
        xformed_pixmapCizgi10 = pixmapCizgi10.transformed(
            xformCizgi10, Qt.SmoothTransformation)
        labelCizgiSagU10.setPixmap(xformed_pixmapCizgi10)

        labelCizgiSagU20 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagU20.move(532, 147)
        labelCizgiSagU20.resize(30, 17)
        labelCizgiSagU20.setScaledContents(True)
        labelCizgiSagU20.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi20 = QPixmap("aa.png")
        xformCizgi20 = QTransform()
        xformCizgi20.rotate(40)
        xformed_pixmapCizgi20 = pixmapCizgi20.transformed(xformCizgi20)
        labelCizgiSagU20.setPixmap(xformed_pixmapCizgi20)

        labelCizgiSagU30 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagU30.move(455, 90)
        labelCizgiSagU30.resize(14, 24)
        labelCizgiSagU30.setScaledContents(True)
        labelCizgiSagU30.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi30 = QPixmap("aa.png")
        xformCizgi30 = QTransform()
        xformCizgi30.rotate(15)
        xformed_pixmapCizgi30 = pixmapCizgi30.transformed(xformCizgi30)
        labelCizgiSagU30.setPixmap(xformed_pixmapCizgi30)

        labelCizgiSagU40 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagU40.move(365, 62)
        labelCizgiSagU40.resize(12, 30)
        labelCizgiSagU40.setScaledContents(True)
        labelCizgiSagU40.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi40 = QPixmap("E:\QT Çalışmaları\son_dashboard\hjd.png")
        xformCizgi40 = QTransform()
        xformCizgi40.rotate(0)
        xformed_pixmapCizgi40 = pixmapCizgi40.transformed(xformCizgi40)
        labelCizgiSagU40.setPixmap(xformed_pixmapCizgi40)
    
    ####### EGİM GOSTERGE ÇİZGİLERİ END #########

    #RPM GOSTERGE START
        labelCizgi0 = QLabel(self.ui.rpmFrame_3)
        labelCizgi0.move(160, 380)
        labelCizgi0.resize(22, 31)
        labelCizgi0.setScaledContents(True)
        labelCizgi0.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi0 = QPixmap("aa.png")
        xformCizgi0 = QTransform()
        xformCizgi0.rotate(30)
        xformed_pixmapCizgi0 = pixmapCizgi0.transformed(
            xformCizgi0, Qt.SmoothTransformation)
        labelCizgi0.setPixmap(xformed_pixmapCizgi0)

        labelCizgi5 = QLabel(self.ui.rpmFrame_3)
        labelCizgi5.move(100, 330)
        labelCizgi5.resize(25, 18)
        labelCizgi5.setScaledContents(True)
        labelCizgi5.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi5 = QPixmap("aa.png")
        xformCizgi5 = QTransform()
        xformCizgi5.rotate(52)
        xformed_pixmapCizgi5 = pixmapCizgi5.transformed(xformCizgi5)
        labelCizgi5.setPixmap(xformed_pixmapCizgi5)

        labelCizgi10 = QLabel(self.ui.rpmFrame_3)
        labelCizgi10.move(70, 245)
        labelCizgi10.resize(29, 10)
        labelCizgi10.setScaledContents(True)
        labelCizgi10.setStyleSheet("QLabel{ background-color: none;}")
        pixmap10 = QPixmap("aa.png")
        xform10 = QTransform()
        xform10.rotate(-91)
        xformed_pixmap10 = pixmap10.transformed(xform10)
        labelCizgi10.setPixmap(xformed_pixmap10)

        labelCizgi15 = QLabel(self.ui.rpmFrame_3)
        labelCizgi15.move(125, 115)
        labelCizgi15.resize(23, 22)
        labelCizgi15.setScaledContents(True)
        labelCizgi15.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi15 = QPixmap("aa.png")
        xformCizgi15 = QTransform()
        xformCizgi15.rotate(-38)
        xformed_pixmapCizgi15 = pixmapCizgi15.transformed(
            xformCizgi15, Qt.SmoothTransformation)
        labelCizgi15.setPixmap(xformed_pixmapCizgi15)

        labelCizgi20 = QLabel(self.ui.rpmFrame_3)
        labelCizgi20.move(243, 70)
        labelCizgi20.resize(8, 27)
        labelCizgi20.setScaledContents(True)
        labelCizgi20.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi20 = QPixmap("aa.png")
        xformCizgi20 = QTransform()
        xformed_pixmapCizgi20 = pixmapCizgi20.transformed(
            xformCizgi20, Qt.SmoothTransformation)
        labelCizgi20.setPixmap(xformed_pixmapCizgi20)

        labelCizgi25 = QLabel(self.ui.rpmFrame_3)
        labelCizgi25.move(365, 120)
        labelCizgi25.resize(22, 23)
        labelCizgi25.setScaledContents(True)
        labelCizgi25.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi25 = QPixmap("aa.png")
        xformCizgi25 = QTransform()
        xformCizgi25.rotate(38)
        xformed_pixmapCizgi25 = pixmapCizgi25.transformed(
            xformCizgi25, Qt.SmoothTransformation)
        labelCizgi25.setPixmap(xformed_pixmapCizgi25)

        labelCizgi30 = QLabel(self.ui.rpmFrame_3)
        labelCizgi30.move(400, 245)
        labelCizgi30.resize(29, 10)
        labelCizgi30.setScaledContents(True)
        labelCizgi30.setStyleSheet("QLabel{ background-color: none;}")
        pixmap30 = QPixmap("aa.png")
        xform30 = QTransform()
        xform30.rotate(90)
        xformed_pixmap30 = pixmap30.transformed(xform30)
        labelCizgi30.setPixmap(xformed_pixmap30)

        labelCizgi35 = QLabel(self.ui.rpmFrame_3)
        labelCizgi35.move(375, 337)
        labelCizgi35.resize(25, 21)
        labelCizgi35.setScaledContents(True)
        labelCizgi35.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi35 = QPixmap("aa.png")
        xformCizgi35 = QTransform()
        xformCizgi35.rotate(138)
        xformed_pixmapCizgi35 = pixmapCizgi35.transformed(xformCizgi35)
        labelCizgi35.setPixmap(xformed_pixmapCizgi35)

        labelCizgi40 = QLabel(self.ui.rpmFrame_3)
        labelCizgi40.move(320, 380)
        labelCizgi40.resize(25, 30)
        labelCizgi40.setScaledContents(True)
        labelCizgi40.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi40 = QPixmap("aa.png")
        xformCizgi40 = QTransform()
        xformCizgi40.rotate(-30)
        xformed_pixmapCizgi40 = pixmapCizgi40.transformed(
            xformCizgi40, Qt.SmoothTransformation)
        labelCizgi40.setPixmap(xformed_pixmapCizgi40)
    #RPM GOSTERGE END

    #HIZ GOSTERGE START
        labelCizgi00 = QLabel(self.ui.hizFrame_3)
        labelCizgi00.move(160, 380)
        labelCizgi00.resize(22, 31)
        labelCizgi00.setScaledContents(True)
        labelCizgi00.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi00 = QPixmap("aa.png")
        xformCizgi00 = QTransform()
        xformCizgi00.rotate(30)
        xformed_pixmapCizgi00 = pixmapCizgi00.transformed(
            xformCizgi00, Qt.SmoothTransformation)
        labelCizgi00.setPixmap(xformed_pixmapCizgi00)

        labelCizgi05 = QLabel(self.ui.hizFrame_3)
        labelCizgi05.move(130, 368)
        labelCizgi05.resize(15, 13)
        labelCizgi05.setScaledContents(True)
        labelCizgi05.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi05 = QPixmap("aa.png")
        xformCizgi05 = QTransform()
        xformCizgi05.rotate(40)
        xformed_pixmapCizgi05 = pixmapCizgi05.transformed(
            xformCizgi05, Qt.SmoothTransformation)
        labelCizgi05.setPixmap(xformed_pixmapCizgi05)

        labelCizgi1010 = QLabel(self.ui.hizFrame_3)
        labelCizgi1010.move(102, 333)
        labelCizgi1010.resize(28, 25)
        labelCizgi1010.setScaledContents(True)
        labelCizgi1010.setStyleSheet("QLabel{ background-color: none;}")
        pixmap1010 = QPixmap("aa.png")
        xform1010 = QTransform()
        xform1010.rotate(50)
        xformed_pixmap1010 = pixmap1010.transformed(xform1010)
        labelCizgi1010.setPixmap(xformed_pixmap1010)

        labelCizgi1515 = QLabel(self.ui.hizFrame_3)
        labelCizgi1515.move(90, 310)
        labelCizgi1515.resize(17, 10)
        labelCizgi1515.setScaledContents(True)
        labelCizgi1515.setStyleSheet("QLabel{ background-color: none;}")
        pixmap1515 = QPixmap("aa.png")
        xform1515 = QTransform()
        xform1515.rotate(-115)
        xformed_pixmap1515 = pixmap1515.transformed(xform1515)
        labelCizgi1515.setPixmap(xformed_pixmap1515)

        labelCizgi2020 = QLabel(self.ui.hizFrame_3)
        labelCizgi2020.move(75, 275)
        labelCizgi2020.resize(30, 15)
        labelCizgi2020.setScaledContents(True)
        labelCizgi2020.setStyleSheet("QLabel{ background-color: none;}")
        pixmap2020 = QPixmap("aa.png")
        xform2020 = QTransform()
        xform2020.rotate(76)
        xformed_pixmap2020 = pixmap2020.transformed(xform2020)
        labelCizgi2020.setPixmap(xformed_pixmap2020)

        labelCizgi2525 = QLabel(self.ui.hizFrame_3)
        labelCizgi2525.move(75, 242)
        labelCizgi2525.resize(15, 5)
        labelCizgi2525.setScaledContents(True)
        labelCizgi2525.setStyleSheet("QLabel{ background-color: none;}")
        pixmap2525 = QPixmap("aa.png")
        xform2525 = QTransform()
        xform2525.rotate(-90)
        xformed_pixmap2525 = pixmap2525.transformed(xform2525)
        labelCizgi2525.setPixmap(xformed_pixmap2525)

        labelCizgi3030 = QLabel(self.ui.hizFrame_3)
        labelCizgi3030.move(75, 198)
        labelCizgi3030.resize(30, 20)
        labelCizgi3030.setScaledContents(True)
        labelCizgi3030.setStyleSheet("QLabel{ background-color: none;}")
        pixmap3030 = QPixmap("aa.png")
        xform3030 = QTransform()
        xform3030.rotate(-65)
        xformed_pixmap3030 = pixmap3030.transformed(xform3030)
        labelCizgi3030.setPixmap(xformed_pixmap3030)

        labelCizgi3535 = QLabel(self.ui.hizFrame_3)
        labelCizgi3535.move(95, 168)
        labelCizgi3535.resize(15, 11)
        labelCizgi3535.setScaledContents(True)
        labelCizgi3535.setStyleSheet("QLabel{ background-color: none;}")
        pixmap3535 = QPixmap("aa.png")
        xform3535 = QTransform()
        xform3535.rotate(-60)
        xformed_pixmap3535 = pixmap3535.transformed(xform3535)
        labelCizgi3535.setPixmap(xformed_pixmap3535)

        labelCizgi4040 = QLabel(self.ui.hizFrame_3)
        labelCizgi4040.move(108, 130)
        labelCizgi4040.resize(27, 28)
        labelCizgi4040.setScaledContents(True)
        labelCizgi4040.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi4040 = QPixmap("aa.png")
        xformCizgi4040 = QTransform()
        xformCizgi4040.rotate(-48)
        xformed_pixmapCizgi4040 = pixmapCizgi4040.transformed(
            xformCizgi4040, Qt.SmoothTransformation)
        labelCizgi4040.setPixmap(xformed_pixmapCizgi4040)

        labelCizgi4545 = QLabel(self.ui.hizFrame_3)
        labelCizgi4545.move(135, 110)
        labelCizgi4545.resize(15, 14)
        labelCizgi4545.setScaledContents(True)
        labelCizgi4545.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi4545 = QPixmap("aa.png")
        xformCizgi4545 = QTransform()
        xformCizgi4545.rotate(-40)
        xformed_pixmapCizgi4545 = pixmapCizgi4545.transformed(
            xformCizgi4545, Qt.SmoothTransformation)
        labelCizgi4545.setPixmap(xformed_pixmapCizgi4545)

        labelCizgi5050 = QLabel(self.ui.hizFrame_3)
        labelCizgi5050.move(170, 85)
        labelCizgi5050.resize(20, 28)
        labelCizgi5050.setScaledContents(True)
        labelCizgi5050.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi5050 = QPixmap("aa.png")
        xformCizgi5050 = QTransform()
        xformCizgi5050.rotate(-20)
        xformed_pixmapCizgi5050 = pixmapCizgi5050.transformed(
            xformCizgi5050, Qt.SmoothTransformation)
        labelCizgi5050.setPixmap(xformed_pixmapCizgi5050)

        labelCizgi5555 = QLabel(self.ui.hizFrame_3)
        labelCizgi5555.move(210, 78)
        labelCizgi5555.resize(8, 16)
        labelCizgi5555.setScaledContents(True)
        labelCizgi5555.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi5555 = QPixmap("aa.png")
        xformCizgi5555 = QTransform()
        xformCizgi5555.rotate(-10)
        xformed_pixmapCizgi5555 = pixmapCizgi5555.transformed(
            xformCizgi5555, Qt.SmoothTransformation)
        labelCizgi5555.setPixmap(xformed_pixmapCizgi5555)

        labelCizgi6060 = QLabel(self.ui.hizFrame_3)
        labelCizgi6060.move(240, 70)
        labelCizgi6060.resize(11, 27)
        labelCizgi6060.setScaledContents(True)
        labelCizgi6060.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi6060 = QPixmap("aa.png")
        xformCizgi6060 = QTransform()
        xformCizgi6060.rotate(-2)
        xformed_pixmapCizgi6060 = pixmapCizgi6060.transformed(
            xformCizgi6060, Qt.SmoothTransformation)
        labelCizgi6060.setPixmap(xformed_pixmapCizgi6060)

        labelCizgi6565 = QLabel(self.ui.hizFrame_3)
        labelCizgi6565.move(282, 78)
        labelCizgi6565.resize(7, 15)
        labelCizgi6565.setScaledContents(True)
        labelCizgi6565.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi6565 = QPixmap("aa.png")
        xformCizgi6565 = QTransform()
        xformCizgi6565.rotate(8)
        xformed_pixmapCizgi6565 = pixmapCizgi6565.transformed(
            xformCizgi6565, Qt.SmoothTransformation)
        labelCizgi6565.setPixmap(xformed_pixmapCizgi6565)

        labelCizgi7070 = QLabel(self.ui.hizFrame_3)
        labelCizgi7070.move(308, 85)
        labelCizgi7070.resize(22, 28)
        labelCizgi7070.setScaledContents(True)
        labelCizgi7070.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi7070 = QPixmap("aa.png")
        xformCizgi7070 = QTransform()
        xformCizgi7070.rotate(30)
        xformed_pixmapCizgi7070 = pixmapCizgi7070.transformed(
            xformCizgi7070, Qt.SmoothTransformation)
        labelCizgi7070.setPixmap(xformed_pixmapCizgi7070)

        labelCizgi7575 = QLabel(self.ui.hizFrame_3)
        labelCizgi7575.move(345, 110)
        labelCizgi7575.resize(12, 15)
        labelCizgi7575.setScaledContents(True)
        labelCizgi7575.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi7575 = QPixmap("aa.png")
        xformCizgi7575 = QTransform()
        xformCizgi7575.rotate(40)
        xformed_pixmapCizgi7575 = pixmapCizgi7575.transformed(
            xformCizgi7575, Qt.SmoothTransformation)
        labelCizgi7575.setPixmap(xformed_pixmapCizgi7575)

        labelCizgi8080 = QLabel(self.ui.hizFrame_3)
        labelCizgi8080.move(365, 125)
        labelCizgi8080.resize(25, 28)
        labelCizgi8080.setScaledContents(True)
        labelCizgi8080.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi8080 = QPixmap("aa.png")
        xformCizgi8080 = QTransform()
        xformCizgi8080.rotate(38)
        xformed_pixmapCizgi8080 = pixmapCizgi8080.transformed(
            xformCizgi8080, Qt.SmoothTransformation)
        labelCizgi8080.setPixmap(xformed_pixmapCizgi8080)

        labelCizgi8585 = QLabel(self.ui.hizFrame_3)
        labelCizgi8585.move(390, 163)
        labelCizgi8585.resize(15, 12)
        labelCizgi8585.setScaledContents(True)
        labelCizgi8585.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi8585 = QPixmap("aa.png")
        xformCizgi8585 = QTransform()
        xformCizgi8585.rotate(60)
        xformed_pixmapCizgi8585 = pixmapCizgi8585.transformed(
            xformCizgi8585, Qt.SmoothTransformation)
        labelCizgi8585.setPixmap(xformed_pixmapCizgi8585)

        labelCizgi9090 = QLabel(self.ui.hizFrame_3)
        labelCizgi9090.move(400, 195)
        labelCizgi9090.resize(29, 16)
        labelCizgi9090.setScaledContents(True)
        labelCizgi9090.setStyleSheet("QLabel{ background-color: none;}")
        pixmap9090 = QPixmap("aa.png")
        xform9090 = QTransform()
        xform9090.rotate(-15)
        xform9090.rotate(9090)
        xformed_pixmap9090 = pixmap9090.transformed(xform9090)
        labelCizgi9090.setPixmap(xformed_pixmap9090)

        labelCizgi9595 = QLabel(self.ui.hizFrame_3)
        labelCizgi9595.move(407, 235)
        labelCizgi9595.resize(17, 6)
        labelCizgi9595.setScaledContents(True)
        labelCizgi9595.setStyleSheet("QLabel{ background-color: none;}")
        pixmap9595 = QPixmap("aa.png")
        xform9595 = QTransform()
        xform9595.rotate(30)
        xform9595.rotate(9595)
        xformed_pixmap9595 = pixmap9595.transformed(xform9595)
        labelCizgi9595.setPixmap(xformed_pixmap9595)

        labelCizgi100 = QLabel(self.ui.hizFrame_3)
        labelCizgi100.move(400, 275)
        labelCizgi100.resize(29, 15)
        labelCizgi100.setScaledContents(True)
        labelCizgi100.setStyleSheet("QLabel{ background-color: none;}")
        pixmap100 = QPixmap("aa.png")
        xform100 = QTransform()
        xform100.rotate(100)
        xformed_pixmap100 = pixmap100.transformed(xform100)
        labelCizgi100.setPixmap(xformed_pixmap100)

        labelCizgi105 = QLabel(self.ui.hizFrame_3)
        labelCizgi105.move(400, 308)
        labelCizgi105.resize(17, 10)
        labelCizgi105.setScaledContents(True)
        labelCizgi105.setStyleSheet("QLabel{ background-color: none;}")
        pixmap105 = QPixmap("aa.png")
        xform105 = QTransform()
        xform105.rotate(115)
        xformed_pixmap105 = pixmap105.transformed(xform105)
        labelCizgi105.setPixmap(xformed_pixmap105)

        labelCizgi110 = QLabel(self.ui.hizFrame_3)
        labelCizgi110.move(375, 333)
        labelCizgi110.resize(27, 25)
        labelCizgi110.setScaledContents(True)
        labelCizgi110.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi110 = QPixmap("aa.png")
        xform110 = QTransform()
        xform110.rotate(-55)
        xformed_pixmapCizgi110 = pixmapCizgi110.transformed(
            xform110, Qt.SmoothTransformation)
        labelCizgi110.setPixmap(xformed_pixmapCizgi110)

        labelCizgi115 = QLabel(self.ui.hizFrame_3)
        labelCizgi115.move(358, 367)
        labelCizgi115.resize(14, 12)
        labelCizgi115.setScaledContents(True)
        labelCizgi115.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi115 = QPixmap("aa.png")
        xform115 = QTransform()
        xform115.rotate(-45)
        xformed_pixmapCizgi115 = pixmapCizgi115.transformed(
            xform115, Qt.SmoothTransformation)
        labelCizgi115.setPixmap(xformed_pixmapCizgi115)

        labelCizgi120 = QLabel(self.ui.hizFrame_3)
        labelCizgi120.move(320, 380)
        labelCizgi120.resize(25, 28)
        labelCizgi120.setScaledContents(True)
        labelCizgi120.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi120 = QPixmap("aa.png")
        xform120 = QTransform()
        xform120.rotate(-28)
        xformed_pixmapCizgi120 = pixmapCizgi120.transformed(
            xform120, Qt.SmoothTransformation)
        labelCizgi120.setPixmap(xformed_pixmapCizgi120)
    #HIZ GOSTERGE END

    #AKU GOSTERGE START
        labelCizgiA0 = QLabel(self.ui.akuFrame_3)
        labelCizgiA0.move(30, 105)
        labelCizgiA0.resize(12, 7)
        labelCizgiA0.setScaledContents(True)
        labelCizgiA0.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiA0 = QPixmap("aa.png")
        xformCizgiA0 = QTransform()
        xformCizgiA0.rotate(-70)
        xformed_pixmapCizgiA0 = pixmapCizgiA0.transformed(
            xformCizgiA0, Qt.SmoothTransformation)
        labelCizgiA0.setPixmap(xformed_pixmapCizgiA0)

        labelCizgiA2 = QLabel(self.ui.akuFrame_3)
        labelCizgiA2.move(66, 53)
        labelCizgiA2.resize(10, 13)
        labelCizgiA2.setScaledContents(True)
        labelCizgiA2.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiA2 = QPixmap("aa.png")
        xformCizgiA2 = QTransform()
        xformCizgiA2.rotate(-40)
        xformed_pixmapCizgiA2 = pixmapCizgiA2.transformed(
            xformCizgiA2, Qt.SmoothTransformation)
        labelCizgiA2.setPixmap(xformed_pixmapCizgiA2)

        labelCizgiA4 = QLabel(self.ui.akuFrame_3)
        labelCizgiA4.move(125, 37)
        labelCizgiA4.resize(4, 12)
        labelCizgiA4.setScaledContents(True)
        labelCizgiA4.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiA4 = QPixmap("aa.png")
        xformCizgiA4 = QTransform()
        xformCizgiA4.rotate(0)
        xformed_pixmapCizgiA4 = pixmapCizgiA4.transformed(
            xformCizgiA4, Qt.SmoothTransformation)
        labelCizgiA4.setPixmap(xformed_pixmapCizgiA4)

        labelCizgiA6 = QLabel(self.ui.akuFrame_3)
        labelCizgiA6.move(185, 53)
        labelCizgiA6.resize(8, 12)
        labelCizgiA6.setScaledContents(True)
        labelCizgiA6.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiA6 = QPixmap("aa.png")
        xformCizgiA6 = QTransform()
        xformCizgiA6.rotate(30)
        xformed_pixmapCizgiA6 = pixmapCizgiA6.transformed(
            xformCizgiA6, Qt.SmoothTransformation)
        labelCizgiA6.setPixmap(xformed_pixmapCizgiA6)

        labelCizgiA8 = QLabel(self.ui.akuFrame_3)
        labelCizgiA8.move(215, 105)
        labelCizgiA8.resize(12, 7)
        labelCizgiA8.setScaledContents(True)
        labelCizgiA8.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiA8 = QPixmap("aa.png")
        xformCizgiA8 = QTransform()
        xformCizgiA8.rotate(70)
        xformed_pixmapCizgiA8 = pixmapCizgiA8.transformed(
            xformCizgiA8, Qt.SmoothTransformation)
        labelCizgiA8.setPixmap(xformed_pixmapCizgiA8)
    #AKU GOSTERGE END

    #YAKIT GOSTERGE START
        labelCizgiYT0 = QLabel(self.ui.yakitFrame_3)
        labelCizgiYT0.move(30, 105)
        labelCizgiYT0.resize(12, 7)
        labelCizgiYT0.setScaledContents(True)
        labelCizgiYT0.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiYT0 = QPixmap("aa.png")
        xformCizgiYT0 = QTransform()
        xformCizgiYT0.rotate(-70)
        xformed_pixmapCizgiYT0 = pixmapCizgiYT0.transformed(
            xformCizgiYT0, Qt.SmoothTransformation)
        labelCizgiYT0.setPixmap(xformed_pixmapCizgiYT0)

        labelCizgiYT2 = QLabel(self.ui.yakitFrame_3)
        labelCizgiYT2.move(66, 53)
        labelCizgiYT2.resize(10, 13)
        labelCizgiYT2.setScaledContents(True)
        labelCizgiYT2.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiYT2 = QPixmap("aa.png")
        xformCizgiYT2 = QTransform()
        xformCizgiYT2.rotate(-40)
        xformed_pixmapCizgiYT2 = pixmapCizgiYT2.transformed(
            xformCizgiYT2, Qt.SmoothTransformation)
        labelCizgiYT2.setPixmap(xformed_pixmapCizgiYT2)

        labelCizgiYT4 = QLabel(self.ui.yakitFrame_3)
        labelCizgiYT4.move(125, 37)
        labelCizgiYT4.resize(4, 12)
        labelCizgiYT4.setScaledContents(True)
        labelCizgiYT4.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiYT4 = QPixmap("aa.png")
        xformCizgiYT4 = QTransform()
        xformCizgiYT4.rotate(0)
        xformed_pixmapCizgiYT4 = pixmapCizgiYT4.transformed(
            xformCizgiYT4, Qt.SmoothTransformation)
        labelCizgiYT4.setPixmap(xformed_pixmapCizgiYT4)

        labelCizgiYT6 = QLabel(self.ui.yakitFrame_3)
        labelCizgiYT6.move(185, 53)
        labelCizgiYT6.resize(8, 12)
        labelCizgiYT6.setScaledContents(True)
        labelCizgiYT6.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiYT6 = QPixmap("aa.png")
        xformCizgiYT6 = QTransform()
        xformCizgiYT6.rotate(30)
        xformed_pixmapCizgiYT6 = pixmapCizgiYT6.transformed(
            xformCizgiYT6, Qt.SmoothTransformation)
        labelCizgiYT6.setPixmap(xformed_pixmapCizgiYT6)

        labelCizgiYT8 = QLabel(self.ui.yakitFrame_3)
        labelCizgiYT8.move(215, 105)
        labelCizgiYT8.resize(12, 7)
        labelCizgiYT8.setScaledContents(True)
        labelCizgiYT8.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiYT8 = QPixmap("aa.png")
        xformCizgiYT8 = QTransform()
        xformCizgiYT8.rotate(70)
        xformed_pixmapCizgiYT8 = pixmapCizgiYT8.transformed(
            xformCizgiYT8, Qt.SmoothTransformation)
        labelCizgiYT8.setPixmap(xformed_pixmapCizgiYT8)
    #YAKIT GOSTERGE END

    #HARARET GOSTERGE START
        labelCizgiH0 = QLabel(self.ui.hararetFrame_3)
        labelCizgiH0.move(30, 105)
        labelCizgiH0.resize(12, 7)
        labelCizgiH0.setScaledContents(True)
        labelCizgiH0.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiH0 = QPixmap("aa.png")
        xformCizgiH0 = QTransform()
        xformCizgiH0.rotate(-70)
        xformed_pixmapCizgiH0 = pixmapCizgiH0.transformed(
            xformCizgiH0, Qt.SmoothTransformation)
        labelCizgiH0.setPixmap(xformed_pixmapCizgiH0)

        labelCizgiH2 = QLabel(self.ui.hararetFrame_3)
        labelCizgiH2.move(66, 53)
        labelCizgiH2.resize(10, 13)
        labelCizgiH2.setScaledContents(True)
        labelCizgiH2.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiH2 = QPixmap("aa.png")
        xformCizgiH2 = QTransform()
        xformCizgiH2.rotate(-40)
        xformed_pixmapCizgiH2 = pixmapCizgiH2.transformed(
            xformCizgiH2, Qt.SmoothTransformation)
        labelCizgiH2.setPixmap(xformed_pixmapCizgiH2)

        labelCizgiH4 = QLabel(self.ui.hararetFrame_3)
        labelCizgiH4.move(125, 37)
        labelCizgiH4.resize(4, 12)
        labelCizgiH4.setScaledContents(True)
        labelCizgiH4.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiH4 = QPixmap("aa.png")
        xformCizgiH4 = QTransform()
        xformCizgiH4.rotate(0)
        xformed_pixmapCizgiH4 = pixmapCizgiH4.transformed(
            xformCizgiH4, Qt.SmoothTransformation)
        labelCizgiH4.setPixmap(xformed_pixmapCizgiH4)

        labelCizgiH6 = QLabel(self.ui.hararetFrame_3)
        labelCizgiH6.move(185, 53)
        labelCizgiH6.resize(8, 12)
        labelCizgiH6.setScaledContents(True)
        labelCizgiH6.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiH6 = QPixmap("aa.png")
        xformCizgiH6 = QTransform()
        xformCizgiH6.rotate(30)
        xformed_pixmapCizgiH6 = pixmapCizgiH6.transformed(
            xformCizgiH6, Qt.SmoothTransformation)
        labelCizgiH6.setPixmap(xformed_pixmapCizgiH6)

        labelCizgiH8 = QLabel(self.ui.hararetFrame_3)
        labelCizgiH8.move(215, 105)
        labelCizgiH8.resize(12, 7)
        labelCizgiH8.setScaledContents(True)
        labelCizgiH8.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiH8 = QPixmap("aa.png")
        xformCizgiH8 = QTransform()
        xformCizgiH8.rotate(70)
        xformed_pixmapCizgiH8 = pixmapCizgiH8.transformed(
            xformCizgiH8, Qt.SmoothTransformation)
        labelCizgiH8.setPixmap(xformed_pixmapCizgiH8)
    #HARARET GOSTERGE END

    #YAG GOSTERGE START
        labelCizgiY0 = QLabel(self.ui.yagFrame_3)
        labelCizgiY0.move(30, 105)
        labelCizgiY0.resize(12, 7)
        labelCizgiY0.setScaledContents(True)
        labelCizgiY0.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiY0 = QPixmap("aa.png")
        xformCizgiY0 = QTransform()
        xformCizgiY0.rotate(-70)
        xformed_pixmapCizgiY0 = pixmapCizgiY0.transformed(
            xformCizgiY0, Qt.SmoothTransformation)
        labelCizgiY0.setPixmap(xformed_pixmapCizgiY0)

        labelCizgiY2 = QLabel(self.ui.yagFrame_3)
        labelCizgiY2.move(66, 53)
        labelCizgiY2.resize(10, 13)
        labelCizgiY2.setScaledContents(True)
        labelCizgiY2.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiY2 = QPixmap("aa.png")
        xformCizgiY2 = QTransform()
        xformCizgiY2.rotate(-40)
        xformed_pixmapCizgiY2 = pixmapCizgiY2.transformed(
            xformCizgiY2, Qt.SmoothTransformation)
        labelCizgiY2.setPixmap(xformed_pixmapCizgiY2)

        labelCizgiY4 = QLabel(self.ui.yagFrame_3)
        labelCizgiY4.move(125, 37)
        labelCizgiY4.resize(4, 12)
        labelCizgiY4.setScaledContents(True)
        labelCizgiY4.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiY4 = QPixmap("aa.png")
        xformCizgiY4 = QTransform()
        xformCizgiY4.rotate(0)
        xformed_pixmapCizgiY4 = pixmapCizgiY4.transformed(
            xformCizgiY4, Qt.SmoothTransformation)
        labelCizgiY4.setPixmap(xformed_pixmapCizgiY4)

        labelCizgiY6 = QLabel(self.ui.yagFrame_3)
        labelCizgiY6.move(185, 53)
        labelCizgiY6.resize(8, 12)
        labelCizgiY6.setScaledContents(True)
        labelCizgiY6.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiY6 = QPixmap("aa.png")
        xformCizgiY6 = QTransform()
        xformCizgiY6.rotate(30)
        xformed_pixmapCizgiY6 = pixmapCizgiY6.transformed(
            xformCizgiY6, Qt.SmoothTransformation)
        labelCizgiY6.setPixmap(xformed_pixmapCizgiY6)

        labelCizgiY8 = QLabel(self.ui.yagFrame_3)
        labelCizgiY8.move(215, 105)
        labelCizgiY8.resize(12, 7)
        labelCizgiY8.setScaledContents(True)
        labelCizgiY8.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgiY8 = QPixmap("aa.png")
        xformCizgiY8 = QTransform()
        xformCizgiY8.rotate(70)
        xformed_pixmapCizgiY8 = pixmapCizgiY8.transformed(
            xformCizgiY8, Qt.SmoothTransformation)
        labelCizgiY8.setPixmap(xformed_pixmapCizgiY8)
    #YAG GOSTERGE END

        self.showMaximized()

    def yanal_egim_sol(self):
        value = self.ui.sliderSolUst.value()
        egim = (100-value) / 100
        print(str(value)+" egim: "+str(egim))

        styleSheet = """
            QFrame{
                border-top-left-radius: 275px;
                background-color: qconicalgradient(cx:1, cy:1, angle:180, stop:{STOP_1} rgba(85, 170, 255, 0), stop:{STOP_2} rgba(252, 201, 109, 255));
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
        self.ui.solUstProgress.setStyleSheet(newStyleSheet)
    
    def yanal_egim_sag(self):
        value = self.ui.sliderSagUst.value()
        egim = (value) / 100
        print(str(value)+" egim: "+str(egim))

        styleSheet = """
                QFrame{
        border-top-right-radius: 275px;
        background-color: qconicalgradient(cx:0, cy:1, angle:0, stop:{STOP_1} rgba(252, 201, 109, 255), stop:{STOP_2} rgba(85, 170, 255, 0));
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
        self.ui.sagUstProgress.setStyleSheet(newStyleSheet)

    def dikey_egim_sol(self):
        value = self.ui.sliderSolAlt.value()
        egim = (value) / 100
        print(str(value)+" egim: "+str(egim))

        styleSheet = """
            QFrame{
                border-bottom-left-radius: 275px;\n
                background-color: qconicalgradient(cx:1, cy:0, angle:180, stop:{STOP_1} rgba(121, 50, 190, 255), stop:{STOP_2} rgba(85, 170, 255, 0));\n
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
        self.ui.solAltProgress.setStyleSheet(newStyleSheet)

    def dikey_egim_sag(self):
        value = self.ui.sliderSagAlt.value()
        #egim = value / 100
        egim = (100-value) / 100
        print(str(value)+" egim: "+str(egim))

        styleSheet = """
            QFrame{
                border-bottom-right-radius: 275px;\n
                background-color: qconicalgradient(cx:0, cy:0, angle:0, stop:{STOP_1} rgba(85, 170, 255, 0), stop:{STOP_2} rgba(121, 50, 190, 255));\n

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
        self.ui.sagAltProgress.setStyleSheet(newStyleSheet)


    def sayfaDegis(self):
        currentIndex = self.ui.stackedWidget.currentIndex()
        if currentIndex < self.ui.stackedWidget.count():
            self.ui.stackedWidget.setCurrentIndex(1)

    def sayfaDegis2(self):
        currentIndex = self.ui.stackedWidget.currentIndex()
        if currentIndex < self.ui.stackedWidget.count():
            self.ui.stackedWidget.setCurrentIndex(0)

    def aku_yakit_refresh(self):
        value = self.ui.verticalSliderYarim_3.value()
        progress = (100 - value) / 100
        print(str(progress))
        print("value: "+str(value))

        styleSheetProgress = """ 
            QFrame{ 
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:180.2, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgba(85, 170, 255, 255));\n
                border-radius: 100px;
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
        self.ui.akuProgress_3.setStyleSheet(newStyleSheet)
        self.ui.yakitProgress_3.setStyleSheet(newStyleSheet)

    def yag_hararet_refresh(self):
        value = self.ui.verticalSliderYarim_3.value()
        progress = (100 - value) / 100
        print(str(progress))
        print("value: "+str(value))

        styleSheetProgress = """ 
            QFrame{ 
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:180.2, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgba(249, 201, 111, 255));\n
                border-radius: 100px;
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
        self.ui.yagProgress_3.setStyleSheet(newStyleSheet)
        self.ui.hararetProgress_3.setStyleSheet(newStyleSheet)

    def hiz_refresh(self):
        value = self.ui.verticalSlider_6.value()
        progress = (100 - value) / 100
        print(str(progress))
        print("value: "+str(value))

        styleSheetProgress = """ 
            QFrame{ 
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:242.2, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgba(64, 249, 243, 255));\n
                border-radius: 140px;
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
        self.ui.kmh_3.setText(str(hizGosterge))
        self.ui.hizProgress_3.setStyleSheet(newStyleSheet)

    def _trigger_refresh(self):
        deger = self.ui.verticalSlider_5.value()
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

        """ if deger<=17 and deger>=8:
            #progress < 0.92 and progress >= 0.83
            #5 il 10
            if deger == 8:
                deger1 = deger *62.5
            elif deger == 9:
                deger1 = deger* 62.1
            elif deger == 10:
                deger1 = deger*61.7
            elif deger == 11:
                deger1=deger*61.3
            elif deger == 12:
                deger1=deger*60.9
            elif deger == 13:
                deger1 = deger*60.5
            elif deger == 14:
                deger1 = deger*60.1
            elif deger == 15:
                deger1 = deger*59.7
            elif deger == 16:
                deger1 = deger*59.3
            elif deger == 17:
                deger1 = (deger*58.8)+1
        else:
            deger1=deger*50 """

        styleSheetProgress = """ 
            QFrame{ 
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:242.2, stop:{STOP_1} rgba(0, 0, 0, 0), stop:{STOP_2} rgba(64, 249, 243, 255));\n
                border-radius: 140px;
            }
        """
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStyleSheet1 = styleSheetProgress.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        deger1 = int(deger1)
        self.ui.rpm_3.setText(str(deger1+1))

        self.ui.rpmProgress_3.setStyleSheet(newStyleSheet1)

    #def cizik(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
