from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('player.png'))

        p =self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.init_ui()


        self.show()


    def init_ui(self):

        #create media player object
        self.mediaPlayer1 = QMediaPlayer(None, QMediaPlayer.VideoSurface)


        #create videowidget object

        videowidget1 = QVideoWidget()


        #create open button
        openBtn1 = QPushButton('Open Video')
        openBtn1.clicked.connect(lambda: self.open_file(self.mediaPlayer1, self.playBtn1))



        #create button for playing
        self.playBtn1 = QPushButton()
        self.playBtn1.setEnabled(False)
        self.playBtn1.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn1.clicked.connect(lambda: self.play_video(self.mediaPlayer1))




        #create slider
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(0, 0)
        self.slider1.sliderMoved.connect(self.set_position1)


        self.is_video_transformed = False

        #create label
        self.label1 = QLabel()
        self.label1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        self.filename = ''

        #create hbox layout
        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setContentsMargins(0, 0, 0, 0)

        #set widgets to the hbox layout
        self.hboxLayout1.addWidget(openBtn1)
        self.hboxLayout1.addWidget(self.playBtn1)
        self.hboxLayout1.addWidget(self.slider1)



        #create vbox layout
        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.addWidget(videowidget1)
        self.vboxLayout1.addLayout(self.hboxLayout1)
        self.vboxLayout1.addWidget(self.label1)

        self.newLayout = QVBoxLayout()
        self.newLayout.addLayout(self.vboxLayout1)

        self.bigBtn = QPushButton()
        self.bigBtn.setText('TO DO SmThing with videofile')
        self.bigBtn.setEnabled(False)
        self.bigBtn.clicked.connect(self.do_smthing_with_videofile)

        self.newLayout.addWidget(self.bigBtn)

        self.setLayout(self.newLayout)

        self.mediaPlayer1.setVideoOutput(videowidget1)


        #media player signals

        self.mediaPlayer1.stateChanged.connect(lambda: self.mediastate_changed(self.mediaPlayer1, self.playBtn1))
        self.mediaPlayer1.positionChanged.connect(self.position_changed1)
        self.mediaPlayer1.durationChanged.connect(self.duration_changed1)


    def open_file(self, player, btn):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if self.filename != '':
            player.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            btn.setEnabled(True)
            self.bigBtn.setEnabled(True)
    def play_video(self, player):
        if player.state() == QMediaPlayer.PlayingState:
            player.pause()

        else:
            player.play()

    def mediastate_changed(self, player, btn):
        if player.state() == QMediaPlayer.PlayingState:
            btn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )
        else:
            btn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )

    def position_changed1(self, position):
        self.slider1.setValue(position)
    def position_changed2(self, position):
        self.slider2.setValue(position)


    def duration_changed1(self, duration):
        self.slider1.setRange(0, duration)
    def duration_changed2(self, duration):
        self.slider2.setRange(0, duration)

    def set_position1(self, position):
        self.mediaPlayer1.setPosition(position)
    def set_position2(self, position):
        self.mediaPlayer2.setPosition(position)


    def handle_errors1(self):
        self.playBtn1.setEnabled(False)
        self.label1.setText("Error: " + self.mediaPlayer1.errorString())
    def handle_errors2(self):
        self.playBtn2.setEnabled(False)
        self.label2.setText("Error: " + self.mediaPlayer2.errorString())

    def do_smthing_with_videofile(self):
        if self.is_video_transformed == False:
            self.is_video_transformed = True
            self.mediaPlayer2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)
            videowidget2 = QVideoWidget()
            self.playBtn2 = QPushButton()
            self.playBtn2.setEnabled(False)
            self.playBtn2.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.playBtn2.clicked.connect(lambda: self.play_video(self.mediaPlayer2))
            self.slider2 = QSlider(Qt.Horizontal)
            self.slider2.setRange(0, 0)
            self.slider2.sliderMoved.connect(self.set_position2)
            self.label2 = QLabel()
            self.label2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
            self.hboxLayout2 = QHBoxLayout()
            self.hboxLayout2.setContentsMargins(0, 0, 0, 0)
            self.hboxLayout2.addWidget(self.playBtn2)
            self.hboxLayout2.addWidget(self.slider2)
            self.vboxLayout2 = QVBoxLayout()
            self.vboxLayout2.addWidget(videowidget2)
            self.vboxLayout2.addLayout(self.hboxLayout2)
            self.vboxLayout2.addWidget(self.label2)
            self.newLayout.addLayout(self.vboxLayout2)
            self.mediaPlayer2.setVideoOutput(videowidget2)
            self.mediaPlayer2.stateChanged.connect(lambda: self.mediastate_changed(self.mediaPlayer2, self.playBtn2))
            self.mediaPlayer2.positionChanged.connect(self.position_changed2)
            self.mediaPlayer2.durationChanged.connect(self.duration_changed2)
            self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            self.playBtn2.setEnabled(True)
        else:
            self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(self.filename)))
            self.playBtn2.setEnabled(True)



app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
