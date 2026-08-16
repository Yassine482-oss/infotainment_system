from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QTimer, QDateTime
import requests
from Music import MusicWindow
from Map import MapWindow
from Message import MessageWindow
from About import AboutWindow
from dotenv import load_dotenv
import os
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Infotainment System')
        self.setFixedSize(1024, 600)
        container=QWidget()
        layout=QVBoxLayout(container)
        welcome=QLabel('Welcome to Infotainment System developped by YL')
        welcome.setAlignment(Qt.AlignCenter)
        welcome.setStyleSheet("font-size: 26px; font-weight : bold;")
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 22px;")
        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("font-size: 18px;")
        self.weather_label=QLabel("🌡️ Temperature : -- °C")
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.weather_label.setStyleSheet("font-size: 18px;")
        layout.addStretch()
        layout.addWidget(welcome)
        layout.addSpacing(20)
        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)
        layout.addSpacing(10)
        layout.addWidget(self.weather_label)
        layout.addStretch()
        self.setCentralWidget(container)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)
        self.update_datetime()
        self.weather_timer=QTimer(self)
        self.weather_timer.timeout.connect(self.update_weather)
        self.timer.start(60000)
        self.update_weather()
        self.music_window = MusicWindow()
        self.map_window = MapWindow()
        self.message_window = MessageWindow()
        self.about_window=AboutWindow()
        menubar = self.menuBar()
        aboutMenu = menubar.addMenu('About')
        musicMenu=menubar.addMenu('Music')
        mapMenu = menubar.addMenu('Map')
        messageMenu=menubar.addMenu('Message')
        exitMenu=menubar.addMenu('Exit')
        aboutAction=aboutMenu.addAction('about')
        aboutAction.triggered.connect(self.openAbout)
        musicAction=musicMenu.addAction('Music')
        musicAction.triggered.connect(self.openMusic)
        mapAction=mapMenu.addAction('Map')
        mapAction.triggered.connect(self.openMap)
        messageAction=messageMenu.addAction('Messages')
        messageAction.triggered.connect(self.openMessage)
        exitAction=exitMenu.addAction('Exit')
        exitAction.triggered.connect(self.close)
    def update_datetime(self):
        current=QDateTime.currentDateTime()
        self.time_label.setText(current.toString("HH:mm:ss"))
        self.date_label.setText(current.toString('dddd dd MMMM yyyy'))
    def openMusic(self):
        self.music_window.show()
        self.music_window.raise_()
        self.music_window.activateWindow()
    def openMap(self):
        self.map_window.show()
        self.map_window.raise_()
        self.map_window.activateWindow()
    def openMessage(self):
        self.message_window.show()
        self.message_window.raise_()
        self.message_window.activateWindow()
    def openAbout(self):
        self.about_window.show()
        self.about_window.raise_()
        self.about_window.activateWindow()
    def update_weather(self):
        load_dotenv()
        API_KEY=os.getenv("API_key")
        City=os.getenv("CITY")
        URL=f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}&units=metric"
        try:
            response=requests.get(URL,timeout=5)
            data=response.json()
            temperature = data["main"]["temp"]
            self.weather_label.setText(f"🌡️ Température : {temperature} °C")
        except Exception:
            self.weather_label.setText("Temperature : unavailable")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
