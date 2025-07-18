Password Generator Application
Overview
The Password Generator is a desktop application built using PyQt5 and Python, designed to create secure, random passwords based on user-defined criteria. The application features a sleek, user-friendly interface with a dark theme and neon-green accents, inspired by a cyberpunk aesthetic. It allows users to customize password length and character types, evaluate password strength, and copy generated passwords to the clipboard.
Features

Customizable Password Generation: Users can select character types (lowercase, uppercase, digits, special characters) and adjust password length (6–32 characters) using a slider.
Password Strength Evaluation: Utilizes the zxcvbn library to assess password strength, displaying results as "Very Weak," "Weak," "Medium," "Strong," or "Very Strong."
Show/Hide Password: Toggle password visibility with an eye icon button.
Copy to Clipboard: Easily copy the generated password with a dedicated button.
Responsive UI: A modern, dark-themed interface with a background image and styled widgets for an intuitive user experience.

App preview 
[App Demo](assets/demo.png)


Technologies Used

Python 3.x: Core programming language.
PyQt5: Framework for building the graphical user interface.
zxcvbn: Library for evaluating password strength.
Qt Designer: Used to create the .ui file for the interface layout.

Project Structure
password_generator/
├── password_generator.py    # Main application logic
├── resources_rc.py          # Compiled resource file for icons and assets
├── password.ui              # Qt Designer file for the UI layout
├── assets/                  # Folder containing images (background, icons)
│   ├── background.png
│   ├── eye-open.png
│   ├── eye-closed.png
│   ├── copy.png

Installation

Clone the Repository:
git clone https://github.com/mahyarmohammadlou/password-generator.git
cd password_generator


Install Dependencies:Ensure you have Python 3.x installed. Install the required Python packages:
pip install pyqt5 zxcvbn


Run the Application:Execute the main script to launch the application:
python password_generator.py



Usage

Launch the application.
Use the slider to set the desired password length (displayed in real-time).
Check the boxes for the character types to include (lowercase, uppercase, digits, special characters).
Click the Generate Password button to create a password.
View the generated password in the text field and its strength below.
Use the eye button to toggle password visibility.
Click the copy button to copy the password to your clipboard.

Notes

Ensure the assets folder is in the same directory as the main script, as it contains the required images for the UI.
The password.ui file is loaded dynamically using uic.loadUi. Ensure it is accessible in the specified path.
The zxcvbn library provides robust password strength analysis based on entropy and common patterns.

Troubleshooting

Missing Assets: If icons or the background image fail to load, verify the assets folder and resources_rc.py file are correctly set up.
UI File Not Found: Ensure the password.ui file is in the correct directory or update the path in password_generator.py.
Dependencies: Confirm that PyQt5 and zxcvbn are installed correctly.

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request with a clear description of your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Inspired by cyberpunk aesthetics for the UI design.
Thanks to the creators of zxcvbn for providing a reliable password strength evaluation tool.
