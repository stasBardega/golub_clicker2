from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys

app = QApplication(sys.argv)


window2_push_button = QPushButton()
window2_push_button.setFixedSize(150, 150)

window = QWidget()
window.setWindowTitle("Golub.clicker")
window.resize(800, 600)

menu_window = QWidget()
menu_window.setWindowTitle("Golub_clicker_menu")
menu_window.resize(800, 600)

window3 = QWidget()
window3.setWindowTitle("Golub_clicker2")
window3.resize(800, 600)

window_setting = QWidget()
window_setting.setWindowTitle("Golub_clicker_setting")
window_setting.resize(800, 600)

current_boost = 1

score1 = 0
score = QLabel()
score.setText(str(score1))


window3_push_button = QPushButton()
window3_push_button.setText("Наступна локація")
window3_sell = QPushButton()
window3_sell.setText("Ціна: 1м")




def on_media_status_changet(status):
     if status == QMediaPlayer.EndOfMedia:
          player.setPosition(0)
          player.play()


player = QMediaPlayer()
url = QUrl.fromLocalFile("music.mp3")
player.setMedia(QMediaContent(url))
player.play()
player.mediaStatusChanged.connect(on_media_status_changet)


setting = QPushButton()
setting.setText("Налаштування")
setting.setFixedSize(150, 150)



slider = QSlider()
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(50)




leave_setting = QPushButton()



name_of_game_menu = QLabel()
name_of_game_menu.setText("Golub clicker")



area = QPushButton()
area.setFixedSize(250, 250)

pixmap = QPixmap("images.jpg")
area.setIcon(QIcon(pixmap))
area.setIconSize(pixmap.size())
area.setStyleSheet("text-align: center;")


pixmap = QPixmap("play.jpg")
window2_push_button.setIcon(QIcon(pixmap))
window2_push_button.setIconSize(pixmap.size())
window2_push_button.setStyleSheet("text-align: center;")


window.setWindowIcon(QIcon("menu_image.jpg"))


upgrade_text = QLabel()
boost_text = QLabel()
boost_text.setText(f"Сила кліку: {current_boost}")
upgrade7_sell = QPushButton()
upgrade7_sell.setText("Ціна 35000")
upgrade7 = QPushButton()
upgrade7.setText("+100")
upgrade8_sell = QPushButton()
upgrade8_sell.setText("Ціна 70000")
upgrade8 = QPushButton()
upgrade8.setText("+250")
upgrade9_sell = QPushButton()
upgrade9_sell.setText("Ціна 150000")
upgrade9 = QPushButton()
upgrade9.setText("+500")
upgrade10_sell = QPushButton()
upgrade10_sell.setText("Ціна 500000")
upgrade10 = QPushButton()
upgrade10.setText("+1500")
upgrade6 = QPushButton()
upgrade6.setText("+50")
upgrade6_sell = QPushButton()
upgrade6_sell.setText("Ціна 15000")
upgrade_text.setText("UPGRADES")
upgrade2_sell = QPushButton()
upgrade2_sell.setText("Ціна: 500 кліків")
upgrade2 = QPushButton()
upgrade2.setText("+5")
upgrade3_sell = QPushButton()
upgrade3_sell.setText("Ціна: 1250 кліків")
upgrade3 = QPushButton()
upgrade3.setText("+10")
upgrade4 = QPushButton()
upgrade4_sell = QPushButton()
upgrade4_sell.setText("Ціна: 3000 кліків")
upgrade4.setText("+15")
upgrade5_sell = QPushButton()
upgrade5_sell.setText("Ціна: 7500 кліків")
upgrade5 = QPushButton()
upgrade5.setText("+25")
upgrade_sell = QPushButton()
upgrade_sell.setText("Ціна: 100 кліків")
upgrade = QPushButton()
upgrade.setText("+1")
button_leave = QPushButton()
button_leave.setText("Leave")


layout1 = QVBoxLayout()
layout3 = QVBoxLayout()
layout4 = QVBoxLayout()
layout5 = QVBoxLayout()
menu_layout = QVBoxLayout()
setting_layout = QVBoxLayout()

layout3.setSpacing(0)
layout3.setContentsMargins(0, 0, 0, 0)

layout5.setSpacing(0)
layout5.setContentsMargins(0, 0, 0, 0)

frame = QFrame()
frame_layout = QVBoxLayout()
frame_layout2 = QVBoxLayout()
frame_layout3 = QVBoxLayout()
frame_layout4 = QVBoxLayout()
frame_layout5 = QVBoxLayout()
frame_layout6 = QVBoxLayout()
frame_layout7 = QVBoxLayout()
frame_layout8 = QVBoxLayout()
frame_layout9 = QVBoxLayout()
frame_layout10 = QVBoxLayout()
frame_layout11 = QVBoxLayout()

frame_layout11.addWidget(window3_push_button)
frame_layout11.addWidget(window3_sell)

frame_layout10.addWidget(upgrade10)
frame_layout10.addWidget(upgrade10_sell)

frame_layout9.addWidget(upgrade9)
frame_layout9.addWidget(upgrade9_sell)

frame_layout8.addWidget(upgrade8)
frame_layout8.addWidget(upgrade8_sell)

frame_layout7.addWidget(upgrade7)
frame_layout7.addWidget(upgrade7_sell)

frame_layout6.addWidget(upgrade6)
frame_layout6.addWidget(upgrade6_sell)

frame_layout3.addWidget(upgrade)
frame_layout3.addWidget(upgrade_sell)

frame_layout4.addWidget(upgrade4)
frame_layout4.addWidget(upgrade4_sell)

frame_layout5.addWidget(upgrade5)
frame_layout5.addWidget(upgrade5_sell)

frame_layout2.addWidget(upgrade3)
frame_layout2.addWidget(upgrade3_sell)

frame_layout.addWidget(upgrade2)
frame_layout.addWidget(upgrade2_sell)

frame_layout.setSpacing(0)
frame_layout.setContentsMargins(0, 0, 0, 0)




layout1.addWidget(area)
layout1.addWidget(button_leave)




layout4.addWidget(boost_text)
layout4.addWidget(score)



menu_layout.addWidget(name_of_game_menu, alignment=Qt.AlignCenter)
menu_layout.addWidget(window2_push_button, alignment=Qt.AlignCenter)
menu_layout.addWidget(setting, alignment=Qt.AlignCenter)


setting_layout.addWidget(slider, alignment=Qt.AlignCenter)
setting_layout.addWidget(leave_setting)


layout2 = QHBoxLayout()



layout5.addLayout(frame_layout10)
layout5.addLayout(frame_layout9)
layout5.addLayout(frame_layout8)
layout5.addLayout(frame_layout7)
layout5.addLayout(frame_layout6)
layout3.addLayout(frame_layout)
layout3.addLayout(frame_layout2)
layout3.addLayout(frame_layout3)
layout3.addLayout(frame_layout4)
layout3.addLayout(frame_layout5)
layout4.addLayout(frame_layout11)
layout2.addLayout(layout1)
layout2.addLayout(layout3)
layout2.addLayout(layout5)
layout2.addLayout(layout4)




window.setLayout(layout2)
menu_window.setLayout(menu_layout)
window_setting.setLayout(setting_layout)






game_over = False




def setting_leave():
     window_setting.hide()
     window.hide()
     window3.hide()
     menu_window.show()

def music_editor(value):
     player.setVolume(value)


def setting_window():
     menu_window.hide()
     window.hide()
     window3.hide()
     window_setting.show()

def level2():
    global score1
    if score1 >= 1000000:
         menu_window.hide()
         window.hide()
         window3.show()

def start_game():
     menu_window.hide()
     window.show()

def leave():
    window.hide()
    menu_window.show()

def scoree():
    global score1
    score1 += current_boost
    score.setText(str(score1))


    if score1 >= 500:
        pixmap = QPixmap("imageeeee.jpg")
        area.setIcon(QIcon(pixmap))
        area.setIconSize(pixmap.size())
        area.setStyleSheet("text-align: center;")

    if score1 >= 1500:
        pixmap = QPixmap("golub.jpg")
        area.setIcon(QIcon(pixmap))
        area.setIconSize(pixmap.size())
        area.setStyleSheet("text-align: center;")

    



def upgrade_clicked():
    global current_boost, score1
    if score1 >= 100:
        score1 -= 100
        current_boost += 1
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade2_clicked():
        global current_boost, score1
        if score1 >= 500:
            score1 -= 500
            current_boost += 5
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade3_clicked():
        global current_boost, score1
        if score1 >= 1250:
            score1 -= 1250
            current_boost += 10
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade4_clicked():
        global current_boost, score1
        if score1 >= 3000:
            score1 -= 3000
            current_boost += 15
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade5_clicked():
        global current_boost, score1
        if score1 >= 7500:
            score1 -= 7500
            current_boost += 25
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade6_clicked():
        global current_boost, score1
        if score1 >= 15000:
            score1 -= 15000
            current_boost += 50
            score.setText(str(score1))
            boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade7_clicked():
    global current_boost, score1
    if score1 >= 35000:
        score1 -= 35000
        current_boost += 100
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade8_clicked():
    global current_boost, score1
    if score1 >= 70000:
        score1 -= 70000
        current_boost += 250
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade9_clicked():
    global current_boost, score1
    if score1 >= 150000:
        score1 -= 150000
        current_boost += 500
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")

def upgrade10_clicked():
    global current_boost, score1
    if score1 >= 500000:
        score1 -= 500000
        current_boost += 1500
        score.setText(str(score1))
        boost_text.setText(f"Сила кліку: {current_boost}")


leave_setting.clicked.connect(setting_leave)
slider.valueChanged.connect(music_editor)
setting.clicked.connect(setting_window)
button_leave.clicked.connect(leave)
area.clicked.connect(scoree)
upgrade.clicked.connect(upgrade_clicked)
upgrade2.clicked.connect(upgrade2_clicked)
upgrade3.clicked.connect(upgrade3_clicked)
upgrade4.clicked.connect(upgrade4_clicked)
upgrade5.clicked.connect(upgrade5_clicked)
upgrade6.clicked.connect(upgrade6_clicked)
upgrade7.clicked.connect(upgrade7_clicked)
upgrade8.clicked.connect(upgrade8_clicked)
upgrade9.clicked.connect(upgrade9_clicked)
upgrade10.clicked.connect(upgrade10_clicked)
window2_push_button.clicked.connect(start_game)
window3_push_button.clicked.connect(level2)


upgrade.setStyleSheet("background-color: blue;")
upgrade_sell.setStyleSheet("background-color: yellow;")
upgrade2.setStyleSheet("background-color: blue;")
upgrade2_sell.setStyleSheet("background-color: yellow;")
upgrade3.setStyleSheet("background-color: blue;")
upgrade3_sell.setStyleSheet("background-color: yellow;")
upgrade4.setStyleSheet("background-color: blue;")
upgrade4_sell.setStyleSheet("background-color: yellow;")
upgrade5.setStyleSheet("background-color: blue;")
upgrade5_sell.setStyleSheet("background-color: yellow;")
upgrade6.setStyleSheet("background-color: blue;")
upgrade6_sell.setStyleSheet("background-color: yellow;")
upgrade7.setStyleSheet("background-color: blue;")
upgrade7_sell.setStyleSheet("background-color: yellow;")
upgrade8.setStyleSheet("background-color: blue;")
upgrade8_sell.setStyleSheet("background-color: yellow;")
upgrade9.setStyleSheet("background-color: blue;")
upgrade9_sell.setStyleSheet("background-color: yellow;")
upgrade10.setStyleSheet("background-color: blue;")
upgrade10_sell.setStyleSheet("background-color: yellow;")
name_of_game_menu.setStyleSheet("font-size: 50px")



menu_window.show()
app.exec_()