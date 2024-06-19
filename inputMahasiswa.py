import tkinter
from tkinter import messagebox
from profileMahasiswa import Mahasiswa
from checkingStudentGPA import CheckStudentGPA
class InputMahasiswa:
  def __init__(self, root):
    self.listMahasiswa = Mahasiswa.dataMahasiswa()
    self.root = root
    self.displayUi()
    
  # Membuat jendela utama
  def displayUi(self):
    self.root.title("Input Data Mahasiswa")

    # Membuat label dan entry untuk Name
    self.nameLabel = tkinter.Label(self.root, text="Name :")
    self.nameLabel.grid(row=0, column=0, padx=10, pady=5)
    self.nameEntry = tkinter.Entry(self.root)
    self.nameEntry.grid(row=0, column=1, padx=10, pady=5)

    # Membuat label dan entry untuk Nilai
    self.nilaiLabel = tkinter.Label(self.root, text="Nilai :")
    self.nilaiLabel.grid(row=1, column=0, padx=10, pady=5)
    self.nilaiEntry = tkinter.Entry(self.root)
    self.nilaiEntry.grid(row=1, column=1, padx=10, pady=5)

    # Membuat label dan entry untuk NIM
    self.idLabel = tkinter.Label(self.root, text="NIM :")
    self.idLabel.grid(row=2, column=0, padx=10, pady=5)
    self.idEntry = tkinter.Entry(self.root)
    self.idEntry.grid(row=2, column=1, padx=10, pady=5)

    # Membuat label dan entry untuk Major
    self.majorLabel = tkinter.Label(self.root, text="Major :")
    self.majorLabel.grid(row=3, column=0, padx=10, pady=5)
    self.majorEntry = tkinter.Entry(self.root)
    self.majorEntry.grid(row=3, column=1, padx=10, pady=5)

    # Membuat tombol untuk menambahkan data
    self.addButton = tkinter.Button(self.root, text="Add Data", command=self.addData)
    self.addButton.grid(row=4, column=0, columnspan=2, pady=10)

    # Membuat tombol untuk melihat data
    self.seeButton = tkinter.Button(self.root, text="See Data", command=self.seeData)
    self.seeButton.grid(row=6, column=0, columnspan=2, pady=10)

    # Membuat frame untuk melihat data
    self.dataFrame = tkinter.Frame(self.root)
    self.dataFrame.grid(row=5, column=0, columnspan=2, pady=10)
    
    # Membuat button untuk menghapus buttonDataMahasiswa
    self.clearButton = tkinter.Button(self.root, text="Clear Data", command=self.clearButtonDataMahasiswa)
    self.clearButton.grid(row=8, column=0, columnspan=4, pady=10)
    
    # Menjalankan aplikasi
    self.root.mainloop()
  
  def mahasiswaInput(self, showMessage=True):
    # Mengambil input dari entry
    name = self.nameEntry.get()
    nilai = self.nilaiEntry.get()
    idCard = self.idEntry.get()
    major = self.majorEntry.get()
      
    # Menghapus spasi dari name dan major
    nameSplit = "".join(name.split())
    majorSplit = "".join(major.split())
      
    # Validasi input
    if idCard.isdigit() and nameSplit.isalpha() and nilai.isdigit() and majorSplit.isalpha():
      lenIdMahasiswa = len(str(idCard))
      lenDigitId = 8
          
      if lenIdMahasiswa <= lenDigitId:
        messagebox.showerror("Error", "The ID length must be at least 8 digits")
        return None

      if len(self.listMahasiswa) < 7:
        if showMessage:
          messagebox.showinfo("Success", "Data has been added")
        return name, nilai, idCard, major
      else:
        messagebox.showinfo("Alert", "Data tidak bisa ditambah lagi")
        
    else:
      messagebox.showerror("Error", "Please input valid data")
      return None

  def addData(self):
    self.listMahasiswa.append(Mahasiswa(*self.mahasiswaInput()))
    self.clearPlaceholder()
    
  def clearPlaceholder(self):
    self.nameEntry.delete(0, tkinter.END)
    self.nilaiEntry.delete(0, tkinter.END)
    self.idEntry.delete(0, tkinter.END)
    self.majorEntry.delete(0, tkinter.END)

  def seeData(self):
    for numberMahasiswa, mahasiswa in enumerate(self.listMahasiswa):
      self.dataButton = tkinter.Button(self.dataFrame, text=f"Data Mahasiswa {numberMahasiswa+1}",command=lambda : mahasiswa.getProfileMahasiswa(self.root, CheckStudentGPA())).pack()
      
  def clearButtonDataMahasiswa(self):
    for widget in self.dataFrame.winfo_children():
        widget.destroy()
    self.listMahasiswa.clear()
      
  @staticmethod
  def main():
    rootTk = tkinter.Tk()
    InputMahasiswa(rootTk)
    rootTk.mainloop()
