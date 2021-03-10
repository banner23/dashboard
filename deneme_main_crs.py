import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QMatrix, QPainter, QPalette, QPixmap, QRadialGradient, QTransform
from PySide2.QtWidgets import *


from ui_oturma_egim_ptesi import Ui_MainWindow

import time
from smbus2 import SMBus
import math

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        labelCizgiSolU20.move(135, 152)
        labelCizgiSolU20.resize(27, 16)
        labelCizgiSolU20.setScaledContents(True)
        labelCizgiSolU20.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi20 = QPixmap("aa.png")
        xformCizgi20 = QTransform()
        xformCizgi20.rotate(138)
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
        labelCizgiSagA10.move(597, 410)
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
        labelCizgiSagA20.move(570, 472)
        labelCizgiSagA20.resize(25, 15)
        labelCizgiSagA20.setScaledContents(True)
        labelCizgiSagA20.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi20 = QPixmap("aa.png")
        xformCizgi20 = QTransform()
        xformCizgi20.rotate(125)
        xformed_pixmapCizgi20 = pixmapCizgi20.transformed(xformCizgi20)
        labelCizgiSagA20.setPixmap(xformed_pixmapCizgi20)

        labelCizgiSagA30 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA30.move(532, 525)
        labelCizgiSagA30.resize(24, 16)
        labelCizgiSagA30.setScaledContents(True)
        labelCizgiSagA30.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi30 = QPixmap("aa.png")
        xformCizgi30 = QTransform()
        xformCizgi30.rotate(135)
        xformed_pixmapCizgi30 = pixmapCizgi30.transformed(xformCizgi30)
        labelCizgiSagA30.setPixmap(xformed_pixmapCizgi30)

        labelCizgiSagA40 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA40.move(480, 565)
        labelCizgiSagA40.resize(18, 25)
        labelCizgiSagA40.setScaledContents(True)
        labelCizgiSagA40.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi40 = QPixmap("aa.png")
        xformCizgi40 = QTransform()
        xformCizgi40.rotate(140)
        xformed_pixmapCizgi40 = pixmapCizgi40.transformed(xformCizgi40)
        labelCizgiSagA40.setPixmap(xformed_pixmapCizgi40)

        labelCizgiSagA50 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA50.move(420, 590)
        labelCizgiSagA50.resize(15, 25)
        labelCizgiSagA50.setScaledContents(True)
        labelCizgiSagA50.setStyleSheet("QLabel{ background-color: none;}")
        pixmapCizgi50 = QPixmap("aa.png")
        xformCizgi50 = QTransform()
        xformCizgi50.rotate(155)
        xformed_pixmapCizgi50 = pixmapCizgi50.transformed(xformCizgi50)
        labelCizgiSagA50.setPixmap(xformed_pixmapCizgi50)

        labelCizgiSagA60 = QLabel(self.ui.egimAnaFrame)
        labelCizgiSagA60.move(367, 600)
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
        labelCizgiSolA20.move(102, 472)
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
        labelCizgiSagU20.move(532, 155)
        labelCizgiSagU20.resize(27, 15)
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


        self.show()

    
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

        resimegim = value * -2.5
        Rightmatrix = QMatrix()
        Rightmatrix.rotate(resimegim)
        self.ui.yanal_egim_resim.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\kobraon.png").transformed(Rightmatrix))

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

        resimegim = value * 2.5
        Rightmatrix = QMatrix()
        Rightmatrix.rotate(resimegim)
        self.ui.yanal_egim_resim.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\kobraon.png").transformed(Rightmatrix))

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

        resimegim = value * -2.5
        Rightmatrix = QMatrix()
        Rightmatrix.rotate(resimegim)
        self.ui.dikey_egim_resim.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\kobrayan.png").transformed(Rightmatrix))

        


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

        resimegim = value * 2.5
        Rightmatrix = QMatrix()
        Rightmatrix.rotate(resimegim)
        self.ui.dikey_egim_resim.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\kobrayan.png").transformed(Rightmatrix))



if __name__ == "__main__":

    def read_byte(self):
     return bus.read_byte_data(address, self)


    def read_word(self):
        high = bus.read_byte_data(address, self)
        low = bus.read_byte_data(address, self+1)
        val = (high << 8) + low
        return val


    def read_word_2c(self):
        val = read_word(self)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val


    def dist(self, b):
        return math.sqrt((self*self)+(b*b))


    def get_y_rotation(self, y, z):
        radians = math.atan2(self, dist(y, z))
        return -math.degrees(radians)


    def get_x_rotation(self, y, z):
        radians = math.atan2(y, dist(self, z))
        return math.degrees(radians)


    bus = smbus.SMBus(1)
    address = 0x68  # MPU6050 I2C adresi

    #MPU6050 ilk calistiginda uyku modunda oldugundan, calistirmak icin asagidaki komutu veriyoruz:
    bus.write_byte_data(address, power_mgmt_1, 0)

    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    print ("Jiroskop X : ", gyro_xout, " olcekli: ", (gyro_xout / 131))
    print ("Jiroskop Y : ", gyro_yout, " olcekli: ", (gyro_yout / 131))
    print ("Jiroskop Z: ", gyro_zout, " olcekli: ", (gyro_zout / 131))

    #Ivmeolcer register'larini oku
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    print ("Ivmeolcer X: ", accel_xout, " olcekli: ", accel_xout_scaled)
    print ("Ivmeolcer Y: ", accel_yout, " olcekli: ", accel_yout_scaled)
    print ("Ivmeolcer Z: ", accel_zout, " olcekli: ", accel_zout_scaled)

    print ("X dondurme: ", get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    print ("Y dondurme: ", get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))

    self.ui.dikey_egim_deger.setText = get_x_rotation(
        accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
