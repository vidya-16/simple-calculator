from tkinter import *
import math
root=Tk()

root.title("Simple calculator")
global op 
op="none"

e=Entry(root,width=80,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


def button_click(number):
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def button_add():
	num=e.get()  # getting first number
	global num1
	global op
	op="add"
	num1=int(num) #making first number as global
	e.delete(0,END)

	
	
def button_sub():
	num=e.get()  #getting first number
	global num1
	global op
	op="sub"
	num1=int(num) #making first number as global
	e.delete(0,END)

def button_mul():
	num=e.get()
	global num1
	global op
	op="mul"
	num1=int(num) #making first number as global
	e.delete(0,END)

def button_div():
	num=e.get()
	global num1
	global op
	op="div"
	num1=int(num) #making first number as global
	e.delete(0,END)

def button_mod():
	num=e.get()
	global num1
	global op
	op="mod"
	num1=int(num) #making first number as global
	e.delete(0,END)

def button_pow():
	num=e.get()
	global num1
	global op
	op="pow"
	num1=int(num) #making first number as global
	e.delete(0,END)

def button_root():
	num=e.get()
	global num1
	global op
	num1=int(num) #making first number as global
	op="root"
	e.delete(0,END)
	e.insert(0,math.sqrt(int(num))) #after clicking the root button root of the number is displayed

def button_equal():
	num=e.get()
	e.delete(0,END)

	if op=="add":
		e.insert(0,num1+int(num))
			
	if op=="sub":
		e.insert(0,num1-int(num))
			
	if op=="mul":
		e.insert(0,num1*int(num))	
	
	if op=="div":
		e.insert(0,num1/int(num))
			
	if op=="mod":
		e.insert(0,num1%int(num))	
		
		
	if op=="pow":
		e.insert(0,num1**int(num))	
		
		
	if op=="root":
		e.insert(0,math.sqrt(int(num1)))
		
	if op=="none":
		e.insert(0,num)
	



def button_clear():
	global op
	e.delete(0,END)
	op="none"

button_1=Button(root,text="1",padx=50,pady=20,command=lambda:button_click(1))
button_2=Button(root,text="2",padx=53,pady=20,command=lambda:button_click(2))
button_3=Button(root,text="3",padx=50,pady=20,command=lambda:button_click(3))
button_4=Button(root,text="4",padx=50,pady=20,command=lambda:button_click(4))
button_5=Button(root,text="5",padx=53,pady=20,command=lambda:button_click(5))
button_6=Button(root,text="6",padx=50,pady=20,command=lambda:button_click(6))
button_7=Button(root,text="7",padx=50,pady=20,command=lambda:button_click(7))
button_8=Button(root,text="8",padx=53,pady=20,command=lambda:button_click(8))
button_9=Button(root,text="9",padx=50,pady=20,command=lambda:button_click(9))
button_0=Button(root,text="0",padx=50,pady=20,command=lambda:button_click(0))
button_clear=Button(root,text="clear",padx=43,pady=20,command=button_clear)
button_add=Button(root,text="+",padx=50,pady=20,command=button_add)
button_sub=Button(root,text="-",padx=53,pady=20,command=button_sub)
button_mul=Button(root,text="*",padx=50,pady=20,command=button_mul)
button_div=Button(root,text="/",padx=71,pady=20,command=button_div)
button_mod=Button(root,text="%",padx=68,pady=20,command=button_mod)
button_pow=Button(root,text="x^n",padx=63,pady=20,command=button_pow)
button_root=Button(root,text="sq_root",padx=54,pady=20,command=button_root)
button_equal=Button(root,text="=",padx=127,pady=20,command=button_equal)

button_add.grid(row=1,column=0)
button_sub.grid(row=1,column=1)
button_mul.grid(row=1,column=2)
button_div.grid(row=1,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_mod.grid(row=2,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_pow.grid(row=3,column=3)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_root.grid(row=4,column=3)

button_0.grid(row=5,column=0)
button_clear.grid(row=5,column=1)
button_equal.grid(row=5,column=2,columnspan=2)

root.mainloop()