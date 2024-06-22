from tkinter import *

class CheckStudentGPA:
  def __init__(self, nilai):
    self.title = ""
    self.GPA = float(nilai)
  
  def checkGPA(self):
    top = Toplevel()
    if self.GPA > 4.0:
      labelGPA = Label(top, text="Tolong Masukkan GPA yang valid")
      
    elif self.GPA >= 3.5 and self.GPA <= 4.0:
      labelGPA = Label(top, text="Summa Cum Laude")

    elif self.GPA >= 3.0 and self.GPA < 3.5:
      labelGPA = Label(top, text="Magna Cum Laude")

    else:
      labelGPA = Label(top, text="Cum Laude")

    labelGPA.pack()
    
  def getTitle(self):
    if self.GPA > 4.0:
      return "Tolong Masukkan GPA yang valid"
    elif self.GPA >= 3.5 and self.GPA < 4.1:
      return "Summa Cum Laude"
    elif self.GPA >= 3.0 and self.GPA <= 3.5:
      return "Magna Cum Laude"
    else:
      return "Cum Laude"

