#!/usr/bin/env python

#-----------------------------------------------------------------------
# widgetqslider.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QFrame, QSlider
from PySide6.QtWidgets import QMainWindow, QGridLayout
from PySide6.QtCore import Qt

#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setMinimum(0)
    slider.setMaximum(100)
    slider.setTickPosition(QSlider.TickPosition.TicksBelow)
    slider.setTickInterval(20)
    slider.setValue(20)

    layout = QGridLayout()
    layout.addWidget(slider, 0, 0)
    frame = QFrame()
    frame.setLayout(layout)

    window = QMainWindow()
    window.setWindowTitle('Widget Test: QSlider')
    window.setCentralWidget(frame)
    screen_size = app.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
