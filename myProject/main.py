#program to show a splash screen for 3 seconds.
#after 3 seconds another file is opened

from tkinter import *
import os 
from PIL import ImageTk,Image
sroot=Tk()	# creating new tkinter window, sroot is a varible
def first():# first() function 
    sroot.destroy()
    if __name__ == '__main__':
        import miniProject
        miniProject.vp_start_gui()
        
sroot.geometry('500x200+500+300')
spath = "/home/lonewolf/myProject/images/clg.png" #path of the image 
simg = ImageTk.PhotoImage(Image.open(spath)) 
my = Label(sroot,image=simg) #image displayed in the label
my.image = simg
my.place(x=0,y=0)
sroot.after(3000,first)	
sroot.overrideredirect(1)# this function removes the top border to minimize, maximize or close
sroot.mainloop()
