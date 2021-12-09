from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific calculator")
root.configure(background= "white")
root.resizable(width=FALSE,height=FALSE)
root.geometry('480x568+0+0')

calc=Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False

    def numberEnter(self,num):
        self.result= False
        firstnumber=txtDisplay.get()
        secondnumber=str(num)
        if self.input_value:
            self.current=secondnumber
            self.input_value=False
        else:
            if secondnumber=='.':
                if secondnumber in firstnumber:
                    return
            self.current=firstnumber+secondnumber
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self,value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="subtract":
            self.total-=self.current
        if self.op=="multiply":
            self.total*=self.current
        if self.op=="divide":
            self.total/=self.current
        if self.op=="Mod":
            self.total%=self.current
        if self.op=="**2":
            self.total=pow(self.current,2)

        self.input_value=True
        self.check_sum=False
        self.display(self.total)

    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def Clear_entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

    def all_clear_entry(self):
        self.Clear_entry()
        self.total=0

    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)

    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)

    def exp(self):
        self.result=False
        self.current=math.exp()
        self.display(self.current)

    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result=False
        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result=False
        self.current=math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def mathsPM(self):
        self.result=False
        self.current= -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
    def log(self):
        self.result=False
        self.current=math.log(float(txtDisplay.get()))
        self.display(self.current)

    def fact(self):
        self.result=False
        self.current=math.factorial(float(txtDisplay.get()))
        self.display(self.current)


added_value=Calc()


txtDisplay=Entry(calc,font=('arial',20,'bold'),bg="white",bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numberpad[i]: added_value.numberEnter(x)
        i+=1
#===============================#
btnClear=Button(calc,text=chr(67),width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
                command=added_value.all_clear_entry).grid(row=1,column=0,pady=1)

btnAllClear=Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
                   command=added_value.Clear_entry).grid(row=1,column=1,pady=1)

btnsq=Button(calc,text="sqrt" ,width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
             command=added_value.squared).grid(row=1,column=2,pady=1)

btnAdd=Button(calc,text="+",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=lambda :added_value.operation("add")).grid(row=1,column=3,pady=1)

btnSubtract=Button(calc,text="-",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
                   command=lambda :added_value.operation("subtract")).grid(row=2,column=3,pady=1)

btnmultiply=Button(calc,text="*",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
                   command=lambda :added_value.operation("multiply")).grid(row=3,column=3,pady=1)

btndivide=Button(calc,text=chr(247),width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
                 command=lambda :added_value.operation("divide")).grid(row=4,column=3,pady=1)

btnzero=Button(calc,text="0",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
               command=lambda :added_value.numberEnter(0)).grid(row=5,column=0,pady=1)

btndot=Button(calc,text=".",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=lambda :added_value.numberEnter(".")).grid(row=5,column=1,pady=1)

btnPM=Button(calc,text=chr(177),width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
             command=added_value.mathsPM).grid(row=5,column=2,pady=1)

btnEqual=Button(calc,text="=",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
                command=added_value.sum_of_total).grid(row=5,column=3,pady=1)
#===================================scientific calculator====================================#
btnPi=Button(calc,text="Pi",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
             command=added_value.pi).grid(row=1,column=4,pady=1)

btnsin=Button(calc,text="sin",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=added_value.sin).grid(row=2,column=4,pady=1)

btncos=Button(calc,text="cos" ,width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=added_value.cos).grid(row=3,column=4,pady=1)

btntan=Button(calc,text="tan",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=added_value.tan).grid(row=4,column=4,pady=1)

#================================================#
btnLog=Button(calc,text="Log",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=added_value.log).grid(row=5,column=4,pady=1)

btnsinh=Button(calc,text="sinh",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
               command=added_value.sinh).grid(row=1,column=5,pady=1)

btncosh=Button(calc,text="cosh" ,width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
               command=added_value.cosh).grid(row=2,column=5,pady=1)

btntanh=Button(calc,text="tanh",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
               command=added_value.tanh).grid(row=3,column=5,pady=1)

btnExp=Button(calc,text="Exp",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=added_value.exp).grid(row=4,column=5,pady=1)
btne=Button(calc,text="e",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
            command=added_value.e).grid(row=5,column=5,pady=1)

btnMod=Button(calc,text="Mod",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=lambda :added_value.operation("Mod")).grid(row=1,column=6,pady=1)

btnfact=Button(calc,text="fact",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=added_value.fact).grid(row=2,column=6,pady=1)

btnx=Button(calc,text="x^2",width=6,height=2,font=('arial',20,'bold'),bd=4,bg='white',
              command=lambda :added_value.operation("**2")).grid(row=3,column=6,pady=1)

lbldisplay=Label(calc,text="Scientific caculator",font=('arial',30,'bold'),justify=CENTER)
lbldisplay.grid(row=0,column=4,columnspan=4)
#====================MENU==========================#
def iExit():
    iExit=tkinter.messagebox.askyesno("Scientific calculator","Confirm if you want to exit")
    if iExit >0:
        root.destroy()
        return

def Standard():
    root.resizable(width=FALSE, height=FALSE)
    root.geometry('480x568')

def Scientific():
    root.resizable(width=FALSE, height=FALSE)
    root.geometry('944x568')

menubar=Menu(calc)


menubar.add_cascade(label="Standard",command=Standard)
menubar.add_cascade(label="Scientific",command=Scientific)
menubar.add_separator()
menubar.add_cascade(label="Exit",command=iExit)

root.configure(menu=menubar)
root.mainloop()
