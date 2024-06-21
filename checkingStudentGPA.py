from tkinter import *

class CheckStudentGPA:
  def __init__(self):
    pass
    
  def checkGPA(self, nilai):
    top = Toplevel()
        
    GPA = float(nilai)  # Ambil nilai GPA dari objek Mahasiswa
        
    if GPA > 40:
      labelGPA = Label(top, text="Tolong Masukkan GPA yang valid")
    elif GPA >= 3.5 and GPA <= 4.0:
      labelGPA = Label(top, text="Summa Cum Laude")
    elif GPA >= 3.0 and GPA <= 3.5:
      labelGPA = Label(top, text="Magna Cum Laude")
    else:
      labelGPA = Label(top, text="Cum Laude")
        
    labelGPA.pack()

