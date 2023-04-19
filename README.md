# FlaskRD
Remote desktop control using Flask, OpenCV and PyAutoGUI

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [Flask](https://pypi.org/project/Flask/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Pillow](https://pypi.org/project/Pillow/2.2.2/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)

## Description
The program uses OpenCV and Pillow to capture the screen frame. Then, the frame served using Flask web server.
Afterthat, mouse clicks are captured using Javascript and passed to python as AJAX requests. Finally, PyAutoGUI simulates the mouse click.

## Running the application
1. Run **main.py** file from terminal (Linux) or Command Prompt (Windows).
   ```
   python main.py
   ```
2. Open `http://localhost/`  or your IP address on the same network.
  

## Limitations

This program although functional was developed in few hours to prove that Python is a powerful tool for web development.
The availability of libraries allowed for the program to be short and minimal. 

- The program uses alot of computer CPU resources. 
- The frame rate is limited by the host computer processing power. 
- The program doesn't support these functionalities (These can be added to the Javascript and Python(PyAutoGUI) easily):
   1. Differentiate between right and left clicks.
   2. Detect mouse wheel roll.
   3. Detect keyboard presses.


