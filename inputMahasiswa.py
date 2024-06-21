import tkinter
from tkinter import messagebox
from profileMahasiswa import Mahasiswa
from checkingStudentGPA import CheckStudentGPA
from PIL import Image, ImageTk
class GUI:
  def __init__(self, root):
    self.root = root
    self.displayUi()

  # Membuat jendela utama
  def displayUi(self):
        self.root.title("Input Data Mahasiswa")
        
        self.root.configure(bg="#222831")
        # Mendapatkan ukuran layar
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Menghitung posisi tengah jendela
        window_width = 800    # lebar jendela
        window_height = 600   # tinggi jendela
        x_center = (screen_width - window_width) // 2
        y_center = (screen_height - window_height) // 2
        
        # Menempatkan jendela di posisi tengah layar
        self.root.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")
        
        # Membuat frame utama
        main_frame = tkinter.Frame(self.root)
        main_frame.pack(pady=80)
        main_frame.configure(bg="#31363F")
        
        # Membuat label dan entry untuk Name
        self.nameLabel = tkinter.Label(main_frame, text="Name", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
        self.nameLabel.grid(row=0, column=0, padx=30, pady=11, sticky="w")
        self.nameEntry = tkinter.Entry(main_frame, width=40, font=26)
        self.nameEntry.grid(row=0, column=1, padx=30, pady=11)

        # Membuat label dan entry untuk Nilai
        self.nilaiLabel = tkinter.Label(main_frame, text="IPK", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
        self.nilaiLabel.grid(row=1, column=0, padx=30, pady=11, sticky="w")
        self.nilaiEntry = tkinter.Entry(main_frame, width=40, font=26)
        self.nilaiEntry.grid(row=1, column=1, padx=30, pady=11)

        # Membuat label dan entry untuk NIM
        self.idLabel = tkinter.Label(main_frame, text="NIM", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
        self.idLabel.grid(row=2, column=0, padx=30, pady=11, sticky="w")
        self.idEntry = tkinter.Entry(main_frame, width=40, font=26)
        self.idEntry.grid(row=2, column=1, padx=30, pady=11)

        # Membuat label dan entry untuk Major
        self.majorLabel = tkinter.Label(main_frame, text="Major", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
        self.majorLabel.grid(row=3, column=0, padx=30, pady=11, sticky="w")
        self.majorEntry = tkinter.Entry(main_frame, width=40, font=26)
        self.majorEntry.grid(row=3, column=1, padx=30, pady=11)

        # Membuat tombol untuk menambahkan data
        self.addButton = tkinter.Button(main_frame, text="Add Data", command=self.addData)
        self.addButton.grid(row=4, column=2, columnspan=2, pady=10)

        # Membuat tombol untuk melihat data
        self.seeButton = tkinter.Button(main_frame, text="See Data", command=self.seeData)
        self.seeButton.grid(row=4, column=1, columnspan=2, pady=10)

        # Membuat frame untuk melihat data
        self.dataFrame = tkinter.Frame(main_frame)
        self.dataFrame.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Membuat button untuk menghapus buttonDataMahasiswa
        self.clearButton = tkinter.Button(main_frame, text="Clear Data", command=self.clearButtonDataMahasiswa)
        self.clearButton.grid(row=4, column=4, columnspan=2, pady=10)
        
        # Mengatur agar konten tetap di tengah saat jendela diubah ukurannya
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
  
  def addData(self):
    self.listMahasiswa.append(Mahasiswa(*self.mahasiswaInput()))
    self.clearPlaceholder()

  def seeData(self):
    if len(self.listMahasiswa) == 0:
      messagebox.showerror("Error", "Please add data")
    else:
      for numberMahasiswa, mahasiswa in enumerate(self.listMahasiswa):
        self.dataButton = tkinter.Button(self.dataFrame, text=f"Data Mahasiswa {numberMahasiswa+1}",command=lambda : mahasiswa.getProfileMahasiswa(self.root, CheckStudentGPA())).pack()
      
  def clearPlaceholder(self):
    self.nameEntry.delete(0, tkinter.END)
    self.nilaiEntry.delete(0, tkinter.END)
    self.idEntry.delete(0, tkinter.END)
    self.majorEntry.delete(0, tkinter.END)
    
  def clearButtonDataMahasiswa(self):
    if len(self.listMahasiswa) == 0:
      messagebox.showerror("Error", "Tidak ada data yang dapat dihapus")
    else:
      for widget in self.dataFrame.winfo_children():
          widget.destroy()
      self.listMahasiswa.clear()

  @staticmethod
  def main():
    rootTk = tkinter.Tk()
    InputMahasiswa(rootTk)
    rootTk.mainloop()
    
class InputMahasiswa(GUI):
  def __init__(self, root):
    self.listMahasiswa = Mahasiswa.dataMahasiswa()
    super().__init__(root)
    
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