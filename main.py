# Code-Busters
import tkinter as tk
from tkinter import ttk
import datetime

# Create the main window
root = tk.Tk()
root.title("Health Management Software")
root.geometry("500x500")

# Use a new font and a different theme
font = ("Arial", 14)
style = ttk.Style(root)
style.theme_use("clam")

# Define a function to handle emergency alerts
def emergency_alert():
    alert = tk.Toplevel(root)
    alert.title("Emergency Alert")
    alert.geometry("300x200")
    tk.Label(alert, text="EMERGENCY ALERT!", font=("Helvetica", 16), foreground="red").pack()
    tk.Button(alert, text="OK", command=alert.destroy, font=font).pack()

# Define a function to handle appointment scheduling
def schedule_appointment():
    appointment = tk.Toplevel(root)
    appointment.title("Appointment Scheduler")
    appointment.geometry("400x300")
    tk.Label(appointment, text="Appointment Date:", font=font).pack()
    date = tk.Entry(appointment, font=font)
    date.pack()
    tk.Label(appointment, text="Appointment Time:", font=font).pack()
    time = tk.Entry(appointment, font=font)
    time.pack()
    tk.Label(appointment, text="Appointment Description:", font=font).pack()
    description = tk.Entry(appointment, font=font)
    description.pack()
    tk.Button(appointment, text="Save", command=lambda: save_appointment(date.get(), time.get(), description.get()), font=font).pack()

# Define a function to save appointments to a file
def save_appointment(date, time, description):
    with open("appointments.txt", "a") as file:
        file.write(f"{date} {time}: {description}\n")
    appointment.destroy()

# Create the buttons for emergency alerts and appointment scheduling
tk.Button(root, text="Emergency Alert", command=emergency_alert, font=font).pack()
tk.Button(root, text="Schedule Appointment", command=schedule_appointment, font=font).pack()

# Start the main event loop
root.mainloop()
