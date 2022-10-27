import tkinter as tk    #used as Gui
from math import *      #used for some math

#calculator
min_size_of_the_window=[300, 350]       
max_size_of_the_window=[800, 800]
label_color_text='#ffffff'
label_color="#80aaff"
entry_color_text='#ffffff'
entry_color='#80aaff'
botton_color_text='black'
bottom_color_number="#ccddff"
bottom_color_others="#b3ccff"
label_for_beauty_color_text="black"
label_result_color="white"

class Calculator:
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("Calculator")
        #size of window
        self.win.geometry('300x350')
        self.win.minsize(min_size_of_the_window[0], min_size_of_the_window[1])
        self.win.maxsize(max_size_of_the_window[0], max_size_of_the_window[1])

        self.create_upper_part()
        self.create_button_numbers()
        self.create_button_others()
        self.stretch_buttons()
    def run(self):
        self.win.mainloop()
    def create_button_others(self):
        tk.Button(text="0",command=lambda:self.put_number("0"),fg=botton_color_text,bg=bottom_color_number).grid(row=7, column=1,sticky="NSEW")
        tk.Button(text='C',command=lambda:self.clear_all(),fg=botton_color_text,bg=bottom_color_others).grid(row=2,column=2,stick='wens')
        tk.Button(text='Del',fg=botton_color_text,bg=bottom_color_others,command=lambda:self.delete_last()).grid(row=2,column=3,stick='wens')
        tk.Button(text='1/x',fg=botton_color_text,bg=bottom_color_others, command=lambda:self.denominator()).grid(row=3,column=0,stick='wens')
        tk.Button(text='x^2',fg=botton_color_text,bg=bottom_color_others,command=lambda:self.square()).grid(row=3,column=1,stick='wens')
        tk.Button(text='√x',fg=botton_color_text,bg=bottom_color_others, command=lambda:self.root()).grid(row=3,column=2,stick='wens')
        tk.Button(text='/',fg=botton_color_text,command=lambda:self.put_number("/"),bg=bottom_color_others).grid(row=3,column=3,stick='wens')
        tk.Button(text='*',fg=botton_color_text,command=lambda:self.put_number("*"),bg=bottom_color_others).grid(row=4,column=3,stick='wens')
        tk.Button(text='-',fg=botton_color_text,command=lambda:self.put_number("-"),bg=bottom_color_others).grid(row=5,column=3,stick='wens')
        tk.Button(text='+',fg=botton_color_text,command=lambda:self.put_number("+"),bg=bottom_color_others).grid(row=6,column=3,stick='wens')
        tk.Button(text='.',fg=botton_color_text,command=lambda:self.point(),bg=bottom_color_others).grid(row=7,column=2,stick='wens')
        tk.Button(text='+/-',fg=botton_color_text,bg=bottom_color_others,command=lambda:self.change_plus_and_minus()).grid(row=7,column=0,stick='wens')
        tk.Button(text='=',fg=botton_color_text,command=lambda:self.equal(),bg=bottom_color_others).grid(row=7,column=3,stick='wens') 
    def create_upper_part(self):
        self.label=tk.Label(text='0',font=('Arial',16),bd=0,fg=label_color_text,anchor='e',bg=label_color)
        self.entry=tk.Entry(font=('Arial',9),fg=entry_color_text,bd=0,bg=entry_color,justify=tk.RIGHT)
        self.entry.insert(0,'0')
        self.label_for_beauty=tk.Label(font=('Arial',14),text="Calculator",fg=label_for_beauty_color_text,bd=0,bg="#b3ccff",justify=tk.RIGHT)

        self.entry.grid(row=0,column=0,columnspan=4,stick='wens')
        self.label.grid(row=1,column=0,columnspan=4,stick='wens')
        self.label_for_beauty.grid(row=2,column=0,columnspan=2,stick='wens')
    def create_button_numbers(self):
        array=["1","2","3","4","5","6","7","8","9"] 
        count=0
        for i in range (6,3,-1):
            for j in range(3):
                tk.Button(text=array[count],command=lambda x=count:self.put_number(array[x]),fg=botton_color_text,bg=bottom_color_number).grid(row=i, column=j,sticky="NSEW")
                count+=1   
    def stretch_buttons(self):
        for i in range (2,8):
            for j in range(4):
                tk.Grid.rowconfigure(self.win,i,weight=1)
                tk.Grid.columnconfigure(self.win,j,weight=1)
        tk.Grid.rowconfigure(self.win,1,weight=1)
    def put_number(self, char):
        string_in_entry=self.entry.get()
        exceptions=["+","-","*","/"]
        if len(string_in_entry) == 1 and (char.isdigit() or char=="-") and string_in_entry[0]=='0':
            string_in_entry=string_in_entry[1:]
        if ((len(string_in_entry)!=0) and (char in exceptions) and (string_in_entry[-1] in exceptions)):
            pass
        else:
            self.change_entry_admin(string_in_entry+char)
    def equal(self):
        text_in_label=self.entry.get()
        if text_in_label=="0":
            pass
        else:
            self.entry.delete(0,tk.END)
            try:
                self.result=eval(text_in_label)
                self.result=str(self.result)
                if self.result[-1]=="0" and self.result[-2]==".":
                    self.result=self.result[0:-2]
                self.label.config(text=self.result)
                self.entry.insert(0,self.result)
            except (ValueError,ZeroDivisionError,SyntaxError,NameError) as ex:
                if str(ex)=="unexpected EOF while parsing (<string>, line 1)":
                    self.label.config(text='Error: cannot perform calculations')
                elif str(ex)=="division by zero": 
                    self.label.config(text='Error: division by zero') 
                else:
                    self.label.config(text='Error: Invalid values entered')
                self.entry.insert(0,'0')
    def clear_all(self):
        self.change_entry_admin("0")
        self.label.config(text='0')
    def point(self):
        result=str(self.entry.get())
        if (result[-1].isdigit())==False and result[-1]!=".":
            self.put_number("0.")
        else:
            toWrite=True
            for i in reversed(result):
                if i==".":
                    toWrite=False
                    break
                try:
                    a=int(i)
                    continue
                except:
                    break
            if  toWrite:
                self.put_number(".")
    def change_entry_admin(self, put_in):
        self.entry.delete(0,tk.END)
        self.entry.insert(0,put_in)
    def square(self):
        self.change_entry_admin('('+self.entry.get()+')**2')
    def delete_last(self):
        text=self.entry.get()
        self.entry.delete(0,tk.END)
        if len(text)==1:
            self.entry.insert(0,'0')
        else:
            text=text[:-1]
            self.entry.insert(0,text)
    def denominator(self):
        self.change_entry_admin("1/("+self.entry.get()+")")
    def root(self):
        self.change_entry_admin("sqrt("+self.entry.get()+")") 
    def change_plus_and_minus(self):
        self.change_entry_admin("-("+self.entry.get()+")") 

#create a window
Calc=Calculator()
Calc.run()