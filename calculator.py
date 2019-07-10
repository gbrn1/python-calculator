from tkinter import *

# define functions
def sumFunction(a,b):
    return a+b

def subtractFunction(a,b):
    return a-b

def multiplyFunction(a,b):
    return a*b

def divideFunction(a,b):
    return a/b

def raiseFunction(a,b):
    return a**b

showtext = ''
text = ''

root = Tk()
root.geometry('300x300')
root.title('Calculator')

painel = Frame(root)
painel.pack()
txt = Label(painel, text=showtext)
txt.pack()
txt["font"] = ("Calibri", "20", "bold")

factors = []
sign = 0

def AddFactor(value):
    global showtext
    global factors
    global text
    showtext+=value
    text+=value
    txt.configure(text=showtext)
    if len(factors) > 0 and sign == 0:
        factors = []
        factors.append(text)

    if len(factors) == 0:
        factors.append(text)
    
    if sign != 0 and len(factors) == 1:
        factors.append(text)

    if len(factors) > 1:
        factors.append(text)
        factors.remove(factors[-2])
        
    print(factors)
def SetSign(Value):
    global sign
    global showtext
    global text
    if sign == 0:
        sign = int(Value)
        if Value == 1:
            showtext+='+'
            txt.configure(text=showtext)
        if Value == 2:
            showtext+='-'
            txt.configure(text=showtext)
        if Value == 3:
            showtext+='x'
            txt.configure(text=showtext)
        if Value == 4:
            showtext+='/'
            txt.configure(text=showtext)
        if Value == 5:
            showtext+='**'
            txt.configure(text=showtext)
        text = ''

def Result():
    global sign
    global showtext
    global factors
    print(factors)
    if len(factors) >= 2:
        a = float(factors[0])
        b = float(factors[1])
        if int(a) == a:
            a = int(a)

        if int(b) == b:
            b = int(b)   
         
        if sign == 1:
            result = sumFunction(a,b)
        if sign == 2:
            result = subtractFunction(a,b)
        if sign == 3:
            result = multiplyFunction(a,b)
        if sign == 4:
            try:
                result = divideFunction(a,b)
            except ZeroDivisionError:
                clear()
        if sign == 5:
            result = raiseFunction(a,b) 
        showtext = str(result)
        txt.configure(text=showtext)
        sign = 0
        factors = [result]

def remove():
    global showtext
    global text
    global sign
    global factors
    signs = ['+','-','x','/']
    if showtext not in signs:
        text = text[:-1]
        newFactor = factors[:-1][:-1]
        factors = factors[:-1]
        factors.append(newFactor)
    else:
        sign = 0
    showtext = showtext[:-1]
    txt.configure(text=showtext)

def clear():
    global showtext
    global text
    global sign
    global painel
    global factors
    showtext = ''
    txt.configure(text=showtext)
    factors = []
    sign = 0

# create buttons
plus = Button(root, text='+', height='2', width='8', command=lambda:SetSign(1))
minus = Button(root, text='-', height='2', width='8', command=lambda:SetSign(2))
multiply = Button(root, text='x', height='2', width='8', command=lambda:SetSign(3))
divide = Button(root, text='/', height='2', width='8', command=lambda:SetSign(4))
potency = Button(root, text='**', height='2', width='8', command=lambda:SetSign(5))
equal = Button(root, text='=', height='2', width='8',command=Result)
num0 = Button(root, text='0', height='2', width='8', command=lambda:AddFactor('0'))
num1 = Button(root, text='1', height='2', width='8', command=lambda:AddFactor('1'))
num2 = Button(root, text='2', height='2', width='8', command=lambda:AddFactor('2'))
num3 = Button(root, text='3', height='2', width='8', command=lambda:AddFactor('3'))
num4 = Button(root, text='4', height='2', width='8', command=lambda:AddFactor('4'))
num5 = Button(root, text='5', height='2', width='8', command=lambda:AddFactor('5'))
num6 = Button(root, text='6', height='2', width='8', command=lambda:AddFactor('6'))
num7 = Button(root, text='7', height='2', width='8', command=lambda:AddFactor('7'))
num8 = Button(root, text='8', height='2', width='8', command=lambda:AddFactor('8'))
num9 = Button(root, text='9', height='2', width='8', command=lambda:AddFactor('9'))
dot = Button(root, text='.', height='2', width='8', command=lambda:AddFactor('.'))
rmv = Button(root, text='>', height='2', width='8', command=remove)
clr = Button(root, text='C', height='2', width='8', command=clear)
# place buttons
equal.place(x=165,y=250) 
plus.place(x=230,y=210)
minus.place(x=230,y=170)
multiply.place(x=230,y=130)
divide.place(x=230,y=250)
dot.place(x=35,y=250)
num0.place(x=100,y=250)
num1.place(x=35,y=210)
num2.place(x=100,y=210)
num3.place(x=165,y=210)
num4.place(x=35,y=170)
num5.place(x=100,y=170)
num6.place(x=165,y=170)
num7.place(x=35,y=130)
num8.place(x=100,y=130)
num9.place(x=165,y=130)
clr.place(x=35,y=90)
rmv.place(x=100,y=90)
potency.place(x=165,y=90)
# main loop
root.mainloop()