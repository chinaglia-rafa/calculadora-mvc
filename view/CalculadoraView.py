from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class CalculadoraView(QtWidgets.QWidget):

    buttonClick = QtCore.pyqtSignal()

    def __init__(self):
        super(CalculadoraView, self).__init__()

        self.__text = None
        self.__button = None

        self.initUi()

    def initUi(self):
        lay = QtWidgets.QVBoxLayout(self)
        title = QtWidgets.QLabel("<b>O QUE DESEJA CALCULAR?</b>")
        lay.addWidget(title, alignment=QtCore.Qt.AlignHCenter)

        fwidget = QtWidgets.QWidget()
        flay = QtWidgets.QFormLayout(fwidget)
        self.__text = QtWidgets.QLineEdit(placeholderText='10 - ( 7 - 2 ) / 2', text='10 - ( 7 - 2 ) / 2')
        self.__button = QtWidgets.QPushButton('Calcular!')
        self.__button.clicked.connect(self.buttonClick)

        flay.addRow(self.__text)
        flay.addRow(self.__button)

        lay.addWidget(fwidget, alignment=QtCore.Qt.AlignHCenter)
        lay.addStretch()

    def clear(self):
        self.usernameInput.clear()
        self.passwordInput.clear()

    def showMessage(self):
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText("your credentials are valid\n Welcome")
        messageBox.exec_()
        self.close()

    def showError(self):
        messageBox = QtWidgets.QMessageBox(self)
        messageBox.setText("your credentials are not valid\nTry again...")
        messageBox.setIcon(QtWidgets.QMessageBox.Critical)
        messageBox.exec_()

    def getInputValue(self):
        return self.__text.text()
