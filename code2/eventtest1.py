#!/usr/bin/env python

#-----------------------------------------------------------------------
# eventtest1.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout
from PySide6.QtWidgets import QMainWindow, QFrame
from PySide6.QtCore import Qt

window = None

def red_button_slot():
    palette = window.palette()
    palette.setColor(window.backgroundRole(), Qt.red)
    window.setPalette(palette)
    window.repaint()

def green_button_slot():
    palette = window.palette()
    palette.setColor(window.backgroundRole(), Qt.GlobalColor.green)
    window.setPalette(palette)
    window.repaint()

def blue_button_slot():
    palette = window.palette()
    palette.setColor(window.backgroundRole(), Qt.GlobalColor.blue)
    window.setPalette(palette)
    window.repaint()

def main():

    global window

    app = QApplication(argv)

    red_button = QPushButton('red')
    green_button = QPushButton('green')
    blue_button = QPushButton('blue')

    red_button.clicked.connect(red_button_slot)
    green_button.clicked.connect(green_button_slot)
    blue_button.clicked.connect(blue_button_slot)

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
    window.setWindowTitle('Event Test 1')
    window.show()

    exit(app.exec())

if __name__ == '__main__':
    main()
