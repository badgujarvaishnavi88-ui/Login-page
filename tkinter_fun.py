from tkinter import *
from tkinter import messagebox
#Create the main window
base = Tk()
base.geometry("550x550")
base.title('Registration Form')

#Label for the title
lbl_0=Label(base,text="Registration Form",bg="white",width=20,font=("bold",20))
lbl_0.place(x=90,y=60)

#Label and Entry for full name
lbl_1=Label(base,text="Full Name",bg="black",fg="white",cursor="heart",width=10,font=("bold",10))
lbl_1.place(x=80,y=130)
enter_1=Entry(base)
enter_1.place(x=240,y=130)

#Label and Entry for Email
lbl_3=Label(base,text="Email",bg="black",fg="white",cursor="heart",width=10,font=("bold",10))
lbl_3.place(x=80,y=180)
enter_3=Entry(base)
enter_3.place(x=240,y=180)

#Label for Gender
lbl_4=Label(base,text="Gender",bg="black",fg="white",width=10,cursor="heart",font=("bold",10))
lbl_4.place(x=80,y=230)
vars=IntVar()
Radiobutton(base,text="Male",padx=5,variable=vars,value=1).place(x=235,y=230)
Radiobutton(base,text="Female",padx=20,variable=vars,value=2).place(x=290,y=230)

#Label for Country
lbl_5=Label(base,text="county",cursor="heart",bg="black",fg="white",width=10,font=("bold",10))
lbl_5.place(x=80,y=280)
list_of_cntry=['India','Canda','US','Germany','UK']
cv=StringVar()
drplist=OptionMenu(base,cv,*list_of_cntry)
drplist.config(width=20)
cv.set('Select your Country')
drplist.place(x=240,y=280)

#Label for language
lbl_6=Label(base,text="Language",bg="black",fg="white",cursor="heart",width=10,font=("bold",10))
lbl_6.place(x=80,y=330)
vars1=IntVar()
Checkbutton(base,text="English",cursor="cross",variable=vars1).place(x=240,y=330)
vars2=IntVar()
Checkbutton(base,text="German",cursor="cross",variable=vars2).place(x=300,y=330)

#Function for the submit button
def clicked():
    messagebox.showinfo('Message','Registration Successful!')

#Submit button
Button(base,text='submit',width=20,bg="black",fg="white",command=clicked,cursor="clock").place(x=180,y=380)

#Start the Tknter event loop
base.mainloop()
