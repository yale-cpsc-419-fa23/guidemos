#!/usr/bin/env python

#-----------------------------------------------------------------------
# dialogreadvalue.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QMainWindow, QFrame
from PySide6.QtWidgets import QTextEdit, QInputDialog

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
    window.setWindowTitle('Read a value')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    def button_slot():
        reply, successful = (
            QInputDialog.getText(window, 'My title', 'My prompt'))
        if successful:
            textedit.append(reply)
        else:
            textedit.append('(no reply)')

    button.clicked.connect(button_slot)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
