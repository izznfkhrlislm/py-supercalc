########################################################################
##					Izzan Fakhril Islam								  ##
##					Student ID: 1606875806							  ##
##					Programming Assignment 4 (Super Calculator)		  ##
##					DDP 1 - Kelas F									  ##
########################################################################
########################################################################
##					Known bug: (will be fixed soon)					  ##
##					- Error when powering with 3 variables			  ##
########################################################################

                               
#Importing the modules needed to run this program
from tkinter import *
from math import * #import math (main module)
from idlelib.ToolTip import * #module needed to show the tool tip

class KalkulatorSuper:
	def __init__(self):
		window = Tk()
		window.title("Super Calculator made by Izzan")
		#Lock the window so it can't be resized
		window.minsize(width = 300, height = 400)
		window.maxsize(width = 300, height = 400)
		frame1 = Frame(window)
		print('Selamat datang di aplikasi kalkulator saya. Mohon kritik dan saran nya. :)')	
		self.memory = '0'  #Calculator memory container
		self.expr = ''  #First operand and equation container
		self.startOfNextOperand = True
		self.enterinput = Entry(frame1, relief = RIDGE, borderwidth = 3, width = 20, font = ('Roboto',18), bg = 'white', fg = 'black')
		self.enterinput.grid(row = 0, column = 0, columnspan = 5)
		buttons = [['CLR',	'MC',	'M+',	'M-',	'MR' ],    #Array of available buttons on the calculator
				   ['d',	'e',	'f',	'+',	'-'  ],
				   ['a',	'b',	'c',	'/',	'*'  ],
				   ['7',	'8',	'9',	'**',	'√'  ],
				   ['4',	'5',	'6',	'sin',	'cos'],
				   ['1',	'2',	'3',	'tan',	'ln' ],
				   ['0',	'.',	'±',	'~',	'2C' ],
				   ['x',	'o',	'^',	'|',	'&'  ],
				   ['π',	'int',	'rad',	'//',	'exp'],
				   ['bin',	'hex',	'oct',	'%',	'='] ]
		
		#Array of tooltips available when the cursor is on a button		   
		ToolTips = [['Clear', 'Memory Clear', 'Memory Add', 'Memory Subtract', 'Memory Recall'					   ],
					['Letter d', 'Letter e/Euler Number', 'Letter f', 'Add', 'Subtract'							   ],
					['Letter a', 'Letter b', 'Letter c', 'Float Divide', 'Multiply'								   ],
					['Seven', 'Eight', 'Nine', 'Power by n', 'Square Root'										   ],
					['Four', 'Five', 'Six', 'sine(radians)', 'cos(radians)'										   ],
					['One', 'Two', 'Three', 'tan(radians)', 'natural log'										   ],
					['Zero', 'Decimal point', 'Toggle +- sign', 'Bitwise complement', "32-bit 2's Complement"	   ],
					['Letter x', 'Letter o', 'Bitwise XOR', 'Bitwise OR', 'Bitwise AND'							   ],
					['Pi', 'Change to Integer', 'Change to radians', 'Integer divide', 'Power of E(2,718...)'	   ],
					['Change to binary', 'Change to hexadecimal', 'Change to octal', 'Modulo', 'Compute to decimal']]
		
		#Looping for each button and tool tip in the row and column
		for r in range(10):
			for c in range(5):
				def cmd(x = buttons[r][c]):
					self.click(x)
				b = Button(frame1, text = buttons[r][c], width = 2, relief = RAISED, font = ("Roboto", 12), command = cmd, bg = "maroon", fg = "white")
				b.grid(row = r+5, column = c)
				tip = ToolTip(b, ToolTips[r][c])
		frame1.pack()
		
		window.mainloop()
	
	#Main function, when a button in the app is clicked
	def click(self, key):
		# action called when the button '=' is clicked
		if key == '=':
			try:
				result = eval(self.expr + self.enterinput.get())
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, result)
				self.expr = ''
			except: #Error Handling
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
			self.startOfNextOperand = True
		
		#standard Python math operations
		elif key in ['+','*','-','/','//','%','**','&','|','^']:
			self.expr += '('+ self.enterinput.get() + ')'
			self.expr += key
			self.startOfNextOperand = True    
		
		#toggle +- sign to the input
		elif key == '±':
			try:
				if self.enterinput.get()[0] == '-':
					self.enterinput.delete(0)
				else:
					self.enterinput.insert(0, '-')
			except IndexError:
				pass
		
		#Square root
		elif key == '√':
			try:
				self.startOfNextOperand = True
				res = sqrt(float(self.enterinput.get()))
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, res)
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#Standard Trigonometry operations + exp (Power by Euler Number)
		elif key in ['sin', 'cos', 'tan', 'exp']:
			self.startOfNextOperand = True
			try:
				res = eval('{}(float({}))'.format(key, self.enterinput.get()))
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, res)
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#Natural log
		elif key == 'ln':
			self.startOfNextOperand = True
			res = log(float(self.enterinput.get()))
			self.enterinput.delete(0, END)
			self.enterinput.insert(END, res)
		
		#Pi (3.14.....)
		elif key == 'π':
			self.startOfNextOperand = True
			self.enterinput.delete(0, END)
			self.enterinput.insert(END, pi)
		
		#Bitwise complement
		elif key == '~':
			self.startOfNextOperand = True
			try:
				res = eval('~{}'.format(self.enterinput.get()))
				self.enterinput.delete(0,END)
				self.enterinput.insert(END, res)
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#Standard base-n conversion number
		elif key in ['bin', 'hex', 'oct', 'int']:
			self.startOfNextOperand = True
			try:
				res = eval('{}({})'.format(key, self.enterinput.get()))
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, res)
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#Radians
		elif key == 'rad':
			self.startOfNextOperand = True
			try:
				res = eval('float(radians({}))'.format(self.enterinput.get()))
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, res)
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#Memory Add
		elif key == 'M+':
			try:
				self.memory = str(eval(self.memory + '+' + self.enterinput.get())) #Adding the input to 'self.memory' variable
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#Memory subtract (Subtracting the content of 'self memory variable with the number in the input)		
		elif key == 'M-':
			try:
				self.memory = str(eval(self.memory + '-' + self.enterinput.get())) 
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#Memory Recall (Returning the content of 'self.memory' to the input pane)		
		elif key == 'MR':
			try:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, self.memory)
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#32-bit 2's Complement
		elif key == '2C':
			self.startOfNextOperand = True
			try:
				num = self.enterinput.get()
				if '-' in num: #condition when the number input is negative (less than 0)
					num = num[1:]
					self.enterinput.delete(0, END)
					self.enterinput.insert(END, format(eval(num), '#032b'))
				else: #condition when the number input is positive (greater than 0)
					res = bin(2**32 - eval(num))
					self.enterinput.delete(0, END)
					self.enterinput.insert(END, format(eval(res), '#032b'))
			except:
				self.enterinput.delete(0, END)
				self.enterinput.insert(END, 'Error')
		
		#Memory Clear (Removing the content of 'self.memory' variable)
		elif key == 'MC':
			self.memory = ''
		
		#Clear (Clears the input pane)
		elif key == 'CLR':
			self.enterinput.delete(0, END)
			self.startOfNextOperand = True
			self.expr = ''
		
		#Condition when numeric input (0-9) and alphabet input (a-e) is clicked
		else:
			#StartOfNextOperand: When a button is clicked, clears the input pane and input the clicked button
			if self.startOfNextOperand:           
				self.enterinput.delete(0, END)    
				self.startOfNextOperand = False	  
			else:								  
				pass							   
			self.enterinput.insert(END, key)
			
		
if __name__ == "__main__":
	KalkulatorSuper()	
