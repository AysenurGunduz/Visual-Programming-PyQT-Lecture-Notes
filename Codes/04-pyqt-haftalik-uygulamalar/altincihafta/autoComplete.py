from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # auto complete options                                                 
        names = ["Apple", "Alps", "Berry", "Cherry" ,"Ayşe"] #bu kelimeler arasında arama yapıyor. Birkaç harfi girdikten sonra otomatik tamamlama yapar.
        completer = QCompleter(names)

        # create line edit and add auto complete                                
        self.lineedit = QLineEdit() #giriş alanı oluşturduk
        self.lineedit.setCompleter(completer) # burada otomatik tamamlama özelliğini ekledik
        layout.addWidget(self.lineedit, 0, 0) #0,0 ile pencerenin neresine yerleşeceğini belirledik

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())