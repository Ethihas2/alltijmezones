from tkinter import *
import time
import pytz
from PIL import Image,ImageTk
from datetime import datetime

root = Tk()
root.title("Time zones")
root.geometry("900x1000")

img_india_var = ImageTk.PhotoImage(Image.open("india.png"))
img_usa = ImageTk.PhotoImage(Image.open("usa.png"))
img_australia_var = ImageTk.PhotoImage(Image.open("australia.png"))
img_japan_var = ImageTk.PhotoImage(Image.open("japan.png"))

label_india = Label(root,text="India")
label_india.place(relx=0.2,rely=0.01,anchor=CENTER)
img_india = Label(root,image=img_india_var)
img_india.place(relx=0.2,rely=0.2,anchor=CENTER)
time_label = Label(root)
time_label.place(relx=0.2,rely=0.4,anchor=CENTER)

label_USA = Label(root,text="USA")
label_USA.place(relx=0.75,rely=0.01,anchor=CENTER)
img_USA = Label(root,image=img_usa)
img_USA.place(relx=0.75,rely=0.2,anchor=CENTER)
time_USA = Label(root)
time_USA.place(relx=0.75,rely=0.4,anchor=CENTER)

label_australia = Label(root,text="Australia")
label_australia.place(relx=0.75,rely=0.5,anchor=CENTER)
img_australia = Label(root,image=img_australia_var)
img_australia.place(relx=0.75,rely=0.7,anchor=CENTER)
time_australia = Label(root)
time_australia.place(relx=0.75,rely=0.9,anchor=CENTER)

label_japan = Label(root,text="Japan")
label_japan.place(relx=0.2,rely=0.5,anchor=CENTER)
img_japan = Label(root,image=img_japan_var)
img_japan.place(relx=0.2,rely=0.7,anchor=CENTER)
time_japan = Label(root)
time_japan.place(relx=0.2,rely=0.9,anchor=CENTER)

class India():
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home) 
        current_time = local_time.strftime("%H:%M:%S")
        time_label["text"]="Time: "+current_time
        time_label.after(200,self.times)
        
class USA:
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_USA["text"]="Time: "+current_time
        time_USA.after(200,self.times)
class Australia:
    def times(self):
        home = pytz.timezone("Antarctica/Macquarie")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_australia["text"]="Time: "+current_time
        time_australia.after(200,self.times)
class Japan:
    def times(self):
        home = pytz.timezone("Asia/Tokyo")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_japan["text"]="Time: "+current_time
        time_japan.after(200,self.times)

obj_india = India()
obj_USA = USA()
obj_australia = Australia()
obj_japan = Japan()

button1 = Button(root,text="Show time",command=obj_india.times)
button1.place(relx=0.2,rely=0.45,anchor=CENTER)

button2 = Button(root,text="Show time",command=obj_USA.times)
button2.place(relx=0.75,rely=0.45,anchor=CENTER)

button3 = Button(root,text="Show time",command=obj_australia.times)
button3.place(relx=0.75,rely=0.95,anchor=CENTER)

button4 = Button(root,text="Show time",command=obj_japan.times)
button4.place(relx=0.2,rely=0.95,anchor=CENTER)
root.mainloop()