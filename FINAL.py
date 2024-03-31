import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys

dimensions_list = [[random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)] for _ in range(10)]

class Ui_Form(QMainWindow):
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setStyleSheet("QWidget {""background-color:green""}")

        self.TrapBtn = QtWidgets.QPushButton(Form)
        self.TrapBtn.setObjectName("TrapBtn")
        self.TrapBtn.setGeometry(QtCore.QRect(220, 120, 80, 40))
        self.TrapBtn.setStyleSheet("QWidget {""background-color:red""}")
        

        self.RectBtn = QtWidgets.QPushButton(Form)
        self.RectBtn.setObjectName("RectBtn")
        self.RectBtn.setGeometry(QtCore.QRect(310, 120, 80, 40))
        self.RectBtn.setStyleSheet("QWidget {""background-color:yellow""}")
        

        self.SqBtn = QtWidgets.QPushButton(Form)
        self.SqBtn.setObjectName("SqBtn")
        self.SqBtn.setGeometry(QtCore.QRect(400, 120, 90, 40))
        self.SqBtn.setStyleSheet("QWidget {""background-color:blue""}")
        

        self.TrapArea = QtWidgets.QPushButton(Form)
        self.TrapArea.setGeometry(QtCore.QRect(70, 195, 125, 31))
        self.TrapArea.setStyleSheet("QWidget {""background-color:red""}")
        self.TrapArea.setObjectName("TrapArea")

        self.RectArea = QtWidgets.QPushButton(Form)
        self.RectArea.setGeometry(QtCore.QRect(70, 230, 125, 31))
        self.RectArea.setStyleSheet("QWidget {""background-color:yellow""}")
        self.RectArea.setObjectName("RectArea")

        self.SqArea = QtWidgets.QPushButton(Form)
        self.SqArea.setGeometry(QtCore.QRect(70, 265, 125, 31))
        self.SqArea.setStyleSheet("QWidget {""background-color:blue""}")
        self.SqArea.setObjectName("SqArea")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label = QtWidgets.QLabel(Form) 
        self.label.setGeometry(QtCore.QRect(20, 20, 400, 50))
        font = QtGui.QFont()
        
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_area = QtWidgets.QLabel(Form) 
        self.label_area.setGeometry(QtCore.QRect(300, 300, 300, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_area.setFont(font)
        self.label_area.setObjectName("label_area")

        self.picture = QtWidgets.QLabel(Form)
        self.picture.setGeometry(QtCore.QRect(290, 220, 121, 91))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap(""))
        self.picture.setScaledContents(True)
        self.picture.setObjectName("picture")

    
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
        message = f'S(trap)={trap.calculate_area()}'
        self.label_area.setText(message)
        self.picture.setPixmap(QtGui.QPixmap("trapecia.jpeg"))
        self.update()
        
    def rectArea(self, rect):
        message = f'S(rect)={rect.calculate_area()}'
        self.label_area.setText(message)
        self.picture.setPixmap(QtGui.QPixmap("martkutxedi.png"))
        self.update()

    def sqArea(self, square):
        message = f'S(sqr)={square.calculate_area()}'
        self.label_area.setText(message)
        self.picture.setPixmap(QtGui.QPixmap("square.png"))
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

class Trapezoid:
    def __init__(self, base_top, base_bottom, height):
        self.base_top = base_top
        self.base_bottom = base_bottom
        self.height = height
    
    def __str__(self):
        return 'Trapezoid dimensions: {}cm X {}cm X {}cm'.format(self.base_top, self.base_bottom, self.height)
    
    def calculate_area(self):
        area = (self.base_top + self.base_bottom) * (self.height / 2)
        return area
    
    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()
    
    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()
    
    def __eq__(self, other):
        return self.calculate_area() == other.calculate_area()


class Rectangle(Trapezoid):
    def __init__(self, width, length):
        super().__init__(width, length, 0)

    def calculate_area(self):
        area = self.base_top * self.base_bottom
        return area
    
    def __str__(self):
        return 'Rectangle dimensions: {}cm X {}cm'.format(self.base_top, self.base_bottom)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def calculate_area(self):
        area = self.base_top ** 2
        return area
    
    def __str__(self):
        return 'Square dimensions: {}cm X {}cm'.format(self.base_top, self.base_top)


    
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
