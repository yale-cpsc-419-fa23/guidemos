#!/usr/bin/env python

#-----------------------------------------------------------------------
# widgetqlistwidget.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QFrame, QListWidget
from PySide6.QtWidgets import QMainWindow, QGridLayout


#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    listwidget = QListWidget()
    listwidget.insertItem(0, 'This is a QListWidget')
    listwidget.insertItem(1, 'Red')
    listwidget.insertItem(2, 'Orange')
    listwidget.insertItem(3, 'Yellow')
    listwidget.insertItem(4, 'Green')
    listwidget.insertItem(5, 'Blue')
    listwidget.insertItem(6, 'Violet')

    listwidget.setCurrentRow(1)

    layout = QGridLayout()
    layout.addWidget(listwidget, 0, 0)
    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Widget Test: QListWidget')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
