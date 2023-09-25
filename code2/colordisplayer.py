#!/usr/bin/env python

#-----------------------------------------------------------------------
# colordisplayer.py
# Author: Bob Dondero
# Modified by Alan Weide 2022-09-25 to use PySide6
#-----------------------------------------------------------------------

from sys import exit, argv
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame
from PySide6.QtWidgets import QLabel, QSlider, QLineEdit, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

#-----------------------------------------------------------------------

MAX_INTENSITY = 255

#-----------------------------------------------------------------------

R = 0
G = 1
B = 2

#-----------------------------------------------------------------------

def create_labels():

    red_label = QLabel('Red:')
    red_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
    red_label.setAutoFillBackground(True)
    palette = red_label.palette()
    palette.setColor(red_label.backgroundRole(), Qt.GlobalColor.red)
    red_label.setPalette(palette)

    green_label = QLabel('Green:')
    red_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
    green_label.setAutoFillBackground(True)
    palette = green_label.palette()
    palette.setColor(green_label.backgroundRole(), Qt.GlobalColor.green)
    green_label.setPalette(palette)

    blue_label = QLabel('Blue:')
    red_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
    blue_label.setAutoFillBackground(True)
    palette = blue_label.palette()
    palette.setColor(blue_label.backgroundRole(), Qt.GlobalColor.blue)
    blue_label.setPalette(palette)

    return (red_label, green_label, blue_label)

#-----------------------------------------------------------------------

def create_sliders():

    red_slider = QSlider(Qt.Orientation.Horizontal)
    red_slider.setMinimum(0)
    red_slider.setMaximum(MAX_INTENSITY)

    green_slider = QSlider(Qt.Orientation.Horizontal)
    green_slider.setMinimum(0)
    green_slider.setMaximum(MAX_INTENSITY)

    blue_slider = QSlider(Qt.Orientation.Horizontal)
    blue_slider.setMinimum(0)
    blue_slider.setMaximum(MAX_INTENSITY)

    return (red_slider, green_slider, blue_slider)

#-----------------------------------------------------------------------

def create_lineedits():

    red_lineedit = QLineEdit('0')
    green_lineedit = QLineEdit('0')
    blue_lineedit = QLineEdit('0')

    return (red_lineedit, green_lineedit, blue_lineedit)

#-----------------------------------------------------------------------

def create_control_frame(labels, sliders, lineedits):

    control_frame_layout = QGridLayout()
    control_frame_layout.setSpacing(0)
    control_frame_layout.setContentsMargins(0, 0, 0, 0)
    control_frame_layout.setRowStretch(0, 0)
    control_frame_layout.setRowStretch(1, 0)
    control_frame_layout.setRowStretch(2, 0)
    control_frame_layout.setColumnStretch(0, 0)
    control_frame_layout.setColumnStretch(1, 1)
    control_frame_layout.setColumnStretch(2, 0)
    control_frame_layout.addWidget(labels[R], 0, 0)
    control_frame_layout.addWidget(labels[G], 1, 0)
    control_frame_layout.addWidget(labels[B], 2, 0)
    control_frame_layout.addWidget(sliders[R], 0, 1)
    control_frame_layout.addWidget(sliders[G], 1, 1)
    control_frame_layout.addWidget(sliders[B], 2, 1)
    control_frame_layout.addWidget(lineedits[R], 0, 2)
    control_frame_layout.addWidget(lineedits[G], 1, 2)
    control_frame_layout.addWidget(lineedits[B], 2, 2)
    control_frame = QFrame()
    control_frame.setLayout(control_frame_layout)
    return control_frame

#-----------------------------------------------------------------------

def create_color_frame():

    color_frame = QFrame()
    color_frame.setAutoFillBackground(True)
    palette = color_frame.palette()
    palette.setColor(color_frame.backgroundRole(), Qt.GlobalColor.black)
    color_frame.setPalette(palette)
    return color_frame

#-----------------------------------------------------------------------

def create_central_frame(color_frame, control_frame):

    central_frame_layout = QGridLayout()
    central_frame_layout.setSpacing(0)
    central_frame_layout.setContentsMargins(0, 0, 0, 0)
    central_frame_layout.setRowStretch(0, 1)
    central_frame_layout.setRowStretch(1, 0)
    central_frame_layout.setColumnStretch(0, 1)
    central_frame_layout.addWidget(color_frame, 0, 0)
    central_frame_layout.addWidget(control_frame, 1, 0)
    central_frame = QFrame()
    central_frame.setLayout(central_frame_layout)
    return central_frame

#-----------------------------------------------------------------------

def create_window(central_frame):

    window = QMainWindow()
    window.setWindowTitle('Color Displayer')
    window.setCentralWidget(central_frame)
    screen_size = QApplication.primaryScreen().availableGeometry()
    window.resize(screen_size.width()//2, screen_size.height()//2)
    return window

#-----------------------------------------------------------------------

def slider_slot_helper(sliders, lineedits, color_frame):

    red = sliders[R].value()
    green = sliders[G].value()
    blue = sliders[B].value()
    lineedits[R].setText(str(red))
    lineedits[G].setText(str(green))
    lineedits[B].setText(str(blue))
    palette = color_frame.palette()
    palette.setColor(
        color_frame.backgroundRole(), QColor(red, green, blue))
    color_frame.setPalette(palette)

#-----------------------------------------------------------------------

def lineedit_slot_helper(lineedits, sliders, color_frame):

    try:
        red = int(lineedits[R].text())
        green = int(lineedits[G].text())
        blue = int(lineedits[B].text())
        if (red < 0) or (red > MAX_INTENSITY):
            raise Exception()
        if (green < 0) or (green > MAX_INTENSITY):
            raise Exception()
        if (blue < 0) or (blue > MAX_INTENSITY):
            raise Exception()
        sliders[R].setValue(red)
        sliders[G].setValue(green)
        sliders[B].setValue(blue)
        palette = color_frame.palette()
        palette.setColor(
            color_frame.backgroundRole(), QColor(red, green, blue))
        color_frame.setPalette(palette)
    except Exception:
        # Use the Slider objects to restore the LineEdit objects.
        lineedits[R].setText(str(sliders[R].value()))
        lineedits[G].setText(str(sliders[G].value()))
        lineedits[B].setText(str(sliders[B].value()))

#-----------------------------------------------------------------------

def main():

    app = QApplication(argv)

    # Create and lay out widgets.

    labels = create_labels()
    sliders = create_sliders()
    lineedits = create_lineedits()
    control_frame = create_control_frame(labels, sliders, lineedits)
    color_frame = create_color_frame()
    central_frame = create_central_frame(color_frame, control_frame)
    window = create_window(central_frame)

    # Handle events for the QSlider objects.

    def slider_slot():
        slider_slot_helper(sliders, lineedits, color_frame)
    for slider in sliders:
        slider.valueChanged.connect(slider_slot)

    # Handle events for the LineEdit objects.

    def lineedit_slot():
        lineedit_slot_helper(lineedits, sliders, color_frame)
    for lineedit in lineedits:
        lineedit.editingFinished.connect(lineedit_slot)

    window.show()
    exit(app.exec())

if __name__ == '__main__':
    main()
