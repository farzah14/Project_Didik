from tkinter import *

class CheckStudentGPA:
  def __init__(self):
    pass
    
  def checkGPA(self, mahasiswa):
    top = Toplevel()
        
    GPA = float(mahasiswa.nilai)  # Ambil nilai GPA dari objek Mahasiswa
        
    if GPA >= 35:
      labelGPA = Label(top, text="Summa Cum Laude")
    elif GPA >= 30:
      labelGPA = Label(top, text="Magna Cum Laude")
    else:
      labelGPA = Label(top, text="Cum Laude")
        
    labelGPA.pack()

