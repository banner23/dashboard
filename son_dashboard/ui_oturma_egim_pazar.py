# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oturma_egimErLfFw.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.anaFrame = QFrame(self.centralwidget)
        self.anaFrame.setObjectName(u"anaFrame")
        self.anaFrame.setStyleSheet(u"background-color: rgb(6, 6, 58);")
        self.anaFrame.setFrameShape(QFrame.StyledPanel)
        self.anaFrame.setFrameShadow(QFrame.Raised)
        self.aracAnaFrame = QFrame(self.anaFrame)
        self.aracAnaFrame.setObjectName(u"aracAnaFrame")
        self.aracAnaFrame.setGeometry(QRect(40, 100, 400, 650))
        self.aracAnaFrame.setFrameShape(QFrame.StyledPanel)
        self.aracAnaFrame.setFrameShadow(QFrame.Raised)
        self.koltukDuzen = QFrame(self.aracAnaFrame)
        self.koltukDuzen.setObjectName(u"koltukDuzen")
        self.koltukDuzen.setGeometry(QRect(65, 280, 248, 280))
        self.koltukDuzen.setStyleSheet(u"")
        self.koltukDuzen.setFrameShape(QFrame.StyledPanel)
        self.koltukDuzen.setFrameShadow(QFrame.Raised)
        self.onKoltukSol = QLabel(self.koltukDuzen)
        self.onKoltukSol.setObjectName(u"onKoltukSol")
        self.onKoltukSol.setGeometry(QRect(20, 10, 55, 55))
        self.onKoltukSol.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png"))
        self.onKoltukSol.setScaledContents(True)
        self.onKoltukSag = QLabel(self.koltukDuzen)
        self.onKoltukSag.setObjectName(u"onKoltukSag")
        self.onKoltukSag.setGeometry(QRect(175, 10, 55, 55))
        self.onKoltukSag.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png"))
        self.onKoltukSag.setScaledContents(True)
        self.koltuk1 = QLabel(self.koltukDuzen)
        self.koltuk1.setObjectName(u"koltuk1")
        self.koltuk1.setGeometry(QRect(25, 110, 45, 45))
        self.koltuk1.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png"))
        self.koltuk1.setScaledContents(True)
        self.koltuk2 = QLabel(self.koltukDuzen)
        self.koltuk2.setObjectName(u"koltuk2")
        self.koltuk2.setGeometry(QRect(25, 165, 45, 45))
        self.koltuk2.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png"))
        self.koltuk2.setScaledContents(True)
        self.koltuk3 = QLabel(self.koltukDuzen)
        self.koltuk3.setObjectName(u"koltuk3")
        self.koltuk3.setGeometry(QRect(25, 220, 45, 45))
        self.koltuk3.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png"))
        self.koltuk3.setScaledContents(True)
        self.koltukKule = QLabel(self.koltukDuzen)
        self.koltukKule.setObjectName(u"koltukKule")
        self.koltukKule.setGeometry(QRect(105, 130, 45, 45))
        self.koltukKule.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png"))
        self.koltukKule.setScaledContents(True)
        self.koltuk4 = QLabel(self.koltukDuzen)
        self.koltuk4.setObjectName(u"koltuk4")
        self.koltuk4.setGeometry(QRect(185, 110, 45, 45))
        self.koltuk4.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png"))
        self.koltuk4.setScaledContents(True)
        self.koltuk5 = QLabel(self.koltukDuzen)
        self.koltuk5.setObjectName(u"koltuk5")
        self.koltuk5.setGeometry(QRect(185, 165, 45, 45))
        self.koltuk5.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png"))
        self.koltuk5.setScaledContents(True)
        self.koltuk6 = QLabel(self.koltukDuzen)
        self.koltuk6.setObjectName(u"koltuk6")
        self.koltuk6.setGeometry(QRect(185, 220, 45, 45))
        self.koltuk6.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png"))
        self.koltuk6.setScaledContents(True)
        self.arac = QLabel(self.aracAnaFrame)
        self.arac.setObjectName(u"arac")
        self.arac.setGeometry(QRect(0, 0, 380, 650))
        self.arac.setPixmap(QPixmap(u"E:\QT Çalışmaları\son_dashboard\kobraustten.png"))
        self.arac.setScaledContents(True)
        self.arac.raise_()
        self.koltukDuzen.raise_()
        self.egimAnaFrame = QFrame(self.anaFrame)
        self.egimAnaFrame.setObjectName(u"egimAnaFrame")
        self.egimAnaFrame.setGeometry(QRect(480, 80, 700, 700))
        self.egimAnaFrame.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"background-color: rgb(6, 6, 58);")
        self.egimAnaFrame.setFrameShape(QFrame.StyledPanel)
        self.egimAnaFrame.setFrameShadow(QFrame.Raised)
        self.egimFrame1 = QFrame(self.egimAnaFrame)
        self.egimFrame1.setObjectName(u"egimFrame1")
        self.egimFrame1.setGeometry(QRect(50, 50, 600, 600))
        self.egimFrame1.setStyleSheet(u"border-radius: 300px;\n"
"background-color: rgb(3, 2, 34);")
        self.egimFrame1.setFrameShape(QFrame.StyledPanel)
        self.egimFrame1.setFrameShadow(QFrame.Raised)
        self.labelSolust10 = QLabel(self.egimAnaFrame)
        self.labelSolust10.setObjectName(u"labelSolust10")
        self.labelSolust10.setGeometry(QRect(20, 210, 40, 40))
        self.labelSolust10.setStyleSheet(u"background-color: transparent;")
        self.labelSolust10.setAlignment(Qt.AlignCenter)
        self.labelSolust20 = QLabel(self.egimAnaFrame)
        self.labelSolust20.setObjectName(u"labelSolust20")
        self.labelSolust20.setGeometry(QRect(80, 100, 40, 40))
        self.labelSolust20.setStyleSheet(u"background-color: transparent;")
        self.labelSolust20.setAlignment(Qt.AlignCenter)
        self.labelSolust30 = QLabel(self.egimAnaFrame)
        self.labelSolust30.setObjectName(u"labelSolust30")
        self.labelSolust30.setGeometry(QRect(180, 25, 40, 40))
        self.labelSolust30.setStyleSheet(u"background-color: transparent;")
        self.labelSolust30.setAlignment(Qt.AlignCenter)
        self.labelSolust40 = QLabel(self.egimAnaFrame)
        self.labelSolust40.setObjectName(u"labelSolust40")
        self.labelSolust40.setGeometry(QRect(285, 0, 40, 40))
        self.labelSolust40.setStyleSheet(u"background-color: transparent;")
        self.labelSolust40.setAlignment(Qt.AlignCenter)
        self.labelSagust10 = QLabel(self.egimAnaFrame)
        self.labelSagust10.setObjectName(u"labelSagust10")
        self.labelSagust10.setGeometry(QRect(640, 210, 40, 40))
        self.labelSagust10.setStyleSheet(u"background-color: transparent;")
        self.labelSagust10.setAlignment(Qt.AlignCenter)
        self.labelSagust20 = QLabel(self.egimAnaFrame)
        self.labelSagust20.setObjectName(u"labelSagust20")
        self.labelSagust20.setGeometry(QRect(580, 100, 40, 40))
        self.labelSagust20.setStyleSheet(u"background-color: transparent;")
        self.labelSagust20.setAlignment(Qt.AlignCenter)
        self.labelSagust30 = QLabel(self.egimAnaFrame)
        self.labelSagust30.setObjectName(u"labelSagust30")
        self.labelSagust30.setGeometry(QRect(500, 40, 40, 40))
        self.labelSagust30.setStyleSheet(u"background-color: transparent;")
        self.labelSagust30.setAlignment(Qt.AlignCenter)
        self.labelSagust40 = QLabel(self.egimAnaFrame)
        self.labelSagust40.setObjectName(u"labelSagust40")
        self.labelSagust40.setGeometry(QRect(385, 0, 40, 40))
        self.labelSagust40.setStyleSheet(u"background-color: transparent;")
        self.labelSagust40.setAlignment(Qt.AlignCenter)
        self.labelSolalt60 = QLabel(self.egimAnaFrame)
        self.labelSolalt60.setObjectName(u"labelSolalt60")
        self.labelSolalt60.setGeometry(QRect(275, 660, 40, 40))
        self.labelSolalt60.setStyleSheet(u"background-color: transparent;")
        self.labelSolalt60.setAlignment(Qt.AlignCenter)
        self.labelSagalt60 = QLabel(self.egimAnaFrame)
        self.labelSagalt60.setObjectName(u"labelSagalt60")
        self.labelSagalt60.setGeometry(QRect(385, 660, 40, 40))
        self.labelSagalt60.setStyleSheet(u"background-color: transparent;")
        self.labelSagalt60.setAlignment(Qt.AlignCenter)
        self.labelSolalt20 = QLabel(self.egimAnaFrame)
        self.labelSolalt20.setObjectName(u"labelSolalt20")
        self.labelSolalt20.setGeometry(QRect(30, 480, 40, 40))
        self.labelSolalt20.setStyleSheet(u"background-color: transparent;")
        self.labelSolalt20.setAlignment(Qt.AlignCenter)
        self.labelSolalt30 = QLabel(self.egimAnaFrame)
        self.labelSolalt30.setObjectName(u"labelSolalt30")
        self.labelSolalt30.setGeometry(QRect(65, 540, 40, 40))
        self.labelSolalt30.setStyleSheet(u"background-color: transparent;")
        self.labelSolalt30.setAlignment(Qt.AlignCenter)
        self.labelSolalt40 = QLabel(self.egimAnaFrame)
        self.labelSolalt40.setObjectName(u"labelSolalt40")
        self.labelSolalt40.setGeometry(QRect(125, 600, 40, 40))
        self.labelSolalt40.setStyleSheet(u"background-color: transparent;")
        self.labelSolalt40.setAlignment(Qt.AlignCenter)
        self.labelSolalt50 = QLabel(self.egimAnaFrame)
        self.labelSolalt50.setObjectName(u"labelSolalt50")
        self.labelSolalt50.setGeometry(QRect(200, 640, 40, 40))
        self.labelSolalt50.setStyleSheet(u"background-color: transparent;")
        self.labelSolalt50.setAlignment(Qt.AlignCenter)
        self.labelSagalt50 = QLabel(self.egimAnaFrame)
        self.labelSagalt50.setObjectName(u"labelSagalt50")
        self.labelSagalt50.setGeometry(QRect(460, 640, 40, 40))
        self.labelSagalt50.setStyleSheet(u"background-color: transparent;")
        self.labelSagalt50.setAlignment(Qt.AlignCenter)
        self.labelSagalt40 = QLabel(self.egimAnaFrame)
        self.labelSagalt40.setObjectName(u"labelSagalt40")
        self.labelSagalt40.setGeometry(QRect(535, 600, 40, 40))
        self.labelSagalt40.setStyleSheet(u"background-color: transparent;")
        self.labelSagalt40.setAlignment(Qt.AlignCenter)
        self.labelSagalt30 = QLabel(self.egimAnaFrame)
        self.labelSagalt30.setObjectName(u"labelSagalt30")
        self.labelSagalt30.setGeometry(QRect(595, 540, 40, 40))
        self.labelSagalt30.setStyleSheet(u"background-color: transparent;")
        self.labelSagalt30.setAlignment(Qt.AlignCenter)
        self.labelSagalt20 = QLabel(self.egimAnaFrame)
        self.labelSagalt20.setObjectName(u"labelSagalt20")
        self.labelSagalt20.setGeometry(QRect(630, 480, 40, 40))
        self.labelSagalt20.setStyleSheet(u"background-color: transparent;")
        self.labelSagalt20.setAlignment(Qt.AlignCenter)
        self.labelSagalt10 = QLabel(self.egimAnaFrame)
        self.labelSagalt10.setObjectName(u"labelSagalt10")
        self.labelSagalt10.setGeometry(QRect(650, 420, 40, 40))
        self.labelSagalt10.setStyleSheet(u"background-color: transparent;")
        self.labelSagalt10.setAlignment(Qt.AlignCenter)
        self.egimGradient = QFrame(self.egimAnaFrame)
        self.egimGradient.setObjectName(u"egimGradient")
        self.egimGradient.setGeometry(QRect(40, 40, 620, 620))
        self.egimGradient.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.526, y2:0.988636, stop:0 rgba(254, 124, 0, 255), stop:1 rgba(108, 1, 175, 255));\n"
"border-radius: 310px;")
        self.egimGradient.setFrameShape(QFrame.StyledPanel)
        self.egimGradient.setFrameShadow(QFrame.Raised)
        self.yatayCizgi = QFrame(self.egimAnaFrame)
        self.yatayCizgi.setObjectName(u"yatayCizgi")
        self.yatayCizgi.setGeometry(QRect(0, 330, 700, 40))
        self.yatayCizgi.setStyleSheet(u"background-color: rgb(6, 6, 58);")
        self.yatayCizgi.setFrameShape(QFrame.StyledPanel)
        self.yatayCizgi.setFrameShadow(QFrame.Raised)
        self.kirmizi = QFrame(self.yatayCizgi)
        self.kirmizi.setObjectName(u"kirmizi")
        self.kirmizi.setGeometry(QRect(65, 15, 555, 10))
        self.kirmizi.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.kirmizi.setFrameShape(QFrame.StyledPanel)
        self.kirmizi.setFrameShadow(QFrame.Raised)
        self.eksi = QLabel(self.yatayCizgi)
        self.eksi.setObjectName(u"eksi")
        self.eksi.setGeometry(QRect(40, -10, 40, 40))
        self.eksi.setAlignment(Qt.AlignCenter)
        self.arti = QLabel(self.yatayCizgi)
        self.arti.setObjectName(u"arti")
        self.arti.setGeometry(QRect(620, -5, 40, 40))
        self.arti.setAlignment(Qt.AlignCenter)
        self.dikeyCizgi = QFrame(self.egimAnaFrame)
        self.dikeyCizgi.setObjectName(u"dikeyCizgi")
        self.dikeyCizgi.setGeometry(QRect(330, 0, 40, 700))
        self.dikeyCizgi.setStyleSheet(u"background-color: rgb(6, 6, 58);")
        self.dikeyCizgi.setFrameShape(QFrame.StyledPanel)
        self.dikeyCizgi.setFrameShadow(QFrame.Raised)
        self.egimFrameOnYuz = QFrame(self.egimAnaFrame)
        self.egimFrameOnYuz.setObjectName(u"egimFrameOnYuz")
        self.egimFrameOnYuz.setGeometry(QRect(100, 100, 500, 500))
        self.egimFrameOnYuz.setStyleSheet(u"border-radius: 250px;\n"
"background-color: rgba(6, 6, 58,255);")
        self.egimFrameOnYuz.setFrameShape(QFrame.StyledPanel)
        self.egimFrameOnYuz.setFrameShadow(QFrame.Raised)
        self.dikey_egim_resim = QLabel(self.egimFrameOnYuz)
        self.dikey_egim_resim.setObjectName(u"dikey_egim_resim")
        self.dikey_egim_resim.setGeometry(QRect(110, 260, 270, 150))
        self.dikey_egim_resim.setStyleSheet(u"background-color: none;")
        self.dikey_egim_resim.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\kobrayan.png"))
        self.dikey_egim_resim.setScaledContents(True)
        self.dikey_egim_resim.setMargin(-1)
        self.dikey_egim_deger = QLabel(self.egimFrameOnYuz)
        self.dikey_egim_deger.setObjectName(u"dikey_egim_deger")
        self.dikey_egim_deger.setGeometry(QRect(250, 420, 120, 40))
        self.dikey_egim_deger.setStyleSheet(u"background-color: none;")
        self.dikey_egim_deger.setAlignment(Qt.AlignCenter)
        self.dikey_egim = QLabel(self.egimFrameOnYuz)
        self.dikey_egim.setObjectName(u"dikey_egim")
        self.dikey_egim.setGeometry(QRect(130, 420, 120, 40))
        self.dikey_egim.setStyleSheet(u"background-color: none;")
        self.dikey_egim.setAlignment(Qt.AlignCenter)
        self.yanal_egim_resim = QLabel(self.egimFrameOnYuz)
        self.yanal_egim_resim.setObjectName(u"yanal_egim_resim")
        self.yanal_egim_resim.setGeometry(QRect(170, 30, 170, 150))
        self.yanal_egim_resim.setStyleSheet(u"background-color: none;")
        self.yanal_egim_resim.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\kobraon.png"))
        self.yanal_egim_resim.setScaledContents(True)
        self.yanal_egim_resim.setMargin(-1)
        self.dikey_egim_2 = QLabel(self.egimFrameOnYuz)
        self.dikey_egim_2.setObjectName(u"dikey_egim_2")
        self.dikey_egim_2.setGeometry(QRect(130, 190, 120, 40))
        self.dikey_egim_2.setStyleSheet(u"background-color: none;")
        self.dikey_egim_2.setAlignment(Qt.AlignCenter)
        self.dikey_egim_deger_2 = QLabel(self.egimFrameOnYuz)
        self.dikey_egim_deger_2.setObjectName(u"dikey_egim_deger_2")
        self.dikey_egim_deger_2.setGeometry(QRect(250, 190, 120, 40))
        self.dikey_egim_deger_2.setStyleSheet(u"background-color: none;")
        self.dikey_egim_deger_2.setAlignment(Qt.AlignCenter)
        self.solUstProgress = QFrame(self.egimAnaFrame)
        self.solUstProgress.setObjectName(u"solUstProgress")
        self.solUstProgress.setGeometry(QRect(75, 75, 275, 275))
        self.solUstProgress.setStyleSheet(u"""
        QFrame{
border-top-left-radius: 275px;
background-color: rgb(255, 255, 127);
background-color: rgb(252, 201, 109);
background-color: qconicalgradient(cx:1, cy:1, angle:180, stop:0.858757 rgba(85, 170, 255, 0), stop:0.860056 rgba(252, 201, 109, 255));
}
        """)
        self.solUstProgress.setFrameShape(QFrame.StyledPanel)
        self.solUstProgress.setFrameShadow(QFrame.Raised)
        self.sagUstProgress = QFrame(self.egimAnaFrame)
        self.sagUstProgress.setObjectName(u"sagUstProgress")
        self.sagUstProgress.setGeometry(QRect(350, 75, 275, 275))
        self.sagUstProgress.setStyleSheet(u"""
                QFrame{
border-top-right-radius: 275px;
background-color: qconicalgradient(cx:0, cy:1, angle:0, stop:0.138593 rgba(252, 201, 109, 255), stop:0.14 rgba(85, 170, 255, 0));
}
        """)
        self.sagUstProgress.setFrameShape(QFrame.StyledPanel)
        self.sagUstProgress.setFrameShadow(QFrame.Raised)
        self.solAltProgress = QFrame(self.egimAnaFrame)
        self.solAltProgress.setObjectName(u"solAltProgress")
        self.solAltProgress.setGeometry(QRect(75, 350, 275, 275))
        self.solAltProgress.setStyleSheet(u"border-bottom-left-radius: 275px;\n"
"background-color: rgb(255, 255, 127);\n"
"background-color: rgb(252, 201, 109);")
        self.solAltProgress.setFrameShape(QFrame.StyledPanel)
        self.solAltProgress.setFrameShadow(QFrame.Raised)
        self.sagAltProgress = QFrame(self.egimAnaFrame)
        self.sagAltProgress.setObjectName(u"sagAltProgress")
        self.sagAltProgress.setGeometry(QRect(350, 350, 275, 275))
        self.sagAltProgress.setStyleSheet(u"border-bottom-right-radius: 275px;\n"
"background-color: rgb(255, 255, 127);\n"
"background-color: rgb(252, 201, 109);")
        self.sagAltProgress.setFrameShape(QFrame.StyledPanel)
        self.sagAltProgress.setFrameShadow(QFrame.Raised)
        self.golge = QFrame(self.egimAnaFrame)
        self.golge.setObjectName(u"golge")
        self.golge.setGeometry(QRect(95, 95, 510, 510))
        self.golge.setStyleSheet(u"background-color: rgba(0, 0, 0,150);\n"
"border-radius: 255px;\n"
"border-style: solid;\n"
"border-width: 2px;")
        self.golge.setFrameShape(QFrame.StyledPanel)
        self.golge.setFrameShadow(QFrame.Raised)
        self.labelSagalt20.raise_()
        self.labelSagalt30.raise_()
        self.labelSagalt40.raise_()
        self.labelSagalt50.raise_()
        self.labelSagust10.raise_()
        self.labelSagust20.raise_()
        self.labelSagust30.raise_()
        self.labelSolalt20.raise_()
        self.labelSolalt30.raise_()
        self.labelSolalt40.raise_()
        self.labelSolalt50.raise_()
        self.labelSolalt60.raise_()
        self.labelSolust10.raise_()
        self.labelSolust20.raise_()
        self.labelSolust40.raise_()
        self.labelSagalt10.raise_()
        self.labelSagalt60.raise_()
        self.labelSagust40.raise_()
        self.labelSolust30.raise_()
        self.egimGradient.raise_()
        self.egimFrame1.raise_()
        self.sagUstProgress.raise_()
        self.solUstProgress.raise_()
        self.solAltProgress.raise_()
        self.sagAltProgress.raise_()
        self.golge.raise_()
        self.dikeyCizgi.raise_()
        self.egimFrameOnYuz.raise_()
        self.yatayCizgi.raise_()
        self.emniyet_kemeri = QLabel(self.anaFrame)
        self.emniyet_kemeri.setObjectName(u"emniyet_kemeri")
        self.emniyet_kemeri.setGeometry(QRect(40, 30, 400, 50))
        self.emniyet_kemeri.setAlignment(Qt.AlignCenter)
        self.egim_kontrol = QLabel(self.anaFrame)
        self.egim_kontrol.setObjectName(u"egim_kontrol")
        self.egim_kontrol.setGeometry(QRect(480, 30, 700, 50))
        self.egim_kontrol.setAlignment(Qt.AlignCenter)
        self.sliderKume = QFrame(self.anaFrame)
        self.sliderKume.setObjectName(u"sliderKume")
        self.sliderKume.setGeometry(QRect(0, 100, 51, 671))
        self.sliderKume.setFrameShape(QFrame.StyledPanel)
        self.sliderKume.setFrameShadow(QFrame.Raised)
        self.LabelSolUst = QLabel(self.sliderKume)
        self.LabelSolUst.setObjectName(u"LabelSolUst")
        self.LabelSolUst.setGeometry(QRect(10, 10, 30, 30))
        self.LabelSolUst.setAlignment(Qt.AlignCenter)
        self.sliderSolUst = QSlider(self.sliderKume)
        self.sliderSolUst.setObjectName(u"sliderSolUst")
        self.sliderSolUst.setGeometry(QRect(20, 40, 18, 110))
        self.sliderSolUst.setMaximum(24)
        self.sliderSolUst.setOrientation(Qt.Vertical)
        self.labelSagUst = QLabel(self.sliderKume)
        self.labelSagUst.setObjectName(u"labelSagUst")
        self.labelSagUst.setGeometry(QRect(10, 350, 35, 30))
        self.labelSagUst.setAlignment(Qt.AlignCenter)
        self.labelSolAlt = QLabel(self.sliderKume)
        self.labelSolAlt.setObjectName(u"labelSolAlt")
        self.labelSolAlt.setGeometry(QRect(10, 180, 30, 30))
        self.labelSolAlt.setAlignment(Qt.AlignCenter)
        self.sliderSagAlt = QSlider(self.sliderKume)
        self.sliderSagAlt.setObjectName(u"sliderSagAlt")
        self.sliderSagAlt.setGeometry(QRect(20, 550, 18, 110))
        self.sliderSagAlt.setOrientation(Qt.Vertical)
        self.sliderSolAlt = QSlider(self.sliderKume)
        self.sliderSolAlt.setObjectName(u"sliderSolAlt")
        self.sliderSolAlt.setGeometry(QRect(20, 210, 18, 110))
        self.sliderSolAlt.setOrientation(Qt.Vertical)
        self.sliderSagUst = QSlider(self.sliderKume)
        self.sliderSagUst.setObjectName(u"sliderSagUst")
        self.sliderSagUst.setMaximum(24)
        self.sliderSagUst.setGeometry(QRect(20, 380, 18, 110))
        self.sliderSagUst.setOrientation(Qt.Vertical)
        self.labelSagAlt = QLabel(self.sliderKume)
        self.labelSagAlt.setObjectName(u"labelSagAlt")
        self.labelSagAlt.setGeometry(QRect(10, 520, 35, 30))
        self.labelSagAlt.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.anaFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.onKoltukSol.setText("")
        self.onKoltukSag.setText("")
        self.koltuk1.setText("")
        self.koltuk2.setText("")
        self.koltuk3.setText("")
        self.koltukKule.setText("")
        self.koltuk4.setText("")
        self.koltuk5.setText("")
        self.koltuk6.setText("")
        self.arac.setText("")
        self.labelSolust10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">10</span></p></body></html>", None))
        self.labelSolust20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">20</span></p></body></html>", None))
        self.labelSolust30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">30</span></p></body></html>", None))
        self.labelSolust40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ff0000\">40</span></p></body></html>", None))
        self.labelSagust10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">10</span></p></body></html>", None))
        self.labelSagust20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">20</span></p></body></html>", None))
        self.labelSagust30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">30</span></p></body></html>", None))
        self.labelSagust40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ff0000\">40</span></p></body></html>", None))
        self.labelSolalt60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ff0000\">60</span></p></body></html>", None))
        self.labelSagalt60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ff0000\">60</span></p></body></html>", None))
        self.labelSolalt20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">20</span></p></body></html>", None))
        self.labelSolalt30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">30</span></p></body></html>", None))
        self.labelSolalt40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">40</span></p></body></html>", None))
        self.labelSolalt50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">50</span></p></body></html>", None))
        self.labelSagalt50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">50</span></p></body></html>", None))
        self.labelSagalt40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">40</span></p></body></html>", None))
        self.labelSagalt30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">30</span></p></body></html>", None))
        self.labelSagalt20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">20</span></p></body></html>", None))
        self.labelSagalt10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-family: Arial Black;  color: #ffffff\">10</span></p></body></html>", None))
        self.eksi.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; color: #ffffff; font-family: Arial Black\">-</span></p></body></html>", None))
        self.arti.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; color: #ffffff; font-family: Arial Black\">+</span></p></body></html>", None))
        self.dikey_egim_resim.setText("")
        self.dikey_egim_deger.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color: #ffffff; font-family: Arial Black\">10</span></p></body></html>", None))
        self.dikey_egim.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color: #ffffff; font-family: Arial Black\">Dikey E\u011fim</span></p></body></html>", None))
        self.yanal_egim_resim.setText("")
        self.dikey_egim_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color: #ffffff; font-family: Arial Black\">Yanal E\u011fim</span></p></body></html>", None))
        self.dikey_egim_deger_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color: #ffffff; font-family: Arial Black\">12</span></p></body></html>", None))
        self.emniyet_kemeri.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:15pt; font-family: Arial Black; color: #ffffff;\">Emniyet Kemeri \u0130kaz Sistemi</span></p></body></html>", None))
        self.egim_kontrol.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:17pt; font-family: Arial Black; color: #ffffff;\">E\u011fim Kontrol Sistemi</span></p></body></html>", None))
        self.LabelSolUst.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color: #ffffff;\">Sol\u00dc</span></p></body></html>", None))
        self.labelSagUst.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color: #ffffff;\">Sag\u00dc</span></p></body></html>", None))
        self.labelSolAlt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color: #ffffff;\">SolA</span></p></body></html>", None))
        self.labelSagAlt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color: #ffffff;\">SagA</span></p></body></html>", None))
    # retranslateUi

