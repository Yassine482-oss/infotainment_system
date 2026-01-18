from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setFixedSize(1024, 600)
        label = QLabel(self)
        pixmap = QPixmap("assets/about.jpeg")
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)
        label.setScaledContents(True)
        self.setCentralWidget(label)
