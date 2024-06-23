from tkinter import *

class CheckStudentGPA:
  def __init__(self, nilai):
    self.GPA = float(nilai)
    
  def getTitle(self):
    if self.GPA > 4.0:
      return "Tolong Masukkan GPA yang valid"
    elif self.GPA >= 3.5 and self.GPA < 4.1:
      return "Summa Cum Laude"
    elif self.GPA >= 3.0 and self.GPA <= 3.5:
      return "Magna Cum Laude"
    else:
      return "Cum Laude"