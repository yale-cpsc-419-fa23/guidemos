#!/usr/bin/env python

#-----------------------------------------------------------------------
# widgetqradiobuttons.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QFrame, QRadioButton
from PySide6.QtWidgets import QMainWindow, QGridLayout


#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    red_radiobutton = QRadioButton('Red QRadioButton')
    green_radiobutton = QRadioButton('Green QRadioButton')
    blue_radiobutton = QRadioButton('Blue QRadioButton')

    red_radiobutton.setChecked(True)

    layout = QGridLayout()
    layout.addWidget(red_radiobutton, 0, 0)
    layout.addWidget(green_radiobutton, 1, 0)
    layout.addWidget(blue_radiobutton, 2, 0)
    radiobutton_frame = QFrame()
    radiobutton_frame.setLayout(layout)

    layout = QGridLayout()
    layout.addWidget(radiobutton_frame, 0, 0)
    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Widget Test: QRadioButtons')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
