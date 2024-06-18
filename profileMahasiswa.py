from tkinter import *

class Mahasiswa:
  def __init__(self, name, nilai, idCard, major):
    self.name = name
    self.nilai = nilai
    self.idCard = idCard
    self.major = major
    
  def getProfileMahasiswa(self, parent, checker):
    top = Toplevel(parent)
    top.title("Profile Mahasiswa BSI")
        
    header = "Profile Mahasiswa".center(30)
    header_frame = Label(top, text=header, font=('Arial', 20, 'bold'))
    header_frame.pack()
        
    profile_info = f"Nama : {self.name}\nNilai : {self.nilai}\nNIM : {self.idCard}\nJurusan : {self.major}"
    profile_label = Label(top, text=profile_info, font=('Arial', 18), anchor='w', justify="left")
    profile_label.pack()
        
    Button(top, text="Check Kelulusan", command=lambda: checker.checkGPA(self)).pack()
    
  def dataMahasiswa():
    return []

