#!/usr/bin/env python

#-----------------------------------------------------------------------
# layoutgridstretch.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QFrame, QLabel
from PySide6.QtWidgets import QMainWindow, QGridLayout
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

    north_label = create_label('North', Qt.red)
    south_label = create_label('South', Qt.red)
    east_label = create_label('East', Qt.gray)
    west_label = create_label('West', Qt.gray)
    center_label = create_label('Center', Qt.green)

    north_label.setFont(QFont('Arial', 24))
    south_label.setFont(QFont('Arial', 24))
    east_label.setFont(QFont('Arial', 24))
    west_label.setFont(QFont('Arial', 24))
    center_label.setFont(QFont('Arial', 24))

    layout = QGridLayout()
    layout.setSpacing(0)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(north_label, 0, 0, 1, 3)
    layout.addWidget(west_label, 1, 0)
    layout.addWidget(center_label, 1, 1)
    layout.addWidget(east_label, 1, 2)
    layout.addWidget(south_label, 2, 0, 1, 3)
    layout.setRowStretch(0, 0)
    layout.setRowStretch(1, 1)
    layout.setRowStretch(2, 0)
    layout.setColumnStretch(0, 0)
    layout.setColumnStretch(1, 1)
    layout.setColumnStretch(2, 0)

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
