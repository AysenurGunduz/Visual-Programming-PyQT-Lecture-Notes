import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        mySlider = QSlider(Qt.Horizontal, self) #horizantal değişirse dikey de olur. Sadece yatay değil dikeyde de olabilir.
        mySlider.setGeometry(30, 40, 200, 30) #ayarlamarını yaptık burada
        mySlider.valueChanged[int].connect(self.changeValue)
        mySlider = QSlider(Qt.Vertical, self) #horizantal değişirse dikey de olur. Sadece yatay değil dikeyde de olabilir.
        mySlider.setGeometry(200, 30, 10, 200) #ayarlamarını yaptık burada
        mySlider.valueChanged[int].connect(self.changeValue)

        self.setGeometry(50,50,320,200)
        self.setWindowTitle("QSlider Example")
        self.show()

    def changeValue(self, value):
        print(value) #değer girmezsek 0-99 arasınsında değerler alırız. Değer girersek o değer aralığında değer alırız.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())