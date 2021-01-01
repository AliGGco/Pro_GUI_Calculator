#imports                                                                                        #imports
from tkinter import * 
import math
#main root                                                                                      #main root
root = Tk()
root.geometry("400x375")
root.resizable(0, 0)
root.title("pro_Calculator")
#root.icon()
#Entery           
expression = StringVar(root, "0")  
calculated = StringVar(root)                                                                            #Entery 
E = Entry(root, justify=RIGHT, selectbackground="#D9D9D9",
                       font="Comic-sens 15 bold", selectforeground="#000000", readonlybackground="#D9D9D9", relief=FLAT,
                       bd=0,)
E.grid(row= 0, column= 0,padx= 50, pady=20, columnspan= 4)

def my_click(number):
    global current
    current = E.get()
    E.delete(0, END)
    E.insert(0, str(current) + str(number))
#cot/cos/tan/sin                                                                                #cot/cos/tan/sin
def sin_click():
    current = E.get()
    current = float(current)
    ans = round(math.sin(math.radians(current)),1)
    E.delete(0, END)
    E.insert(0, ans)
    
def cos_click():
    current = E.get()
    current = float(current)
    ans = round(math.cos(math.radians(current)),1)
    E.delete(0, END)
    E.insert(0, ans)
def cot_click():
    current = E.get()
    current = float(current)
    ans = round(math.tan(math.radians(current)),1)
    ans1 = round(1/ans,1)
    E.delete(0, END)
    E.insert(0, ans1)
def tan_click():
    current = E.get()
    current = float(current)
    ans = round(math.tan(math.radians(current)),1)
    E.delete(0, END)
    E.insert(0, ans)
#%/CE/C/<x                                                                                      #%/CE/C/<x
def percent_click():
    current = E.get()
    current = float(current)
    E.delete(0, END)
    ans = (current/ 100)
    E.insert(0, ans)
def CE_click():
    E.delete(0, END)
def C_click():
    E.delete(0, END)
def clear1_click():
    pos = len(E.get())
    display = str(E.get())
    if display == '':
        E.insert(0, '0')
    elif display == ' ':
        E.insert(0, '0')
    elif display == '0':
        pass
    else:
        E.delete(0, END)
        E.insert(0, display[0:pos-1])       
#1/x/x^2/radical/devision                                                                       #1/x/x^2/radical/devision
def onex_click():
    current = E.get()
    first_num = float(current)
    second_number = (float(1))
    ans = (second_number / first_num)
    E.delete(0, END)
    E.insert(0, ans)
    
def power_click():
    first_number = E.get()
    global first_num
    global math
    math = "power"
    first_num = float(first_number)
    E.delete(0, END)
def radical_click():
    current = float(E.get())
    ans = math.sqrt(current)
    E.delete(0, END)
    E.insert(0, ans)

def devision_click():
    first_number = E.get()
    global first_num
    global math
    math = "devision"
    first_num = float(first_number)
    E.delete(0, END)
#multiply/substract/add                                                                         #multiply/substract/add
def multiply_click():
    first_number = E.get()
    global first_num
    global math
    math = "multiplication"
    first_num = float(first_number)
    E.delete(0, END)
def substract_click():
    first_number = E.get()
    global first_num
    global math
    math = "subtraction"
    first_num = float(first_number)
    E.delete(0, END)
def add_click():
    first_number = E.get()
    global first_num
    global math
    math = "addition"
    first_num = float(first_number)
    E.delete(0, END)
#-/dote                                                                                         #-/dote
def negative_click():
    E.insert(0, "-")
def dote_click():
    current = E.get()
    E.delete(0, END)
    E.insert(-1, current + ".")
#equation                                                                                       #equation
def Equation_click():
    second_number = E.get()
    E.delete(0, END)
    sec_num = float(second_number)
    if math == "addition":
        E.insert(0, first_num + sec_num)
    elif math == "subtraction":
        E.insert(0, first_num - sec_num)
    elif math == "multiplication":
        E.insert(0, first_num * sec_num)
    elif math == "devision":
        E.insert(0, first_num / sec_num)
    elif math == "power":
        E.insert(0, first_num ** sec_num)    
    
        

#numbers defenition
#                                                                              #numbers defenition
Button_num0 = Button(root, text="0", padx= 43, pady= 10, command= lambda: my_click(0))
Button_num1 = Button(root, text="1", padx= 42, pady= 10, command= lambda: my_click(1))
Button_num2 = Button(root, text="2", padx= 43, pady= 10, command= lambda: my_click(2))

Button_num3 = Button(root, text="3", padx= 41, pady= 10, command= lambda: my_click(3))
Button_num4 = Button(root, text="4", padx= 42, pady= 10, command= lambda: my_click(4))
Button_num5 = Button(root, text="5", padx= 43, pady= 10, command= lambda: my_click(5))

Button_num6 = Button(root, text="6", padx= 41, pady= 10, command= lambda: my_click(6))
Button_num7 = Button(root, text="7", padx= 41.5, pady= 10, command= lambda: my_click(7))
Button_num8 = Button(root, text="8", padx= 43, pady= 10, command= lambda: my_click(8))
Button_num9 = Button(root, text="9", padx= 41, pady= 10, command= lambda: my_click(9))
#cot/cos/tan/sin                                                                                #cot/cos/tan/sin 
Button_sin = Button(root, text="sin", padx= 38, pady= 10,bg= "#d3d3d3", command= sin_click)
Button_cos = Button(root, text="cos", padx= 38, pady= 10,bg= "#d3d3d3", command= cos_click)
Button_tan = Button(root, text="tan", padx= 38, pady= 10,bg= "#d3d3d3", command= tan_click)
Button_cot = Button(root, text="cot", padx= 36, pady= 10,bg= "#d3d3d3", command= cot_click)
#%/CE/C/<x                                                                                      #%/CE/C/<x
Button_percent = Button(root, text="%", padx= 40, pady= 10,bg= "#d3d3d3", command= percent_click )
Button_CE = Button(root, text="CE", padx= 40, pady= 10,bg= "#d3d3d3", command= CE_click )
Button_C = Button(root, text="C", padx= 40, pady= 10,bg= "#d3d3d3", command= C_click )
Button_clear1 = Button(root, text="<x", padx= 39, pady= 10,bg= "#d3d3d3", command= clear1_click )
#1/x/x^2/radical/devision                                                                       #1/x/x^2/radical/devision
Button_1x = Button(root, text="1/x", padx= 36, pady= 10,bg= "#d3d3d3", command= onex_click)
Button_power = Button(root, text="^", padx= 43, pady= 10,bg= "#d3d3d3", command= power_click)
Button_radical = Button(root, text="√", padx= 40, pady= 10,bg= "#d3d3d3", command= radical_click)
Button_devision = Button(root, text="/", padx= 43, pady= 10,bg= "#d3d3d3", command= devision_click)
#multiply/substract/add                                                                         #multiply/substract/add
Button_multiply = Button(root, text="X", padx= 42, pady= 10,bg= "#d3d3d3", command= multiply_click)
Button_substract = Button(root, text="-", padx= 43, pady= 10,bg= "#d3d3d3", command= substract_click)
Button_add = Button(root, text="+", padx= 42, pady= 10,bg= "#d3d3d3", command= add_click)
#-/dote                                                                                         #-/dote
Button_negative = Button(root, text="+/-", padx= 36, pady= 10,bg= "#d3d3d3", command= negative_click )
Button_dote = Button(root, text=".", padx= 43, pady= 10,bg= "#d3d3d3", command= dote_click)
#equation                                                                                       #equation
Button_equation = Button(root, text="=", padx= 42, pady= 10,bg= "#d3d3d3", command= Equation_click)

#griding
#griding numbers
Button_num1.grid(row=4, column= 0)
Button_num2.grid(row=4, column= 1)
Button_num3.grid(row=4, column= 2)

Button_num4.grid(row=5, column= 0)
Button_num5.grid(row=5, column= 1)
Button_num6.grid(row=5, column= 2)

Button_num7.grid(row=6, column= 0)
Button_num8.grid(row=6, column= 1)
Button_num9.grid(row=6, column= 2)
Button_num0.grid(row=7, column= 1)
#griding cot/cos/tan/sin 
Button_sin.grid(row=1, column= 0)
Button_cos.grid(row=1, column= 1)
Button_cot.grid(row=1, column= 2)
Button_tan.grid(row=1, column= 3)
#griding %/CE/C/<x
Button_percent.grid(row=2, column= 0)
Button_CE.grid(row=2, column= 1)
Button_C.grid(row=2, column= 2)
Button_clear1.grid(row=2, column= 3)
#griding 1/x/x^2/radical/devision
Button_1x.grid(row=3, column= 0)
Button_power.grid(row=3, column= 1)
Button_radical.grid(row=3, column= 2)
Button_devision.grid(row=3, column= 3)
#griding multiply/substract/add
Button_multiply.grid(row=4, column= 3)
Button_substract.grid(row=5, column= 3)
Button_add.grid(row=6, column= 3)
#griding -/dote equation
Button_negative.grid(row=7, column= 0)
Button_dote.grid(row=7, column= 2)
Button_equation.grid(row=7, column= 3)
root.mainloop()
