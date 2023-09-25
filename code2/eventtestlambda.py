#!/usr/bin/env python

#-----------------------------------------------------------------------
# eventtestlambda.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout
from PySide6.QtWidgets import QMainWindow, QFrame
from PySide6.QtCore import Qt

def main():

    app = QApplication(argv)

    red_button = QPushButton('red')
    green_button = QPushButton('green')
    blue_button = QPushButton('blue')

    def set_window_color(color):
        palette = window.palette()
        palette.setColor(window.backgroundRole(), color)
        window.setPalette(palette)
        window.repaint()

    red_button.clicked.connect(lambda: set_window_color(Qt.GlobalColor.red))
    green_button.clicked.connect(lambda: set_window_color(Qt.GlobalColor.green))
    blue_button.clicked.connect(lambda: set_window_color(Qt.GlobalColor.blue))

    layout = QHBoxLayout()
    layout.addWidget(red_button)
    layout.addWidget(green_button)
    layout.addWidget(blue_button)

    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)
    window.setWindowTitle('Event Test 4')
    window.show()

    exit(app.exec())

if __name__ == '__main__':
    main()
