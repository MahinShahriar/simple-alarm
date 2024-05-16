# Import Required Library
import datetime
import time
import pygame
from threading import *
from tkinter import *

# Create the main clock window
clock = Tk()
clock.title("Mahin's Clock")
clock.geometry("500x300")

# Function to stop the alarm and destroy the stop button
def stop_alarm():
    global stop_button
    print("Alarm Stopped!")
    pygame.mixer.music.stop()
    stop_button.destroy()

# Function to trigger the alarm at the set time
def alarm(set_alarm_timer):
    global stop_button
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            pygame.mixer.init()
            pygame.mixer.music.load("itihash.mp3")
            pygame.mixer.music.play()
            stop_button = Button(clock, text="Stop Alarm", command=stop_alarm, bg="red", fg="white", relief="raised", font=("Arial", 12, "bold"))
            stop_button.place(x=220, y=120, width=100, height=50)
            break

# Function to set the alarm time based on user input
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}"
    alarm(set_alarm_timer)

# Create labels and input fields for setting the alarm time
time_format = Label(clock, text="Enter time in 24-hour format:", fg="blue", font=("Arial", 14))
time_format.place(x=50, y=20)

add_time_label = Label(clock, text="Hour  Min", font=("Arial", 12))
add_time_label.place(x=150, y=50)

set_your_alarm_label = Label(clock, text="When to wake you up", fg="orange", relief="solid", font=("Helvetica", 16, "bold"))
set_your_alarm_label.place(x=50, y=50)

hour = StringVar()
min = StringVar()

def on_hour_entry_click(event):
    hour_entry.config(state="normal")
    if hour_entry.get() == "hh":
        hour_entry.delete(0, "end")

def on_min_entry_click(event):
    min_entry.config(state="normal")
    if min_entry.get() == "min":
        min_entry.delete(0, "end")



hour_entry = Entry(clock, textvariable=hour, fg="black", bg="lightgray", font=("Arial", 14), width=10)
hour_entry.insert(0, "hh")  # Set default text for hour entry
hour_entry.bind("<FocusIn>", on_hour_entry_click)
hour_entry.bind("<FocusOut>", lambda event: hour_entry.insert(0, "hh") if not hour_entry.get() else None)  # Restore default text if no input
hour_entry.config(state="readonly")  # Disable editing
hour_entry.place(x=150, y=80)

min_entry = Entry(clock, textvariable=min, fg="black", bg="lightgray", font=("Arial", 14), width=5)
min_entry.insert(0, "min")  # Set default text for minute entry
min_entry.bind("<FocusIn>", on_min_entry_click)
min_entry.bind("<FocusOut>", lambda event: min_entry.insert(0, "min") if not min_entry.get() else None)  # Restore default text if no input
min_entry.config(state="readonly")


min_entry.place(x=200, y=80)


submit_button = Button(clock, text="Set Alarm", fg="white", bg="green", font=("Arial", 14, "bold"), command=actual_time)
submit_button.place(x=100, y=120, width=100, height=50)

clock.mainloop()
