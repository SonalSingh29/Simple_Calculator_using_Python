from tkinter import *

scr=Tk()
e=Entry(scr,font=('times',20,'bold'),bg='yellow')
e.grid(row=0,columnspan=3)
def eq():
    try:
        s=eval(e.get())
    except:
        s=0
    e.delete(0,END)
    e.insert(0,s)


b=Button(scr,text='1',command=lambda :e.insert(END,'1'),font=('times',20,'bold'),bg='yellow',width=5)
b.grid(row=1,column=0)
b1=Button(scr,text='2',command=lambda :e.insert(END,'2'),font=('times',20,'bold'),bg='yellow',width=5)
b1.grid(row=1,column=1)
b2=Button(scr,text='3',command=lambda :e.insert(END,'3'),font=('times',20,'bold'),bg='yellow',width=5)
b2.grid(row=1,column=2)

b3=Button(scr,text='4',command=lambda :e.insert(END,'4'),font=('times',20,'bold'),bg='yellow',width=5)
b3.grid(row=2,column=0)
b4=Button(scr,text='5',command=lambda :e.insert(END,'5'),font=('times',20,'bold'),bg='yellow',width=5)
b4.grid(row=2,column=1)
b5=Button(scr,text='6',command=lambda :e.insert(END,'6'),font=('times',20,'bold'),bg='yellow',width=5)
b5.grid(row=2,column=2)

b6=Button(scr,text='7',command=lambda :e.insert(END,'7'),font=('times',20,'bold'),bg='yellow',width=5)
b6.grid(row=3,column=0)
b7=Button(scr,text='8',font=('times',20,'bold'),bg='yellow',command=lambda :e.insert(END,'8'),width=5)
b7.grid(row=3,column=1)
b8=Button(scr,text='9',command=lambda :e.insert(END,'9'),font=('times',20,'bold'),bg='yellow',width=5)
b8.grid(row=3,column=2)

b9=Button(scr,text='+',command=lambda :e.insert(END,'+'),font=('times',20,'bold'),bg='yellow',width=5)
b9.grid(row=4,column=0)
b10=Button(scr,text='0',command=lambda :e.insert(END,'0'),font=('times',20,'bold'),bg='yellow',width=5)
b10.grid(row=4,column=1)
b11=Button(scr,text='-',command=lambda :e.insert(END,'-'),font=('times',20,'bold'),bg='yellow',width=5)
b11.grid(row=4,column=2)

b12=Button(scr,text='*',command=lambda :e.insert(END,'*'),font=('times',20,'bold'),bg='yellow',width=5)
b12.grid(row=5,column=0)
b13=Button(scr,text='/',command=lambda :e.insert(END,'/'),font=('times',20,'bold'),bg='yellow',width=5)
b13.grid(row=5,column=1)
b14=Button(scr,text='**',command=lambda :e.insert(END,'**'),font=('times',20,'bold'),bg='yellow',width=5)
b14.grid(row=5,column=2)

b15=Button(scr,text='clr',command=lambda :e.delete(0,END),font=('times',20,'bold'),bg='yellow',width=5)
b15.grid(row=6,column=0)
b16=Button(scr,text='%',command=lambda :e.insert(END,'%'),font=('times',20,'bold'),bg='yellow',width=5)
b16.grid(row=6,column=1)
b17=Button(scr,text='=',command=eq,font=('times',20,'bold'),bg='yellow',width=5)
b17.grid(row=6,column=2)

scr.mainloop()

