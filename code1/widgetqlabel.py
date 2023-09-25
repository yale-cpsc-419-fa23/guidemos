#!/usr/bin/env python

#-----------------------------------------------------------------------
# widgetqlabel.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QFrame, QLabel
from PySide6.QtWidgets import QMainWindow, QGridLayout

#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    label = QLabel('This is a QLabel')

    layout = QGridLayout()
    layout.addWidget(label, 0, 0)
    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Widget Test: QLabel')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
