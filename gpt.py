import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys

Digit_list = [[random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)] for i in range(10)]

class Ui_Form(QMainWindow):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setStyleSheet("QWidget {""background-color:green""}")

        self.TrapBtn = QtWidgets.QPushButton(Form)
        self.TrapBtn.setObjectName("TrapBtn")
        self.TrapBtn.setGeometry(QtCore.QRect(310, 120, 80, 50))
        self.TrapBtn.setStyleSheet("QWidget {""background-color:red""}")
        

        self.RectBtn = QtWidgets.QPushButton(Form)
        self.RectBtn.setObjectName("RectBtn")
        self.RectBtn.setGeometry(QtCore.QRect(220, 120, 80, 50))
        self.RectBtn.setStyleSheet("QWidget {""background-color:red""}")
        

        self.SqBtn = QtWidgets.QPushButton(Form)
        self.SqBtn.setObjectName("SqBtn")
        self.SqBtn.setGeometry(QtCore.QRect(400, 120, 90, 50))
        self.SqBtn.setStyleSheet("QWidget {""background-color:red""}")
        

        self.TrapArea = QtWidgets.QPushButton(Form)
        self.TrapArea.setGeometry(QtCore.QRect(70, 195, 125, 31))
        self.TrapArea.setStyleSheet("QWidget {""background-color:yellow""}")
        self.TrapArea.setObjectName("TrapArea")

        self.RectArea = QtWidgets.QPushButton(Form)
        self.RectArea.setGeometry(QtCore.QRect(70, 230, 125, 31))
        self.RectArea.setStyleSheet("QWidget {""background-color:yellow""}")
        self.RectArea.setObjectName("RectArea")

        self.SqArea = QtWidgets.QPushButton(Form)
        self.SqArea.setGeometry(QtCore.QRect(70, 265, 125, 31))
        self.SqArea.setStyleSheet("QWidget {""background-color:yellow""}")
        self.SqArea.setObjectName("SqArea")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label = QtWidgets.QLabel(Form) 
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

    
    def TrapezoidBtn(self, trapezoids):
        text = ""

        for trapezoid in trapezoids:
            text += str(trapezoid) + "\n"
        self.label.setText(text)

        self.update()

    def RectangleBtn(self, rectangles):
        text = ""
        for rectangle in rectangles:
            text += str(rectangle) + "\n"
        self.label.setText(text)
        self.update()

    def SquareBtn(self, squares):
        text = ""
        for square in squares:
            text += str(square) + "\n"
        self.label.setText(text)
        self.update()
    
    def trapArea(self, trap):
        message = f'S(trap)={trap.area()}'
        self.label_area.setText(message)
        self.photo.setPixmap(QtGui.QPixmap("trapecia.jpeg"))
        self.update()
        
    def rectArea(self, rect):
        message = f'S(rect)={rect.area()}'
        self.label_area.setText(message)
        self.photo.setPixmap(QtGui.QPixmap("martkutxedi.png"))
        self.update()

    def sqArea(self, square):
        message = f'S(sqr)={square.area()}'
        self.label_area.setText(message)
        self.photo.setPixmap(QtGui.QPixmap("square.png"))
        self.update()

    def update(self):
        self.label.adjustSize()
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FormArea"))
        self.RectBtn.setText(_translate("Form", "Rectangle"))
        self.TrapBtn.setText(_translate("Form", "Trapezoid"))
        self.SqBtn.setText(_translate("Form", "Square"))
        self.TrapArea.setText(_translate("Form", "Area of Trapezoid"))
        self.RectArea.setText(_translate("Form", " Area of Rectangle"))
        self.SqArea.setText(_translate("Form", "Area of Square"))

class Trapezoid(object):
    def __init__(self, a, b, h):
        self.a = a 
        self.b = b
        self.h = h
    
    def __str__(self):
        return 'Trapezoid dementions: {}cm X {}cm X {}cm'.format(self.a, self.b, self.h)
    
    def area(self):
        self.s = (self.a + self.b) * (self.h / 2)
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
        if self.area() != other.area():
            return "NoT Eqaul"
        return "Equal"
    


class Rectangle(Trapezoid):
    def __init__(self, a, b):
        super().__init__(a, b, 0)

    def area(self):
        self.s = self.a * self.b
        return self.s
    
    def __str__(self):
        return 'Rectangle dementions: {}cm X {}cm '.format(self.a, self.b)

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, 0)
    
    def area(self):
        self.s = self.a ** 2
        return self.s
    
    def __str__(self):
        return 'Square dementions: {}cm'.format(self.a,self.a,self.a)
    
    
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()

        trap1 = Trapezoid(6, 10, 16)
        trap2 = Trapezoid(6, 15, 18)
        rect1 = Rectangle(3, 10)
        rect2 = Rectangle(5, 6)
        square1 = Square(8)
        square2 = Square(6)

        ui.TrapArea.clicked.connect(lambda: ui.trapArea(trap1))  
        ui.RectArea.clicked.connect(lambda: ui.rectArea(rect1)) 
        ui.SqArea.clicked.connect(lambda: ui.sqArea(square1)) 

        trapezoids = [trap1, trap2]
        rectangles = [rect1, rect2]
        squares = [square1, square2]


        ui.TrapBtn.clicked.connect(lambda: ui.TrapezoidBtn([trap1]))
        ui.RectBtn.clicked.connect(lambda: ui.RectangleBtn([rect2]))
        ui.SqBtn.clicked.connect(lambda: ui.SquareBtn([square1]))


        sys.exit(app.exec_())
