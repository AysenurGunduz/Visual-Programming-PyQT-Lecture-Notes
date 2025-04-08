from PyQt5.QtWidgets import *
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setWindowTitle("ToolBox Example")

        self.pbar = QToolBox(self)
        self.pbar.setGeometry(100, 100, 500, 30) #geometrisini ayarladık
        #self.pbar.setValue(40) #başlangıç değeri

        # Add toolbar and items
        toolbox = QToolBox()
        layout.addWidget(toolbox, 0, 0)
        label = QLabel()
        toolbox.addItem(label, "Students")
        label = QLabel()
        toolbox.addItem(label, "Teachers")
        label = QLabel()
        toolbox.addItem(label, "Directors")

        # show number of items
        print(toolbox.count())

        # disable tab
        toolbox.setItemEnabled(0, False) #öğrenciyi kapatırız burada sanırım 

        # mouseover tooltip
        toolbox.setItemToolTip(0, "This is a tooltip") #fareyle öğrencinin üstüne gittiğimizde bu yazı görünür bilgi veriri gibi düşünelim 

        # tests if items are enabled
        print(toolbox.isItemEnabled(0))
        print(toolbox.isItemEnabled(1))

        # insert item
        item = QLabel()
        toolbox.insertItem(1, item, "Python")

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
 