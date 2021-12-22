'''secure password checker uses api tp get the hash list and compares it offline Git:PrakashDanabal'''
from tkinter import *
from passwordChecker import password_check


root =Tk()
root.title('Password_Check')
root.geometry('300x200') 
label_password=Label(root,text='Enter Password')
password=Entry(root,show='*')
label_result=Label(root,text=" ")
label_password.grid(row=0,column=0)
label_result.grid(row=2,column=0)
password.grid(row=1,column=0)



def checkpwd(): 
    result=password_check(password.get())
    if result=='green' or result=='red':
        password.config(bg=result)
        if result=='green':
            label_result.config(text= 'Hard Password')
        else:
            label_result.config(text='Weak Password')
    else:
        password.config(bg='yellow')



button_check=Button(root,command=checkpwd,text='Check')
button_check.grid(row=1,column=1)
root.mainloop()
