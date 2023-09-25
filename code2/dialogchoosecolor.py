#!/usr/bin/env python

#-----------------------------------------------------------------------
# dialogchoosecolor.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QMainWindow, QFrame
from PySide6.QtWidgets import QTextEdit, QColorDialog

def main():

    app = QApplication(argv)

    button = QPushButton('Show Dialog')

    textedit = QTextEdit()

    layout = QVBoxLayout()
    layout.addWidget(button)
    layout.addWidget(textedit)

    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Choose a color')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    def button_slot():
        color = QColorDialog.getColor()
        if color.isValid():
            textedit.append('Red: %s Green: %s Blue: %s' %
            (color.red(), color.green(), color.blue()))
        else:
            textedit.append('(No color chosen)')

    button.clicked.connect(button_slot)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
