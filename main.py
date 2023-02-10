import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import uuid

class Patient:
    def _init_(self, name, age, symptoms, emergency_contact, appointment_time):
        self.id = str(uuid.uuid4().int)[:10]
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.emergency_contact = emergency_contact
    
    def display_info(self):
        return "ID:" + self.id + "\nName:" + self.name + "\nAge:" + self.age + "\nSymptoms:" + self.symptoms + "\nEmergency Contact:" + self.emergency_contact 

def patient_info():
    name = name_entry.get()
    age = age_entry.get()
    symptoms = symptoms_entry.get()
    emergency_contact = emergency_contact_entry.get()
    return Patient(name, age, symptoms, emergency_contact)
    

def schedule_appointment():
    appointment_window = tk.Toplevel(root)
    appointment_window.title("Appointment Scheduler")
    appointment_window.geometry("500x400")
    appointment_window.config(bg='#CAF4F4')

    label_font = ('delight coffee', 14)

    tk.Label(appointment_window, text="Appointment Date:", font=label_font).pack()
    date = tk.Entry(appointment_window, bg='light sky blue')
    date.pack(pady=20)
    tk.Label(appointment_window, text="Appointment Time:", font=label_font).pack()
    time = tk.Entry(appointment_window, bg='light sky blue')
    time.pack(pady=20)
    tk.Label(appointment_window, text="Appointment Description:", font=label_font).pack()
    description = tk.Entry(appointment_window, bg='light sky blue')
    description.pack(pady=20)
    tk.Button(appointment_window, text="Save", command=lambda: save_appointment(appointment_window, date.get(), time.get(), description.get())).pack(pady=10)

    

# Define a function to save appointments to a file
def save_appointment(appointment_window, date, time, description):
    with open("appointments.txt", "a") as file:
        file.write(f"{date} {time}: {description}\n")
    appointment_window.destroy()



root = tk.Tk()
root.title("Patient Information")
root.geometry("700x700")
root.config(bg='#CAF4F4')

# Style
label_font = ('delight coffee', 14)
entry_font = ('impact', 14)

name_label = tk.Label(root, text="Name:", font=label_font)
name_label.pack(pady=5)
name_entry = tk.Entry(root, font=entry_font, bg='light sky blue')
name_entry.pack(pady=5)

age_label = tk.Label(root, text="Age:", font=label_font)
age_label.pack(pady=5)
age_entry = tk.Entry(root, font=entry_font, bg='light sky blue')
age_entry.pack(pady=5)

symptoms_label = tk.Label(root, text="Symptoms:", font=label_font)
symptoms_label.pack(pady=5)
symptoms_entry = tk.Entry(root, font=entry_font, bg='light sky blue')
symptoms_entry.pack(pady=5)

emergency_contact_label = tk.Label(root, text="Emergency Contact:", font=label_font)
emergency_contact_label.pack(pady=10)
emergency_contact_entry = tk.Entry(root, font=entry_font, bg='light sky blue')
emergency_contact_entry.pack(pady=10)

appointment_button = tk.Button(root, text="Appointment", command=schedule_appointment, font=label_font)
appointment_button.pack(pady=10)



root.mainloop()
