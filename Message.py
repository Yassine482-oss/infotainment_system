from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class MessageWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Message')
        self.setFixedSize(1024, 600)
        container=QWidget()
        self.setCentralWidget(container)
        layout=QVBoxLayout(container)
        label1=QLabel('thank you for your visit')
        label1.setAlignment(Qt.AlignCenter)
        label2 = QLabel('No updates for the moment')
        label2.setAlignment(Qt.AlignCenter)
        label3=QLabel("Don't hesitate to check from time to time")
        label3.setAlignment(Qt.AlignCenter)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
