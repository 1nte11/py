from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
# Command: python -m PyQt5.uic.pyuic -x qtPractice.ui -o qtPractice.py

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FANJARA")
        self.setWindowIcon(QIcon(("./logo192.png")))
        self.setFixedHeight(400)
        self.setFixedWidth(400)
        self.setGeometry(200,200,200,200)
        self.setStyleSheet('background-color: green')

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())