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

def radiciationFunction(a,b):
    return a**(1/b)

showtext = ''
text = ''

root = Tk()
root.geometry('400x400')
root.title('Calculator')
root.resizable(0,0)
root.iconbitmap('calculator_icon.ico')

canvas = Canvas(root, height=100, width=600, bg='#30302f')

painel = Frame(root)
painel.pack()
txt = Label(painel, text=showtext, fg='white', bg='#30302f')
txt.pack()
txt["font"] = ("Arial", "32", "bold")

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
        if Value == 6:
            showtext+='√'
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
        if sign == 6:
            result = radiciationFunction(a,b)
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
    text = ''
    showtext = ''
    txt.configure(text=showtext)
    factors = []
    sign = 0

# create buttons


potency = Button(root, text='**',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:SetSign(5))
radiciation = Button(root, text='√',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:SetSign(6))
equal = Button(root, text='=',font='arial, 12',fg='#314961', height='3', width='11',bg='#ffbe54',bd=1,command=Result)
num0 = Button(root, text='0',font='arial, 12',fg='#314961', height='3', width='21',bd=1, command=lambda:AddFactor('0'))
num1 = Button(root, text='1',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('1'))
num2 = Button(root, text='2',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('2'))
num3 = Button(root, text='3',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('3'))
num4 = Button(root, text='4',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('4'))
num5 = Button(root, text='5',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('5'))
num6 = Button(root, text='6',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('6'))
num7 = Button(root, text='7',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('7'))
num8 = Button(root, text='8',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('8'))
num9 = Button(root, text='9',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('9'))
dot = Button(root, text=',',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=lambda:AddFactor('.'))
rmv = Button(root, text='>',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=remove)
clr = Button(root, text='C',font='arial, 12',fg='#314961', height='3', width='10',bd=1, command=clear)
plus = Button(root, text='+',font='arial, 12',fg='#314961',height='3', width='11',bg='#ffbe54',bd=0.5, command=lambda:SetSign(1))
minus = Button(root, text='-',font='arial, 12',fg='#314961', height='3', width='11',bg='#ffbe54',bd=0.5, command=lambda:SetSign(2))
multiply = Button(root, text='x',font='arial, 12',fg='#314961', height='3', width='11',bg='#ffbe54',bd=0.5, command=lambda:SetSign(3))
divide = Button(root, text='/',font='arial, 12',fg='#314961', height='3', width='11',bg='#ffbe54',bd=0.5, command=lambda:SetSign(4))
# place buttons
equal.place(x=294,y=334) 
plus.place(x=294,y=268)
minus.place(x=294,y=202)
multiply.place(x=294,y=136)
divide.place(x=294,y=70)
dot.place(x=196,y=334)
num0.place(x=0,y=334)
num1.place(x=0,y=268)
num2.place(x=98,y=268)
num3.place(x=196,y=268)
num4.place(x=0,y=202)
num5.place(x=98,y=202)
num6.place(x=196,y=202)
num7.place(x=0,y=136)
num8.place(x=98,y=136)
num9.place(x=196,y=136)
clr.place(x=0,y=70)
#rmv.place(x=100,y=90)
potency.place(x=196,y=70)
radiciation.place(x=98,y=70)

canvas.place(x=-10,y=-10)

# main loop
root.mainloop()
