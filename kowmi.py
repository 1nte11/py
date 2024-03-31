import random as rd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

#python -m PyQt5.uic.pyuic -x qtPractice.ui -o qtPractice.py

Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]

class Ui_Form(QMainWindow):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 397)
        Form.setStyleSheet("QWidget {\n"
"background-color:#d4ffeb\n"
"}")
        self.RectBtn = QtWidgets.QPushButton(Form)
        self.RectBtn.setGeometry(QtCore.QRect(210, 110, 81, 51))
        self.RectBtn.setStyleSheet("QWidget {\n"
"background-color:rgb(170, 170, 255)\n"
"}")
        self.RectBtn.setObjectName("RectBtn")
        self.TrapBtn = QtWidgets.QPushButton(Form)
        self.TrapBtn.setGeometry(QtCore.QRect(120, 110, 81, 51))
        self.TrapBtn.setStyleSheet("QWidget {\n"
"background-color:rgb(170, 170, 255)\n"
"}")
        self.TrapBtn.setObjectName("TrapBtn")
        self.SqBtn = QtWidgets.QPushButton(Form)
        self.SqBtn.setGeometry(QtCore.QRect(300, 110, 91, 51))
        self.SqBtn.setStyleSheet("QWidget {\n"
"background-color:rgb(170, 170, 255)\n"
"}")
        self.SqBtn.setObjectName("SqBtn")
        self.TrapArea = QtWidgets.QPushButton(Form)
        self.TrapArea.setGeometry(QtCore.QRect(470, 80, 91, 31))
        self.TrapArea.setStyleSheet("QWidget {\n"
"background-color:rgb(170, 170, 255)\n"
"}")
        self.TrapArea.setObjectName("TrapArea")
        self.RectArea = QtWidgets.QPushButton(Form)
        self.RectArea.setGeometry(QtCore.QRect(470, 120, 91, 31))
        self.RectArea.setStyleSheet("QWidget {\n"
"background-color:rgb(170, 170, 255)\n"
"}")
        self.RectArea.setObjectName("RectArea")
        self.SqArea = QtWidgets.QPushButton(Form)
        self.SqArea.setGeometry(QtCore.QRect(470, 160, 91, 31))
        self.SqArea.setStyleSheet("QWidget {\n"
"background-color:rgb(170, 170, 255)\n"
"}")
        self.SqArea.setObjectName("SqArea")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        ###
        self.label = QtWidgets.QLabel(Form)  # Define the label
        self.label.setGeometry(QtCore.QRect(20, 20, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Peikari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_area = QtWidgets.QLabel(Form) #for area
        self.label_area.setGeometry(QtCore.QRect(150, 300, 300, 100))
        font = QtGui.QFont()
        font.setFamily("Peikari")
        font.setPointSize(16)
        self.label_area.setFont(font)
        self.label_area.setObjectName("label_area")

        self.SqArea.setObjectName("SqArea")
        self.photo = QtWidgets.QLabel(Form)
        self.photo.setGeometry(QtCore.QRect(210, 220, 121, 91))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap(""))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

    
    def trapBtn(self, trapezoids):
        text = ""

        for trapezoid in trapezoids:
            text += str(trapezoid) + "\n"
        self.label.setText(text)

        self.update()

    def rectBtn(self, rectangles):
        text = ""
        for rectangle in rectangles:
            text += str(rectangle) + "\n"
        self.label.setText(text)
        self.update()

    def sqBtn(self, squares):
        text = ""
        for square in squares:
            text += str(square) + "\n"
        self.label.setText(text)
        self.update()
    
    def trapArea(self, trap):
        text = 'Area of Trapezoid is ' + str(trap.area())  # Added space after "is"
        self.label_area.setText(text)
        self.photo.setPixmap(QtGui.QPixmap("trap.png"))
        self.update()
        
    def rectArea(self, rect):
        text = 'Area of Rectangle is ' + str(rect.area())  # Added space after "is"
        self.label_area.setText(text)
        self.photo.setPixmap(QtGui.QPixmap("rect.png"))
        self.update()

    def sqArea(self, square):
        text = 'Area of Square is ' + str(square.area())  # Changed "Trapezoid" to "Square"
        self.label_area.setText(text)
        self.photo.setPixmap(QtGui.QPixmap("square.png"))
        self.update()

    def update(self):
        self.label.adjustSize()
    #-----------------------------------------------------------
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.RectBtn.setText(_translate("Form", "Rectangle"))
        self.TrapBtn.setText(_translate("Form", "Trapezoid"))
        self.SqBtn.setText(_translate("Form", "Square"))
        self.TrapArea.setText(_translate("Form", "Trapezoid Area"))
        self.RectArea.setText(_translate("Form", "Rectangle Area"))
        self.SqArea.setText(_translate("Form", "Square Area"))

class Trapezoid(object):
    def __init__(self, a, b, height):
        self.a = a # ფუძე
        self.b = b
        self.height = height
    
    def __str__(self):
        return 'Trapezoid has {} cm a, {} cm b and {} cm height'.format(self.a, self.b, self.height)
    
    def area(self):
        self.s = (self.a + self.b) * (self.height / 2)
        return self.s
    
    def __gt__(self, other):
        if self.area() > other.area():
            return True
        return False
    
    def __lt__(self, other):
        if self.area() < other.area():
            return True
        return False
    
    def __eq__(self, other):
        if self.area() == other.area():
            return "Both are Eqaul"
        return "Not equal"
    


class Rectangle(Trapezoid):
    def __init__(self, a, b):
        super().__init__(a, b, 0)

    def area(self):
        self.s = self.a * self.b
        return self.s
    
    def __str__(self):
        return 'Rectangle has {} cm width and {} cm height'.format(self.a, self.b)

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, 0)
    
    def area(self):
        self.s = self.a ** 2
        return self.s
    
    def __str__(self):
        return 'Square has {} cm width and height'.format(self.a)
    
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()

        t1 = Trapezoid(3, 5, 8)
        t2 = Trapezoid(2, 5, 6)

        r1 = Rectangle(2, 10)
        r2 = Rectangle(3, 8)

        s1 = Square(5)

        trapezoids = [t1, t2]
        rectangles = [r1, r2]
        squares = [s1]

        ui.TrapBtn.clicked.connect(lambda: ui.trapBtn([t1]))
        ui.RectBtn.clicked.connect(lambda: ui.rectBtn([r2]))
        ui.SqBtn.clicked.connect(lambda: ui.sqBtn([s1]))

        ui.TrapArea.clicked.connect(lambda: ui.trapArea(t1))  
        ui.RectArea.clicked.connect(lambda: ui.rectArea(r1)) 
        ui.SqArea.clicked.connect(lambda: ui.sqArea(s1)) 

        sys.exit(app.exec_())

