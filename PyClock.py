#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name:       PyClock
Created by: Christian Morán
e-mail:     christianrmoran86@gmail.com
More code:  http://github.com/chrisrm86

##########################################################
"""
from tkinter import *
import time 

class PyClock:
	def __init__(self, parent=None):
		self.frame = parent
		self.frame.geometry("485x200")
		self.frame.resizable(False,False)
		self.frame.title("PyClock")
		self.frame.iconbitmap('clock-icon.ico')
		self.cont = Frame(self.frame)
		self.cont.pack(expand=YES, fill=BOTH)

		self.buttonsContainer = Frame(self.cont)
		self.buttonsContainer.pack(side=BOTTOM)

		display = Label(self.cont, bg="Black", fg="white", height=2)
		display.pack(expand=NO, fill=X)

		def actualTime():
			t=time.strftime('%H:%M:%S', time.localtime())
			if t != '':
				display.config(text=t, font=('times 25',90))
			display.after(1000, actualTime)
		actualTime()

		def classic():
			display.config(bg="Black", fg="White")

		def reverse():
			display.config(bg="White", fg="Black")

		def orange():
			display.config(bg="White", fg="Orange")

		def blue():
			display.config(bg="#052242", fg="#0C5AB1")

		def uranium():
			display.config(bg="#4A5765", fg="White")

		self.b1 = Button(self.buttonsContainer, text="Classic", command=classic, width=10)
		self.b1.pack(side=LEFT)
		self.b2 = Button(self.buttonsContainer, text="Reverse", command=reverse, width=10)
		self.b2.pack(side=LEFT)
		self.b3 = Button(self.buttonsContainer, text="Orange", command=orange, width=10)
		self.b3.pack(side=LEFT)
		self.b4 = Button(self.buttonsContainer, text="Blue", command=blue, width=10)
		self.b4.pack(side=LEFT)
		self.b5 = Button(self.buttonsContainer, text="Uranium", command=uranium, width=10)
		self.b5.pack(side=LEFT)

if __name__=='__main__':
	root = Tk()
	PyClock(root)
	root.mainloop()