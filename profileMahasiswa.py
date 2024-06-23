import tkinter
from checkingStudentGPA import CheckStudentGPA 
class Mahasiswa:
  def __init__(self, name, ipk, nim, jurusan):
    self.name = name
    self.ipk = ipk
    self.nim = nim
    self.jurusan = jurusan
    
  def getProfileMahasiswa(self, root, index):
    result = f"Data ke-{index+1} = Name : {self.name}, NIM : {self.nim}, IPK : {self.ipk}, Major : {self.jurusan}, Title : {CheckStudentGPA(self.ipk).getTitle()}"
        
    textDataMahasiswa = tkinter.Label(root, text=result, font=("Roboto", 12), bg="#31363F", fg="#E7F0DC")
    textDataMahasiswa.grid(row=index, column=0, padx=20, pady=10, sticky="w")
    
  def dataMahasiswa():
    return []

