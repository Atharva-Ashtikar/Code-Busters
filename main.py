import tkinter as tk
from tkinter import messagebox
import uuid

class Patient:
    def __init__(self, name, age, symptoms, emergency_contact):
        self.id = str(uuid.uuid4().int)[:10]
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.emergency_contact = emergency_contact
    
    def display_info(self):
        return "ID:" + self.id + "\nName:" + self.name + "\nAge:" + self.age + "\nSymptoms:" + self.symptoms + "\nEmergency Contact:" + self.emergency_contact

def get_patient_info():
    name = name_entry.get()
    age = age_entry.get()
    symptoms = symptoms_entry.get()
    emergency_contact = emergency_contact_entry.get()
    return Patient(name, age, symptoms, emergency_contact)

def display_patient_info():
    patient = get_patient_info()
    messagebox.showinfo("Patient Information", patient.display_info())

def save_patient_info():
    patient = get_patient_info()
    with open("patient_info.txt", "a") as file:
        file.write(patient.display_info() + "\n")
    messagebox.showinfo("Success", "Patient information saved successfully!")

root = tk.Tk()
root.title("Patient Information")
root.geometry("700x700")

# Style
label_font = ('Helvetica', 14)
entry_font = ('Helvetica', 16)

name_label = tk.Label(root, text="Name:", font=label_font)
name_label.pack(pady=10)
name_entry = tk.Entry(root, font=entry_font)
name_entry.pack(pady=10)

age_label = tk.Label(root, text="Age:", font=label_font)
age_label.pack(pady=10)
age_entry = tk.Entry(root, font=entry_font)
age_entry.pack(pady=10)

symptoms_label = tk.Label(root, text="Symptoms:", font=label_font)
symptoms_label.pack(pady=10)
symptoms_entry = tk.Entry(root, font=entry_font)
symptoms_entry.pack(pady=10)

emergency_contact_label = tk.Label(root, text="Emergency Contact:", font=label_font)
emergency_contact_label.pack(pady=10)
emergency_contact_entry = tk.Entry(root, font=entry_font)
emergency_contact_entry.pack(pady=10)

display_button = tk.Button(root, text="Display Information", command=display_patient_info, font=label_font)
display_button.pack(pady=10)

save_button = tk.Button(root, text="Save Information", command=save_patient_info, font=label_font)
save_button.pack(pady=20)

root.mainloop()