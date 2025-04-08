import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(100, 100, 500, 30) #geometrisini ayarladık
        self.pbar.setValue(40) #başlangıç değeri
        
        self.setWindowTitle("QT Progressbar Example")
        self.setGeometry(300,300,700,600)   #sayfa geometrisi
        self.show()

        self.timer = QTimer() #zamanlayıcı oluşturduk
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(1000) #1 saniyede bir artacak

    def handleTimer(self):
        value = self.pbar.value()
        if value < 100:
            value = value + 1 #100 olana kadar 1 arttır
            self.pbar.setValue(value)
        else:
            self.timer.stop()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())