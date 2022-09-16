# getting Tkinter for making window interface
import tkinter as tk
from tkinter import *
import sys


sys.path.append('files\\')


from face_recognizer import run_fr
from face_encoder import  encoding_faces_to_database


# Creating a window
window = tk.Tk()

# Setting the name of the window
window.title('Face Recognition System')

# Size of the window
window.geometry("500x650")


# Putting the text on the window
text1 = Label(window, text='\n\nStart the recording')
text1.pack()

# Putting the Button on the window -
# input parameters --> window, Name of the button, Width of the button, The function it does
button1 = tk.Button(window, text='Start', width=25, command = run_fr)
button1.pack()


# Putting the text on the window
text2 = Label(window, text='\n\nUpdate face-database')
text2.pack()

# Putting the Button on the window
button2 = tk.Button(window, text='Update', width=25, command =  encoding_faces_to_database)
button2.pack()

'''
# Putting the text on the window
text3 = Label(window, text='\n\nEvaluate the time')
text3.pack()

# Putting the Button on the window
button3 = tk.Button(window, text='Evaluate', width=25, command = "")
button3.pack()
'''

# Creating a function that closes the window
def close_file():
    window.destroy()

text4 = Label(window, text='\n\n')
text4.pack()

button4 = tk.Button(window, text='Close', width=25, command = close_file)
button4.pack()

# Show the Window
window.mainloop()

