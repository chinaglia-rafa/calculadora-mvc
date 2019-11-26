from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from PyQt5.QtWidgets import QApplication
from view.CalculadoraView import CalculadoraView
from model.Calculadora import Calculadora


class CalculadoraController():

    DEBUG = True

    def __init__(self):
        self.__app = QApplication([])

        self.__model = Calculadora()
        self.__view = CalculadoraView()

        self.timer = None

        self.__view.buttonClick.connect(self.clicked)

    def init(self):
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: None)
        self.timer.start(100)

        self.__view.show()
        self.__app.exec_()

    def debug(self, *text):
        if (self.DEBUG):
            for item in text:
                print(item, end=' ')
            print("")

    def clicked(self):
        text = self.__view.getInputValue()
        self.debug("String atual", text)

        postFixed = self.__model.parse(text)
