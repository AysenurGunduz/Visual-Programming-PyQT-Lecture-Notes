import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class RenkAyarlayici(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Kırmızı Dial
        self.kirmizi_dial = QDial(self)
        self.kirmizi_dial.setMinimum(0)
        self.kirmizi_dial.setMaximum(255)
        self.kirmizi_dial.setValue(0)
        self.kirmizi_dial.valueChanged.connect(self.renkDegistir)

        # Yeşil Dial
        self.yesil_dial = QDial(self)
        self.yesil_dial.setMinimum(0)
        self.yesil_dial.setMaximum(255)
        self.yesil_dial.setValue(0)
        self.yesil_dial.valueChanged.connect(self.renkDegistir)

        # Mavi Dial
        self.mavi_dial = QDial(self)
        self.mavi_dial.setMinimum(0)
        self.mavi_dial.setMaximum(255)
        self.mavi_dial.setValue(0)
        self.mavi_dial.valueChanged.connect(self.renkDegistir)

        # Renk Göstergesi
        self.renk_gostergesi = QLabel(self)
        self.renk_gostergesi.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.renk_gostergesi.setAlignment(Qt.AlignCenter)

        # Dial Layout'ları
        dial_layout = QHBoxLayout()
        dial_layout.addWidget(self.kirmizi_dial)
        dial_layout.addWidget(self.yesil_dial)
        dial_layout.addWidget(self.mavi_dial)

        # Ana Layout
        ana_layout = QVBoxLayout()
        ana_layout.addLayout(dial_layout)
        ana_layout.addWidget(self.renk_gostergesi)
        self.setLayout(ana_layout)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Tam Renk Paleti Ayarlama')
        self.show()

    def renkDegistir(self, value):
        # Dial değerlerine göre rengi güncelle
        kirmizi = self.kirmizi_dial.value()
        yesil = self.yesil_dial.value()
        mavi = self.mavi_dial.value()
        renk = QColor(kirmizi, yesil, mavi)
        self.renk_gostergesi.setStyleSheet(f"background-color: {renk.name()};")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    renk_ayarlayici = RenkAyarlayici()
    sys.exit(app.exec_())