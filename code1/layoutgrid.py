#!/usr/bin/env python

#-----------------------------------------------------------------------
# layoutgrid.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QFrame, QLabel
from PySide6.QtWidgets import QMainWindow, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont

#-----------------------------------------------------------------------

def create_label(text, color):

    label = QLabel(text)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setAutoFillBackground(True)
    palette = label.palette()
    palette.setColor(label.backgroundRole(), color)
    label.setPalette(palette)
    return label

#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    red_label = create_label('Red', Qt.red)
    orange_label = create_label('Orange', QColor(0xFF, 0xA5, 0x00))
    yellow_label = create_label('Yellow', Qt.yellow)
    green_label = create_label('Green', Qt.green)
    blue_label = create_label('Blue', Qt.blue)
    violet_label = create_label('Violet', QColor(0x7F, 0x00, 0xFF))

    typeface = 'Arial'
    red_label.setFont(QFont(typeface, 24))
    orange_label.setFont(QFont(typeface, 24))
    yellow_label.setFont(QFont(typeface, 24))
    green_label.setFont(QFont(typeface, 24))
    blue_label.setFont(QFont(typeface, 24))
    violet_label.setFont(QFont(typeface, 24))

    layout = QGridLayout()
    layout.setSpacing(10)
    layout.setContentsMargins(10, 10, 10, 10)
    layout.addWidget(red_label, 0, 0)
    layout.addWidget(orange_label, 0, 1)
    layout.addWidget(yellow_label, 0, 2)
    layout.addWidget(green_label, 1, 0)
    layout.addWidget(blue_label, 1, 1)
    layout.addWidget(violet_label, 1, 2)

    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Layout Test: QGridLayout')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
