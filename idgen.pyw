from random import choice
import sys
import style
from PyQt5.QtWidgets import QLabel, QSpinBox, QPushButton, QLineEdit, QGridLayout, QWidget,\
	 QApplication, QMessageBox, qApp
from PyQt5.QtGui import QIcon


class IDGen(QWidget):
    def __init__(self):
        super(IDGen, self).__init__()
        self.numbers = '123456789'
        self.letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'

        qchar = QLabel('Longitud del ID')
        self.qchar = QSpinBox(valueChanged=self.getlong)
        self.qchar.setValue(9)
        self.gbutton = QPushButton('Generar', clicked=self.actid)
        self.exitbutton = QPushButton('Cerrar', clicked=self.closethis)
        self.set = QPushButton('Establecer', clicked=self.setid)
        self.id = QLineEdit()

        # style
        self.gbutton.setStyleSheet(style.button)
        self.exitbutton.setStyleSheet(style.button)
        self.id.setStyleSheet(style.lineedit)
        self.set.setStyleSheet(style.button)

        ly = QGridLayout()
        ly.addWidget(qchar, 0, 0)
        ly.addWidget(self.qchar, 0, 1)
        ly.addWidget(self.id, 1, 0, 1, 2)
        ly.addWidget(self.gbutton, 2, 0)
        ly.addWidget(self.exitbutton, 2, 1)
        ly.addWidget(self.set, 3, 0)
        self.setStyleSheet('background:rgb(211, 211, 211)')
        self.setLayout(ly)
        self.setWindowTitle('Generador de ID')
        self.setWindowIcon(QIcon('id.png'))

    def closethis(self):
        qApp.quit()

    def getlong(self):
        longitud = self.qchar.value()
        return longitud

    def gennum(self):
        word = ''
        for i in range(self.getlong()):
            n = choice(self.numbers)
            word += n
        return word

    def genlet(self):
        word = ''
        num = self.getlong()

        for i in range(int(num)):
            x = choice(self.numbers)
            y = choice(self.letters)
            char = choice([x, y])
            word += char
        return word

    def gen(self):
        n = choice([1, 2])
        if n == 1:
            code = self.gennum()
        else:
            code = self.genlet()
        return code

    def actid(self):
        self.id.setText(self.gen())

    def setid(self):
        lines = []
        try:
            with open('./teknogods.ini') as h:
                for line in h.readlines():
                    lines.append(line)
            lines[2] = 'ID={0}\n'.format(self.id.text())
            with open('./teknogods.ini', 'w') as t:
                for i in lines:
                    t.write(i)
            QMessageBox.information(self, 'Listo', 'Listo')
        except:
            QMessageBox.information(self, 'Error', 'Por favor asegurese de que el programa esta en la carpeta del juego')
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = IDGen()
    ex.show()
    sys.exit(app.exec_())
