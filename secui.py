import tkinter
from tkinter import *



window=Tk()

#define the function to execute securitycam.py script, first import the securitycam.py module as following
def record():
     import securitycam
     execfile('securitycam.py')
     
    
#put a button named 'Start Security Cam' which will execute the securitycam module when clicked
btn=Button(window, text="Start Security Cam", fg='blue', bg = "white", font=("Helvetica", 8),command = record)

#define positions of the button
btn.place(x=80, y=100)

#stop = Button(window, text="Stop Security Cam",command=stop)
#stop.place(x=80, y=140)

#define window title
window.title('Security Cam Application')

#define window geonmetry
window.geometry("300x200+10+20")
window.mainloop()
