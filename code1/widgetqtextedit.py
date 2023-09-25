#!/usr/bin/env python

#-----------------------------------------------------------------------
# widgetqtextedit.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QTextEdit

#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    long_str = 'Red Orange Yellow Green Blue Violet '
    long_str += 'Red Orange Yellow Green Blue Violet '
    long_str += 'Red Orange Yellow Green Blue Violet '
    long_str += 'Red Orange Yellow Green Blue Violet '
    long_str += 'Red Orange Yellow Green Blue Violet '
    long_str += 'Red Orange Yellow Green Blue Violet '
    long_str += 'Red Orange Yellow Green Blue Violet'
    textedit = QTextEdit('This is a QTextEdit' + '<br>' + long_str)

    layout = QGridLayout()
    layout.addWidget(textedit, 0, 0)
    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Widget Test: QTextEdit')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
