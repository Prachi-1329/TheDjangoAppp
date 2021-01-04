from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
 #   return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
from tkinter import*
gui = Tk()
gui.geometry('650x650')
gui.configure(bg='pink')
gui.title("Registration Form")
lbl_0 = Label(gui, text="Register Yourself!",bg='pink',width=20,font=("bold", 25))
lbl_0.place(x=100,y=63)
lbl_1 = Label(gui, text="Name",width=20,bg='pink',font=("bold", 14))
lbl_1.place(x=90,y=140)
tbt_1 = Entry(gui)
tbt_1.place(x=250,y=140)
lbl_2 = Label(gui, text="Email",width=20,bg='pink',font=("bold", 14))
lbl_2.place(x=78,y=190)
tbt_2 = Entry(gui)
tbt_2.place(x=250,y=190)
lbl_3 = Label(gui, text="Gender",width=20,bg='pink',font=("bold", 14))
lbl_3.place(x=80,y=240)
var = IntVar()
Radiobutton(gui, text="Male",padx = 5,bg='pink', variable=var, value=1).place(x=245,y=240)
Radiobutton(gui, text="Female",padx = 20,bg='pink', variable=var, value=2).place(x=300,y=240)
lbl_4 = Label(gui, text="Age:",width=20,bg='pink',font=("bold", 14))
lbl_4.place(x=80,y=290)
tbt_2 = Entry(gui)
tbt_2.place(x=250,y=290)
Button(gui, text='Submit',width=30,bg='grey',fg='black').place(x=190,y=390)
gui.mainloop()
print("registration form  seccussfully created...")
