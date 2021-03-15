import RPi.GPIO as GPIO
import time
import itertools

GPIO.setmode(GPIO.BOARD)
#1
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#2
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#3
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#4
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#5
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#6
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#7
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#8
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#9
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

Leftmatrix = QMatrix()
Leftmatrix.rotate(90)
Rightmatrix = QMatrix()
Rightmatrix.rotate(-90)

while True:
    time.sleep(1)
    #1
    if GPIO.input(10) == GPIO.HIGH:
        if GPIO.input(12) == GPIO.HIGH:
            print("1.Koltuk Kemer Takılı :)")
            self.ui.koltukSurucu = QLabel(self.koltukDuzen)
            self.ui.koltukSurucu.setObjectName(u"koltukSurucu")
            self.ui.koltukSurucu.setGeometry(QRect(20, 10, 55, 55))
            self.ui.koltukSurucu.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png"))
            self.koltukSurucu.setScaledContents(True)
        elif GPIO.input(12) == GPIO.LOW:
            print("1.Koltuk Kemer Takın!!")
            self.ui.koltukSurucu = QLabel(self.koltukDuzen)
            self.ui.koltukSurucu.setObjectName(u"koltukSurucu")
            self.ui.koltukSurucu.setGeometry(QRect(20, 10, 55, 55))
            self.ui.koltukSurucu.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png"))
            self.koltukSurucu.setScaledContents(True)
    elif GPIO.input(10) == GPIO.LOW:
        print("1.Koltuk Boş")
        self.ui.koltukSurucu = QLabel(self.koltukDuzen)
        self.ui.koltukSurucu.setObjectName(u"koltukSurucu")
        self.ui.koltukSurucu.setGeometry(QRect(20, 10, 55, 55))
        self.ui.koltukSurucu.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png"))
        self.koltukSurucu.setScaledContents(True)
    #2
    if GPIO.input(11) == GPIO.HIGH:
        if GPIO.input(13) == GPIO.HIGH:
            print("2.Koltuk Kemer Takılı :)")
            self.koltukKomutan = QLabel(self.koltukDuzen)
            self.koltukKomutan.setObjectName(u"koltukKomutan")
            self.koltukKomutan.setGeometry(QRect(175, 10, 55, 55))
            self.koltukKomutan.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png"))
            self.koltukKomutan.setScaledContents(True)
        elif GPIO.input(13) == GPIO.LOW:
            print("2.Koltuk Kemer Takın!!")
            self.koltukKomutan = QLabel(self.koltukDuzen)
            self.koltukKomutan.setObjectName(u"koltukKomutan")
            self.koltukKomutan.setGeometry(QRect(175, 10, 55, 55))
            self.koltukKomutan.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png"))
            self.koltukKomutan.setScaledContents(True)
    elif GPIO.input(11) == GPIO.LOW:
        print("2.Koltuk Boş")
        self.koltukKomutan = QLabel(self.koltukDuzen)
        self.koltukKomutan.setObjectName(u"koltukKomutan")
        self.koltukKomutan.setGeometry(QRect(175, 10, 55, 55))
        self.koltukKomutan.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png"))
        self.koltukKomutan.setScaledContents(True)
    #3
    if GPIO.input(18) == GPIO.HIGH:
        if GPIO.input(21) == GPIO.HIGH:
            print("3.Koltuk Kemer Takılı :)")
            self.koltukP1 = QLabel(self.koltukDuzen)
            self.koltukP1.setObjectName(u"koltuk1")
            self.koltuk1.setGeometry(QRect(25, 110, 45, 45))
            self.koltukP1.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
        elif GPIO.input(21) == GPIO.LOW:
            print("3.Koltuk Kemer Takın!!")
            self.koltukP1 = QLabel(self.koltukDuzen)
            self.koltukP1.setObjectName(u"koltukP1")
            self.koltuk1.setGeometry(QRect(25, 110, 45, 45))
            self.koltukP1.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
            self.koltukP1.setScaledContents(True)
    elif GPIO.input(18) == GPIO.LOW:
        print("3.Koltuk Boş")
        self.koltukP1 = QLabel(self.koltukDuzen)
        self.koltukP1.setObjectName(u"koltuk1")
        self.koltuk1.setGeometry(QRect(25, 110, 45, 45))
        self.koltukP1.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
        self.koltukP1.setScaledContents(True)
    #4
    if GPIO.input(19) == GPIO.HIGH:
        if GPIO.input(22) == GPIO.HIGH:
            print("4.Koltuk Kemer Takılı :)")
            self.koltukP2 = QLabel(self.koltukDuzen)
            self.koltukP2.setObjectName(u"koltukP2")        
            self.koltuk2.setGeometry(QRect(25, 165, 45, 45))
            self.koltukP2.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
        elif GPIO.input(22) == GPIO.LOW:
            print("4.Koltuk Kemer Takın!!")
            self.koltukP2 = QLabel(self.koltukDuzen)
            self.koltukP2.setObjectName(u"koltuk2")
            self.koltuk2.setGeometry(QRect(25, 165, 45, 45))
            self.koltukP2.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
            self.koltukP2.setScaledContents(True)
    elif GPIO.input(19) == GPIO.LOW:
        print("4.Koltuk Boş")
        self.koltukP2 = QLabel(self.koltukDuzen)
        self.koltukP2.setObjectName(u"koltuk2")
        self.koltuk1.setGeometry(QRect(25, 165, 45, 45))
        self.koltukP2.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
        self.koltukP2.setScaledContents(True)
    #5
    if GPIO.input(23) == GPIO.HIGH:
        if GPIO.input(24) == GPIO.HIGH:
            print("5.Koltuk Kemer Takılı :)")
            self.koltukP3 = QLabel(self.koltukDuzen)
            self.koltukP3.setObjectName(u"koltukP3")
            self.koltukP3.setGeometry(QRect(25, 220, 45, 45))
            self.koltukP3.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
        elif GPIO.input(24) == GPIO.LOW:
            print("5.Koltuk Kemer Takın!!")
            self.koltukP3 = QLabel(self.koltukDuzen)
            self.koltukP3.setObjectName(u"koltukP3")
            self.koltukP3.setGeometry(QRect(25, 220, 45, 45))
            self.koltukP3.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
    elif GPIO.input(23) == GPIO.LOW:
        print("5.Koltuk Boş")
        self.koltukP3 = QLabel(self.koltukDuzen)
        self.koltukP3.setObjectName(u"koltukP3")
        self.koltukP3.setGeometry(QRect(25, 220, 45, 45))
        self.koltukP3.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png").transformed(Leftmatrix, Qt.SmoothTransformation))
    #6
    if GPIO.input(26) == GPIO.HIGH:
        if GPIO.input(33) == GPIO.HIGH:
            print("6.Koltuk Kemer Takılı :)")
            self.koltukP4 = QLabel(self.koltukDuzen)
            self.koltukP4.setObjectName(u"koltukP4")
            self.koltukP4.setGeometry(QRect(185, 110, 45, 45))
            self.koltukP4.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
            self.koltukP4.setScaledContents(True)
        elif GPIO.input(33) == GPIO.LOW:
            print("6.Koltuk Kemer Takın!!")
            self.koltukP4 = QLabel(self.koltukDuzen)
            self.koltukP4.setObjectName(u"koltukP4")
            self.koltukP4.setGeometry(QRect(185, 110, 45, 45))
            self.koltukP4.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
            self.koltukP4.setScaledContents(True)
    elif GPIO.input(26) == GPIO.LOW:
        print("6.Koltuk Boş")
        self.koltukP4 = QLabel(self.koltukDuzen)
        self.koltukP4.setObjectName(u"koltukP4")
        self.koltukP4.setGeometry(QRect(185, 110, 45, 45))
        self.koltukP4.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
        self.koltukP4.setScaledContents(True)
    #7
    if GPIO.input(37) == GPIO.HIGH:
        if GPIO.input(29) == GPIO.HIGH:
            print("7.Koltuk Kemer Takılı :)")
            self.koltukP5 = QLabel(self.koltukDuzen)
            self.koltukP5.setObjectName(u"koltukP5")
            self.koltukP5.setGeometry(QRect(185, 165, 45, 45))
            self.koltukP5.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
            self.koltukP5.setScaledContents(True)
        elif GPIO.input(29) == GPIO.LOW:
            print("7.Koltuk Kemer Takın!!")
            self.koltukP5 = QLabel(self.koltukDuzen)
            self.koltukP5.setObjectName(u"koltukP5")
            self.koltukP5.setGeometry(QRect(185, 165, 45, 45))
            self.koltukP5.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
            self.koltukP5.setScaledContents(True)
    elif GPIO.input(37) == GPIO.LOW:
        print("7.Koltuk Boş")
        self.koltukP5 = QLabel(self.koltukDuzen)
        self.koltukP5.setObjectName(u"koltukP5")
        self.koltukP5.setGeometry(QRect(185, 165, 45, 45))
        self.koltukP5.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
        self.koltukP5.setScaledContents(True)
    #8
    if GPIO.input(31) == GPIO.HIGH:
        if GPIO.input(32) == GPIO.HIGH:
            print("8.Koltuk Kemer Takılı :)")
            self.koltukP6 = QLabel(self.koltukDuzen)
            self.koltukP6.setObjectName(u"koltukP6")
            self.koltukP6.setGeometry(QRect(185, 220, 45, 45))
            self.koltukP6.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
            self.koltukP6.setScaledContents(True)
        elif GPIO.input(32) == GPIO.LOW:
            print("8.Koltuk Kemer Takın!!")
            self.koltukP6 = QLabel(self.koltukDuzen)
            self.koltukP6.setObjectName(u"koltukP6")
            self.koltukP6.setGeometry(QRect(185, 220, 45, 45))
            self.koltukP6.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
            self.koltukP6.setScaledContents(True)
    elif GPIO.input(31) == GPIO.LOW:
        print("8.Koltuk Boş")
        self.koltukP6 = QLabel(self.koltukDuzen)
        self.koltukP6.setObjectName(u"koltukP6")
        self.koltukP6.setGeometry(QRect(185, 220, 45, 45))
        self.koltukP6.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png").transformed(Rightmatrix, Qt.SmoothTransformation))
        self.koltukP6.setScaledContents(True)
    #9
    if GPIO.input(35) == GPIO.HIGH:
        if GPIO.input(36) == GPIO.HIGH:
            print("9.Koltuk Kemer Takılı :)")
            self.koltukKule = QLabel(self.koltukDuzen)
            self.koltukKule.setObjectName(u"koltukKule")
            self.koltukKule.setGeometry(QRect(105, 130, 45, 45))
            self.koltukKule.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\yesilkoltuk1.png"))
            self.koltukKule.setScaledContents(True)
        elif GPIO.input(36) == GPIO.LOW:
            print("9.Koltuk Kemer Takın!!")
            self.koltukKule = QLabel(self.koltukDuzen)
            self.koltukKule.setObjectName(u"koltukKule")
            self.koltukKule.setGeometry(QRect(105, 130, 45, 45))
            self.koltukKule.setPixmap(
                QPixmap(u"E:\QT Çalışmaları\son_dashboard\k\u0131rm\u0131z\u0131koltuk1.png"))
            self.koltukKule.setScaledContents(True)
    elif GPIO.input(35) == GPIO.LOW:
        print("9.Koltuk Boş")
        self.koltukKule = QLabel(self.koltukDuzen)
        self.koltukKule.setObjectName(u"koltukKule")
        self.koltukKule.setGeometry(QRect(105, 130, 45, 45))
        self.koltukKule.setPixmap(
            QPixmap(u"E:\QT Çalışmaları\son_dashboard\/beyaz1.png"))
        self.koltukKule.setScaledContents(True)
    
