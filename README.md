# Security-Cam-and-Basic-UI-with-OpenCV-and-TKinter
Security Cam and Basic UI with OpenCV and TKinter made with Python

There are three different files in this repository. One is 'securitycam.py' which contains the scrpit for security cam. When this script is run, it startarts to record when it detecs a face, and it continues to record until 5 seconds after it stops detecting a face. And when it stops recording, it writes the recorded video in mp4 format to the same folder which contains 'securitycam.py' file.  Note that only 'securitycam.py' file is enough to function as a face detection security cam, and you can quit the program by pressing 'q'. 

The second file of this repository is 'secui.py', which provides a basic user interface for 'securitycam.py' script to run. When 'Start Security Cam' button is clicked, is opens 'securitycam.py' scrpit, and when you close the interface, 'securitycam.py' script also stops.

The third file is the batch file, 'secui.bat', you need to open and close the whole application by running and closing from this third batch file.

Note that for the program to be able to run all of these three files need to be in the same folder. Also opencv needs to be installed, you can just open the command prompt and type 'pip3 install opencv-python' and it will be done.

