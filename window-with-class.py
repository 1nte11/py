from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())