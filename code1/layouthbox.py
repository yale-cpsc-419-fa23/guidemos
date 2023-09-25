#!/usr/bin/env python

#-----------------------------------------------------------------------
# layouthbox.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QFrame, QLabel
from PySide6.QtWidgets import QMainWindow, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

#-----------------------------------------------------------------------

def create_label(text, color):

    label = QLabel(text)
    label.setAlignment(Qt.AlignCenter)
    label.setAutoFillBackground(True)
    palette = label.palette()
    palette.setColor(label.backgroundRole(), color)
    label.setPalette(palette)
    return label

#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    red_label = create_label('Red', Qt.red)
    green_label = create_label('Green', Qt.green)
    blue_label = create_label('Blue', Qt.blue)

    red_label.setFont(QFont('Arial', 24))
    green_label.setFont(QFont('Arial', 24))
    blue_label.setFont(QFont('Arial', 24))

    layout = QHBoxLayout()
    layout.setSpacing(0)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(red_label)
    layout.addWidget(green_label)
    layout.addWidget(blue_label)

    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Layout Test: QHBoxLayout')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
