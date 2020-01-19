import tkinter
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.svm import SVC
#import tkFileDialog
import cv2



window = tkinter.Tk()


def select_image():

	global panelA, panelB
	path = tkinter.filedialog.askopenfilename()
	if len(path) > 0:
		image=cv2.imread(path)
	panelA.image = image



panelA = None
panelB= None









btn = tkinter.Button(window,text='Select an Image',command = select_image)
btn.pack(side="bottom",fill='both',expand='yes',padx="10",pady = "10")


window.geometry('1000x800')
window.mainloop()