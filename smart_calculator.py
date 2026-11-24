import tkinter as tk
import math
window=tk.Tk()
window.title("smart Calculator")
window.geometry("420x600")
window.config(bg="black")
history=[]
entry=tk.Entry(window,font=("Arial",20),justify="right",bg="white")
entry.pack(fill="x",padx=10,pady=10,ipady=10)
def append(value):
    entry.insert(tk.END,value)
def clear():
    entry.delete(0,tk.END)
def calculate():
    try:
        expr=entry.get()
        expr=expr.replace("sqrt(","math.sqrt(")
        expr=expr.replace("%","/100")
        if "math.sqrt("in expr and not expr.endswith(")"):
            expr=expr+")"
        result=str(eval(expr))
        history.append(entry.get()+"="+result)
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
def show_history():
    entry.delete(0,tk.END)
    if len(history)==0:
        entry.insert(0,"No History")
    else:
        entry.insert(0,history[-1])
frame=tk.Frame(window,bg="black")
frame.pack()
buttons=[
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
    "C","sqrt","%","History"
]
row=0
col=0
for char in buttons:
    if char =="C":
        b=tk.Button(frame,text=char,width=5,height=2,font=("Arial",16),bg="red",fg="white",command=clear)
    elif char =="=":
        b=tk.Button(frame,text=char,width=5,height=2,font=("Arial",16),bg="orange",fg="white",command=calculate)
    elif char=="sqrt":
        b=tk.Button(frame,text=char,width=5,height=2,font=("Arial",16),bg="purple",fg="white",command=lambda:append("sqrt("))
    elif char=="History":
        b=tk.Button(frame,text=char,width=5,height=2,font=("Arial",16),bg="blue",fg="white",command=show_history)
    else:
        b=tk.Button(frame,text=char,width=5,height=2,font=("Arial",16),bg="white",command=lambda c=char:append(c))
    b.grid(row=row,column=col,sticky="nsew",padx=2,pady=2)
    col+=1
    if col>3:
        col=0
        row+=1
window.mainloop()
    

