from tkinter import *
from PIL import ImageTk,Image
import pyautogui

root = Tk()
root.attributes("-topmost", True,)
root.config(bg="black")
root.overrideredirect(1)
root.wm_attributes("-alpha", 0.01)

def Position():
    root.geometry("1000x1000+%d+%d" % (pyautogui.position()[0]-500, pyautogui.position()[1]-500))
    root.after(1, Position)

Position()
root.mainloop()