from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QSlider, QCheckBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import os
import sys
import resources_rc
import random
import string
import zxcvbn

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), '..', 'ui', 'password_generator.ui')
        ui_path = os.path.abspath(ui_path)
        uic.loadUi(ui_path, self)

        # Add Widgets
        self.eyeBtn = self.findChild(QPushButton, "eyeBtn")
        self.copyBtn = self.findChild(QPushButton, "copyBtn")
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.lengthSlider = self.findChild(QSlider, "horizontalSlider")
        self.lengthValueLabel = self.findChild(QLabel, "show_length_label")
        self.lowercaseCheckbox = self.findChild(QCheckBox, "lowercaseCheckbox")
        self.uppercaseCheckbox = self.findChild(QCheckBox, "uppercaseCheckbox")
        self.digitsCheckbox = self.findChild(QCheckBox, "digitsCheckbox")
        self.specialCheckbox = self.findChild(QCheckBox, "specialCheckbox")
        self.generateButton = self.findChild(QPushButton, "generateButton")
        self.strengthLabel = self.findChild(QLabel, "strengthLabel")
        self.eye_open = True
        # Set minimum, maximum, and initial value for the slider
        self.lengthSlider.setMinimum(6)
        self.lengthSlider.setMaximum(32)
        self.lengthSlider.setValue(12)

        # Connecting widgets via click event
        self.eyeBtn.clicked.connect(self.show_hide_pass)
        self.copyBtn.clicked.connect(self.copy_pass)
        self.lengthSlider.valueChanged.connect(self.update_length_label)
        self.generateButton.clicked.connect(self.generate_password)

        self.show()

    # Function to show/hide password
    def show_hide_pass(self):

        if self.eye_open:
            self.eyeBtn.setIcon(QIcon("assets/eye-closed.png"))
            self.eyeBtn.setIconSize(QSize(42, 42))
            self.lineEdit.setEchoMode(QLineEdit.Password)
            self.eye_open = False
        else:
            self.eyeBtn.setIcon(QIcon("assets/eye-open.png"))
            self.lineEdit.setEchoMode(QLineEdit.Normal)
            self.eye_open = True

    # Function to copy password
    def copy_pass(self):

        text = self.lineEdit.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    # Update length label when slider value changes
    def update_length_label(self, value):
        self.lengthValueLabel.setText(str(value))

    # Generate Password and evaluate it
    def generate_password(self):
        # Get password length from slider
        password_length = self.lengthSlider.value()

        # Create a list of selected characters
        char_set = ""

        # Check selected checkboxes
        if self.lowercaseCheckbox.isChecked():
            char_set += string.ascii_lowercase
        if self.uppercaseCheckbox.isChecked():
            char_set += string.ascii_uppercase
        if self.digitsCheckbox.isChecked():
            char_set += string.digits
        if self.specialCheckbox.isChecked():
            char_set += string.punctuation

        # If no option is selected, display an error message
        if not char_set:
            self.lineEdit.setText("No characters selected!")
            return

        # Generate a random password
        password = ''.join(random.choice(char_set) for _ in range(password_length))

        self.lineEdit.setText(password)
        result = zxcvbn.zxcvbn(password)

        # Display password strength in UI
        score = result['score']

        # Password strength score
        if score == 0:
            self.strengthLabel.setText("This password is Very Weak!")
        elif score == 1:
            self.strengthLabel.setText("This password is Weak!")
        elif score == 2:
            self.strengthLabel.setText("This password is Medium!")
        elif score == 3:
            self.strengthLabel.setText("This password is Strong!")
        else:
            self.strengthLabel.setText("This password is Very Strong!")


app = QApplication(sys.argv)
window = UI()
app.exec_()
