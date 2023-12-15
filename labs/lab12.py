import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("CGPA Management System")

        full_window_frame = ttk.Frame(self)
        full_window_frame.grid(row=0, column=0, padx=10, pady=10)  

        self.oop_label = ttk.Label(full_window_frame, text="OOP")
        self.oop_label.grid(row=0, column=0, padx=10, pady=10)

        self.oop_marks = tk.StringVar()
        self.oop_marks_entry = ttk.Entry(full_window_frame, width=50)
        self.oop_marks_entry.grid(row=0, column=1, padx=10, pady=10)
        self.oop_marks_entry["textvariable"] = self.oop_marks

        self.oop_lab_label = ttk.Label(full_window_frame, text="OOP LAB")
        self.oop_lab_label.grid(row=1, column=0, padx=10, pady=10)

        self.oop_lab_marks = tk.StringVar()
        self.oop_lab_marks_entry = ttk.Entry(full_window_frame, width=50)
        self.oop_lab_marks_entry.grid(row=1, column=1, padx=10, pady=10)
        self.oop_lab_marks_entry["textvariable"] = self.oop_lab_marks

        self.eng_label = ttk.Label(full_window_frame, text="ENGLISH")
        self.eng_label.grid(row=2, column=0, padx=10, pady=10)

        self.eng_marks = tk.StringVar()
        self.eng_marks_entry = ttk.Entry(full_window_frame, width=50)
        self.eng_marks_entry.grid(row=2, column=1, padx=10, pady=10)
        self.eng_marks_entry["textvariable"] = self.eng_marks

        self.ist_label = ttk.Label(full_window_frame, text="ISLAMIAT")
        self.ist_label.grid(row=3, column=0, padx=10, pady=10)

        self.ist_marks = tk.StringVar()
        self.ist_marks_entry = ttk.Entry(full_window_frame, width=50)
        self.ist_marks_entry.grid(row=3, column=1, padx=10, pady=10)
        self.ist_marks_entry["textvariable"] = self.ist_marks

        self.calc_button = ttk.Button(full_window_frame, text="Save")
        self.calc_button.grid(row=4, column=0, padx=10, pady=10)
        self.calc_button.bind('<Button-1>', self.calc)

        self.display_label = ttk.Label(self, text="Percentage: ")
        self.display_label.grid(row=5, column=0, columnspan=2, padx=10,pady=10)

    def get_p1(self):
        perc = int(self.oop_marks_entry.get())
        return perc
    
    def get_p2(self):
        perc = int(self.oop_lab_marks_entry.get())
        return perc
    
    def get_p3(self):
        perc = int(self.eng_marks_entry.get())
        return perc
    
    def get_p4(self):
        perc = int(self.ist_marks_entry.get())
        return perc
    
    def calc(self, event):
        oop_hrs = 3
        oop_lab_hrs = 1
        eng_hrs = 2
        ist_hrs = 2
        oop = self.get_p1()
        oop_lab = self.get_p2()
        eng = self.get_p3()
        ist = self.get_p4()
        num = (oop_hrs * oop) + (oop_lab_hrs * oop_lab) + (eng_hrs * eng) + (ist_hrs * ist)
        den = oop_hrs + oop_lab_hrs + eng_hrs + ist_hrs
        result = num / den
        self.display_label.config(text=f"Percentage: {result}")

    def sum_cr_hrs():
        oop_hrs = 3
        oop_lab_hrs = 1
        eng_hrs = 2
        ist_hrs = 2
        sum_hrs = oop_hrs + oop_lab_hrs + eng_hrs + ist_hrs
        return sum_hrs
    
    def points(self, score):
        if score >= 80:
            point = 4
            return point
        elif score >= 60 and score <= 79:
            point = 3
            return point
        elif score > 50 and score <= 64:
            point = 2
            return point
        elif score < 50:
            point = 0
            return point
    

    def cgpa(self, num, den, event):
        cgpa = num / den

def main():
    App().mainloop()
    # App.pnt(App, '<Button-1>')
    


main()