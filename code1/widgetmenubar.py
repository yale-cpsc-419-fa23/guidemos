#!/usr/bin/env python

#-----------------------------------------------------------------------
# widgetmenubar.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QMainWindow

#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    window = QMainWindow()
    window.setWindowTitle('Widget Test: Menubar')
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    menu_bar = window.menuBar()
    menu_bar.setNativeMenuBar(False) # Relevant on Mac
    color_menu = menu_bar.addMenu('Color')
    color_menu.addAction('Red')
    color_menu.addAction('Green')
    color_menu.addSeparator()
    blue_menu = color_menu.addMenu('Blue')
    blue_menu.addAction('Navy')
    blue_menu.addAction('Aqua')

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
