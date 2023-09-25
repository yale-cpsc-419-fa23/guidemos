#!/usr/bin/env python

#-----------------------------------------------------------------------
# widgetqcheckbox.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame
from PySide6.QtWidgets import QGridLayout, QCheckBox

#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    checkbox = QCheckBox('This is a QCheckBox')

    layout = QGridLayout()
    layout.addWidget(checkbox, 0, 0)

    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Widget Test: QCheckBox')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
