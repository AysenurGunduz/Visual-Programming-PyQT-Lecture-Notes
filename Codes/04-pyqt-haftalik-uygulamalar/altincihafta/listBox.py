from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.listwidget = QListWidget()
        self.listwidget.insertItem(0, "Red")
        self.listwidget.insertItem(1, "Orange")
        self.listwidget.insertItem(2, "Blue")
        self.listwidget.insertItem(3, "White") #bu şekilde listeye ekleme yaptık
        self.listwidget.insertItem(4, "Green")
        self.listwidget.clicked.connect(self.clicked)
        layout.addWidget(self.listwidget)
        #birden fazla click yapabiliriz.

    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem() #tıkladığımızda hangi elemanı seçtiğimizi gösterir 
        print(item.text())

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())