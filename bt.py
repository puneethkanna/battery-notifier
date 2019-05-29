from tkinter import *
from tkinter import messagebox
import colour
#import tkFontChooser
import tkinter as tk
import psutil
from win10toast import ToastNotifier
import time
#import webbrowser
#import atexit
import threading 
#import on
#import off
global tim
def on_closing():
    exit(0)
    root.destroy()
def get_det():
    ''''try:
        stop_threads = True
        t1.join()
    except:
        pass
        stop_threads = False'''
    print("Program entered into get_det")
    try:
        stop_threads = True
        t1.join()
        stop_threads = False
        print("Previous thread stopped.")
    except:
        stop_threads = False
        pass
    t1 = threading.Thread(target=on, args=(plugged, f,))
    #on(plugged, f)
    t1.start()
  # msg = messagebox.showinfo( "Hello Python", "Hello World")
def sel():
    print("Progrm entered into sel")
    selection = "You selected the option " + str(var.get())
    tim = str(var.get())
    print(tim)
    label.config(text = selection)
   #button = tk.Button(frame, text="Go", command=self.get_input, width=15)
# Button that calls get_input function when pressed
#self.top.bind_all("<Return>", self.get_input)
# Binds the Enter/Return key on your keyboard to the get_input function as an alternative to clicking the button
print("This program started on"+time.ctime())
#totalnoti=
""""
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
   
    print(int(flag) + 1)"""
#ptest()
def on(plugged,f):
    print("In ON")
    if stop_threads: 
        last_func()
    if(plugged == "Plugged In"):
        print(f)
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        t=int(battery.percent)
        if plugged == False:
            plugged = "Not Plugged In"
            off(plugged, t)
        else:
            plugged = "Plugged In"
    #flag = percent
    #print(percent)
        if(int(percent) != f+int(selection)):
            print("Changed ON")
            toaster = ToastNotifier()
            toaster.show_toast(plugged, percent)
            percent = str(battery.percent)
            f = int(percent)
            
        time.sleep(5)
        on(plugged, t)
    else:
        off(plugged, f)
#on(plugged,f,selection)
#flag = percent
#f=int(percent)
def off(plugged,f):
    if stop_threads: 
        last_func()
    print("In OFF")
    if(plugged == "Not Plugged In"):
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        t=int(battery.percent)
        if plugged == False:
            plugged = "Not Plugged In"
        else:
            plugged = "Plugged In"
            on(plugged, t)
    #flag = percent
        if(f-int(selection) != int(percent)):
            print("Changed OFF")
            toaster = ToastNotifier()
            toaster.show_toast(plugged, percent)
            f = int(percent)
            #if stop_threads: 
             #   last_func()
        time.sleep(5)
        off(plugged, t)
    else:
        on(percent,f)
def last_func():
    print("")
#print("The code had stopped if you want to use it run it again\n")
#battery = psutil.sensors_battery()
#plugged = battery.power_plugged
#percent = str(battery.percent)
#if plugged == False:
#    plugged = "Not Plugged In"
#else:
#    plugged = "Plugged In"
        # print(percent + '% | ' + plugged)
        # if __name__ == "__main__":
#toaster = ToastNotifier()
#toaster.show_toast(plugged, percent)
#flag = percent
#f = int(flag)
#print(f)
global stop_threads
stop_threads = False
if __name__ == "__main__": 
    top = Tk()
    top.title("Battery Notifier")
    top.geometry("600x500")
#w = tk.Tk()
    sam = "For Every certain percent decrease of battery you get notification.\n\n\n"
    msg = tk.Message(top, text = sam)
    msg.config(bg='white', font=('times', 20, 'italic'), relief = FLAT)
#w.pack(fill=X)
#msg.place(x = 50,y = 50)
    msg.pack(fill = X,padx=5, pady=10, side=TOP)
    var = StringVar()
""""
while True:
    event=wait_for_event()
    event.process()
    if main_window_has_been_destroyed():
        break
"""
#label = Label( top, textvariable = var, relief = RAISED )

#var.set("For Every certain percent decrease of battery you get notification.\n\n\n",)
#label.pack()
var = IntVar()
R1 = Radiobutton(top, text = "1%", variable = var, value = 1,command = sel)
R1.pack( anchor = W )

R2 = Radiobutton(top, text = "2%", variable = var, value = 2,command = sel)
R2.pack( anchor = W )

R3 = Radiobutton(top, text = "20%", variable = var, value = 20,command = sel)
R3.pack( anchor = W)
R4 = Radiobutton(top, text = "25%", variable = var, value = 25,command = sel)
R4.pack( anchor = W )
"""""
R1.place(x = 25,y = 75)
R2.place(x = 25,y = 95)
R3.place(x = 25,y = 115)"""""
selection = str(var.get())
label = Label(top)
label.pack()
B = Button(top, text = "OK", command = get_det)
B.place(x = 400,y = 300)
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
if plugged == False:
    plugged = "Not Plugged In"
else:
    plugged = "Plugged In"
        # print(percent + '% | ' + plugged)
        # if __name__ == "__main__":
toaster = ToastNotifier()
#toaster.show_toast(plugged, percent)
flag = percent
f = int(flag)
print(f)
t1 = threading.Thread(target=on, args=(plugged, f,))
try:
    stop_threads = True
    t1.join()
except:
    stop_threads = False
    pass
#off(plugged,f,selection)
top.protocol("WM_DELETE_WINDOW", on_closing)

top.mainloop()
#atexit.register(top.mainloop)
"""
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.minsize(600, 500)
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()
"""
