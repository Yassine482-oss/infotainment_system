from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import QUrl

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map")
        self.setFixedSize(1024, 600)
        view = QQuickWidget()
        view.setSource(QUrl.fromLocalFile("map.qml"))
        view.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.setCentralWidget(view)
