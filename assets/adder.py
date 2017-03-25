from tkinter import *
import math
import operator
import functools

class simpleAdder(object):
	def __init__(self):
		window = Tk()
		window.title("Simple Adder")
		
		
		self.input1 = StringVar()
		self.entervalue = Entry(window, width = 25, bg = "white", textvariable = self.input1, state = NORMAL)
		self.addButton = Button(window, text = "Add", command = self.onButtonClick, bg = "white")
		self.multiplyButton = Button(window, text = "Multiply", command = self.onButtonClick(2), bg = "white")
		self.equalButton = Button(window, text = "=", command = lambda: self.onEqualClick(1), bg = "white")
		self.entervalue.pack()
		self.addButton.pack()
		self.equalButton.pack()
		self.numbers = []
		self.entervalue.insert(END, '0')
		window.mainloop()
		
	def onButtonClick(self):
		
		self.value = int(self.entervalue.get())
		self.numbers.append(self.value)
		print(self.numbers)
		self.entervalue.delete(0, END)
		self.entervalue.insert(END, '0')
	
	def onEqualClick(self, button_id):
		if button_id == 1:
			self.value2 = int(self.entervalue.get())
			self.numbers.append(self.value2)
			print(self.numbers)
			self.akhir = sum(self.numbers)
			self.entervalue.delete(0, END )
			self.entervalue.insert(END, self.akhir)
		
			
			
	#def add(self):
	#	self.value = int(self.entervalue.get())
	#	self.numbers.append(self.value)
	#	print(self.numbers)
	#	self.entervalue.delete(0, END)
	#	self.entervalue.insert(END, '0')
	
	#def equal(self):
	#	self.value2 = int(self.entervalue.get())
	#	self.numbers.append(self.value2)
	#	print(self.numbers)
	#	self.akhir = sum(self.numbers)
	#	self.entervalue.delete(0, END )
	#	self.entervalue.insert(END, self.akhir)
	
		
if __name__ == "__main__":
	simpleAdder()
		
