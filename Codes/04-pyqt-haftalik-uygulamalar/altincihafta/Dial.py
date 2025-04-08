from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.dial = QDial()
        self.dial.setMinimum(0) #minimum değer
        self.dial.setMaximum(100) #maksimum değer
        self.dial.setValue(40) #formu ilk çalıştırdığımda hangi değerden başlayacak
        self.dial.valueChanged.connect(self.sliderMoved) #tuttuğumuz değeri gösterir, clikc gibi tıklayıp bırakmıyoruz sürekli tutuyoruz
        layout.addWidget(self.dial)

    def sliderMoved(self):
        print("Dial value = %i" % (self.dial.value()))

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())