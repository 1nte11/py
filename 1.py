import random as rd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(20, 10, 441, 231))
        self.picture_label.setFrameShape(QtWidgets.QFrame.Box)
        self.picture_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_label.setText("")
        self.picture_label.setPixmap(QtGui.QPixmap("trapecia.jpg"))
        self.picture_label.setScaledContents(True)
        self.picture_label.setObjectName("picture_label")
        
        self.answer_label = QtWidgets.QLabel(self.centralwidget)
        self.answer_label.setGeometry(QtCore.QRect(20, 250, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.answer_label.setFont(font)
        self.answer_label.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.answer_label.setFrameShape(QtWidgets.QFrame.Box)
        self.answer_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.answer_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.answer_label.setObjectName("answer_label")
        
        self.trp_area = QtWidgets.QPushButton(self.centralwidget)
        self.trp_area.setGeometry(QtCore.QRect(20, 330, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trp_area.setFont(font)
        self.trp_area.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.trp_area.setObjectName("trp_area")
        
        
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(130, 470, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close.setFont(font)
        self.close.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.close.setObjectName("close")
        
        self.mrt_area = QtWidgets.QPushButton(self.centralwidget)
        self.mrt_area.setGeometry(QtCore.QRect(160, 330, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mrt_area.setFont(font)
        self.mrt_area.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.mrt_area.setObjectName("mrt_area")
        
        self.kvt_area = QtWidgets.QPushButton(self.centralwidget)
        self.kvt_area.setGeometry(QtCore.QRect(330, 330, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kvt_area.setFont(font)
        self.kvt_area.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.kvt_area.setObjectName("kvt_area")
        
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(50, 400, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet("border-color: rgb(186, 186, 186);")
        self.clear_button.setObjectName("clear_button")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 21))
        self.menubar.setObjectName("menubar")
        self.menuChoose_Figure = QtWidgets.QMenu(self.menubar)
        self.menuChoose_Figure.setObjectName("menuChoose_Figure")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.Trapecia = QtWidgets.QAction(MainWindow)
        self.Trapecia.setObjectName("Trapecia")
        self.Martkutxedi = QtWidgets.QAction(MainWindow)
        self.Martkutxedi.setObjectName("Martkutxedi")
        self.Kvadrati = QtWidgets.QAction(MainWindow)
        self.Kvadrati.setObjectName("Kvadrati")
        
        self.menuChoose_Figure.addAction(self.Trapecia)
        self.menuChoose_Figure.addAction(self.Martkutxedi)
        self.menuChoose_Figure.addAction(self.Kvadrati)
        self.menubar.addAction(self.menuChoose_Figure.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # call pictures:
        self.Trapecia.triggered.connect(lambda: self.show_trapezoid())
        self.Martkutxedi.triggered.connect(lambda: self.show_rectangle())
        self.Kvadrati.triggered.connect(lambda: self.show_square())

        # call button functions:
        self.trp_area.clicked.connect(lambda: self.T(Digit_list[0]))
        self.mrt_area.clicked.connect(lambda: self.M(Digit_list[0]))
        self.kvt_area.clicked.connect(lambda: self.K(Digit_list[0]))
        self.clear_button.clicked.connect(self.Remove)
        self.close.clicked.connect(MainWindow.close)

    # define show_figures function:
    def show_trapezoid(self):
        self.picture_label.setPixmap(QtGui.QPixmap("./trapecia.jpeg"))

    def show_rectangle(self):
        self.picture_label.setPixmap(QtGui.QPixmap("./martkutxedi.png"))

    def show_square(self):
        self.picture_label.setPixmap(QtGui.QPixmap("./square.png"))

    # choose which figures area should be shown:
    def T(self, digit):
        trp_1 = Trapecia(digit)
        self.answer_label.setText(f'Area Of Trapezoid: {trp_1.t_fartobi()} m\u00b2')

    def M(self, digit):
        mrt_1 = Martkutxedi(digit)
        self.answer_label.setText(f'Area Of Rectangle: {mrt_1.m_fartobi()} m\u00b2')

    def K(self, digit):
        kvt_1 = Kvadrati(digit)
        self.answer_label.setText(f'Area Of Square: {kvt_1.k_fartobi()} m\u00b2')

    # define function for Clear Button:
    def Remove(self):
        self.answer_label.setText("0")
        self.picture_label.setPixmap(QtGui.QPixmap(""))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.answer_label.setText(_translate("MainWindow", "0"))
        self.trp_area.setText(_translate("MainWindow", "Trapezoid"))
        self.close.setText(_translate("MainWindow", "CLOSE APP"))
        self.mrt_area.setText(_translate("MainWindow", "Rectangle"))
        self.kvt_area.setText(_translate("MainWindow", "Square"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.menuChoose_Figure.setTitle(_translate("MainWindow", "Choose Figure"))
        self.Trapecia.setText(_translate("MainWindow", "Trapecia"))
        self.Martkutxedi.setText(_translate("MainWindow", "Martkutxedi"))
        self.Kvadrati.setText(_translate("MainWindow", "Kvadrati"))

# ------------------------------------------------ SECOND PART ------------------------------------------ #
Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]

class Trapecia:
    def __init__(self, digit):
        self.fudze1 = digit[0]
        self.fudze2 = digit[1]
        self.simagle = digit[2]

    def __str__(self):
        return str(self.fudze1) + ", " + str(self.fudze2) + ", " + str(self.simagle)

    def t_fartobi(self):
        return (self.fudze1 + self.fudze2) / 2 * self.simagle

class Martkutxedi:
    def __init__(self, digit):
        self.fudze1 = digit[0]
        self.fudze2 = digit[1]

    def __str__(self):
        return str(self.fudze1) + ", " + str(self.fudze2)

    def m_fartobi(self):
        return self.fudze1 * self.fudze2

class Kvadrati:
    def __init__(self, digit):
        self.fudze1 = digit[0]

    def __str__(self):
        return str(self.fudze1)

    def k_fartobi(self):
        return self.fudze1 ** 2

# ------------------------------------------------ LAST PART ------------------------------------------ #

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
