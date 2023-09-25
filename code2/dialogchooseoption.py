#!/usr/bin/env python

#-----------------------------------------------------------------------
# dialogchooseoption.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QMainWindow, QFrame
from PySide6.QtWidgets import QTextEdit, QMessageBox

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
    window.setWindowTitle('Choose an option')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    def button_slot():
        reply = QMessageBox.question(window, 'My title', 'My message',
            buttons=(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No))
            # Others: Ok, Open, Save, Cancel, Close, Discard,
            # Apply, Reset, RestoreDefaults, Help, SaveAll,
            # YesToAll, NoToAll, Abort, Retry, Ignore, NoButton
        if reply == QMessageBox.StandardButton.Yes:
            text = 'Yes'
        elif reply == QMessageBox.StandardButton.No:
            text = 'No'
        else:
            text = '(No option chosen)'  # Unused!!! (Or...should be)
        textedit.append(text)

    button.clicked.connect(button_slot)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
