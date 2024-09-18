from tkinter import *
import calendar
screen=Tk()
screen.geometry("600x600")
screen.title("Calendar app📅")
screen.config(background="MediumPurple1")
def newscreen():
    screen2=Tk()
    screen2.geometry("600x600")
    screen2.title("year things 📅")
    screen2.config(background="SeaGreen1")
    year=int(clickyear.get())
    calendartext=calendar.calendar(year)
    displaycalendar=Label(screen2,text=calendartext,bg="SlateBlue1",fg="DarkSlateBlue",font=("chick",10,"bold"),justify="right")
    displaycalendar.grid(row=1,column=1,padx=60)
    screen2.mainloop()
caltitle=Label(screen,text="CALENDAR",bg="MediumPurple1",fg="gray1",font=("chick",35,"bold"))
yearinput=Label(screen,text="enter your year",bg="MediumPurple1",fg="gray1",font=("forte",16))
clickyear=Entry(screen)
button=Button(screen,text="submit",bg="HotPink",fg="gray1",font=("chick",10,"bold"),command=newscreen)
button.grid(row=4,column=1,padx=230,pady=50)
yearinput.grid(row=2,column=1,padx=230,pady=40)
caltitle.grid(row=1,column=1,padx=150)
clickyear.grid(row=3,column=1,padx=230)
screen.mainloop()
#Homework:
#Build the enemy snake and 