import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QSlider
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


class MusicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music')
        self.setFixedSize(1024, 600)
        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)

        self.music_dir = "music"
        self.playlist = [
            os.path.join(self.music_dir, f)
            for f in os.listdir(self.music_dir)
            if f.endswith(".mp3")
        ]
        self.current_index = 0
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)

        label = QLabel('Music')
        label.setAlignment(Qt.AlignCenter)

        self.slider_music = QSlider(Qt.Horizontal)
        self.slider_music.setRange(0, 100)
        inner_container = QWidget()
        inner_layout = QHBoxLayout(inner_container)
        self.button_prev = QPushButton('<<')
        self.button_play = QPushButton('Play/Pause')
        self.button_next = QPushButton('>>')
        inner_layout.addWidget(self.button_prev)
        inner_layout.addWidget(self.button_play)
        inner_layout.addWidget(self.button_next)

        son_container = QWidget()
        son_layout = QVBoxLayout(son_container)
        self.slider_volume = QSlider(Qt.Horizontal)
        self.slider_volume.setRange(0, 100)
        self.slider_volume.setValue(50)
        self.audio_output.setVolume(0.5)
        label2 = QLabel('soundbar')
        son_layout.addWidget(self.slider_volume)
        son_layout.addWidget(label2)
        layout.addWidget(label)
        layout.addWidget(self.slider_music)
        layout.addWidget(inner_container)
        layout.addWidget(son_container)

        # =====================
        # 🔗 CONNEXIONS
        # =====================
        self.button_play.clicked.connect(self.play_pause)
        self.button_next.clicked.connect(self.next_music)
        self.button_prev.clicked.connect(self.previous_music)

        self.slider_volume.valueChanged.connect(
            lambda v: self.audio_output.setVolume(v / 100)
        )

        self.player.positionChanged.connect(self.slider_music.setValue)
        self.player.durationChanged.connect(self.slider_music.setMaximum)
        self.slider_music.sliderMoved.connect(self.player.setPosition)

    def load_current_music(self):
        if not self.playlist:
            return
        file_path = self.playlist[self.current_index]
        self.player.setSource(QUrl.fromLocalFile(file_path))

    def play_pause(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            if self.player.source().isEmpty():
                self.load_current_music()
            self.player.play()

    def next_music(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_current_music()
        self.player.play()

    def previous_music(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_current_music()
        self.player.play()