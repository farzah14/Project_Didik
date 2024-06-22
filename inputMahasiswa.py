import tkinter
from tkinter import messagebox
from profileMahasiswa import Mahasiswa
from checkingStudentGPA import CheckStudentGPA 
from fpdf import FPDF

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
    window_width = 1280    # lebar jendela
    window_height = 720   # tinggi jendela
    x_center = (screen_width - window_width) // 2
    y_center = (screen_height - window_height) // 2
        
    # Menempatkan jendela di posisi tengah layar
    self.root.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")
        
    # Membuat frame utama dengan ukuran yang dapat berubah
    self.main_frame = tkinter.Frame(self.root)
    self.main_frame.pack(pady=80, fill="y")
    self.main_frame.configure(bg="#31363F")
    
     # Menambahkan judul di tengah
    self.titleLabel = tkinter.Label(self.root, text="Form Data Mahasiswa", font=("Roboto", 40), fg="#76ABAE", bg="#222831")
    self.titleLabel.pack(pady=0)

    
    # Membuat label dan entry untuk Name
    self.nameLabel = tkinter.Label(self.main_frame, text="Name", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
    self.nameLabel.grid(row=0, column=0, padx=30, pady=11, sticky="w")
    self.nameEntry = tkinter.Entry(self.main_frame, width=40, font=26)
    self.nameEntry.grid(row=0, column=1, padx=30, pady=11)

    # Membuat label dan entry untuk Nilai
    self.nilaiLabel = tkinter.Label(self.main_frame, text="IPK", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
    self.nilaiLabel.grid(row=1, column=0, padx=30, pady=11, sticky="w")
    self.nilaiEntry = tkinter.Entry(self.main_frame, width=40, font=26)
    self.nilaiEntry.grid(row=1, column=1, padx=30, pady=11)

    # Membuat label dan entry untuk NIM
    self.idLabel = tkinter.Label(self.main_frame, text="NIM", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
    self.idLabel.grid(row=2, column=0, padx=30, pady=11, sticky="w")
    self.idEntry = tkinter.Entry(self.main_frame, width=40, font=26)
    self.idEntry.grid(row=2, column=1, padx=30, pady=11)

    # Membuat label dan entry untuk Major
    self.majorLabel = tkinter.Label(self.main_frame, text="Major", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
    self.majorLabel.grid(row=3, column=0, padx=30, pady=11, sticky="w")
    self.majorEntry = tkinter.Entry(self.main_frame, width=40, font=26)
    self.majorEntry.grid(row=3, column=1, padx=30, pady=11)

    # Membuat tombol untuk menambahkan data
    self.addButton = tkinter.Button(self.main_frame, text="Add Data", command=self.addData, width=11, height=2, bg="#365E32", fg="#E7F0DC", font=("Roboto", 12))
    self.addButton.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    # Membuat tombol untuk melihat data
    self.seeButton = tkinter.Button(self.main_frame, text="See Data", command=self.seeData, width=11, height=2, font=("Roboto", 12), bg="#6295A2", fg="#E7F0DC")
    self.seeButton.grid(row=4, column=1, columnspan=1, padx=10, pady=10)
    
    # Membuat button untuk menghapus data
    self.clearButton = tkinter.Button(self.main_frame, text="Clear Data", command=self.clearButtonDataMahasiswa, width=11, height=2, font=("Roboto", 12), bg="#E2DFD0")
    self.clearButton.grid(row=4, column=2, columnspan=1, padx=25, pady=10)
    # Membuat frame untuk menampung button data mahasiswa
    self.dataFrame = tkinter.Frame(self.main_frame, bg="#31363F")
    self.dataFrame.grid(row=5, column=0, columnspan=2, pady=20)
    
    # Membuat button untuk download file pdf
    self.download = tkinter.Button(self.main_frame, text="Download", command=self.downloadData, bg="#C40C0C", fg="#E7F0DC")
    self.download.grid(row=3, column=2, columnspan=2)
    
    # Mengatur agar konten tetap di tengah saat jendela diubah ukurannya
    self.main_frame.grid_rowconfigure(0, weight=1)
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_rowconfigure(1, weight=1)
    self.main_frame.grid_columnconfigure(1, weight=1)
  
  def addData(self):
    self.listMahasiswa.append(Mahasiswa(*self.mahasiswaInput()))
    self.clearPlaceholder()

  def seeData(self):
    if len(self.listMahasiswa) == 0:
      messagebox.showerror("Error", "Please add data")
    else:
      # Membuat window baru
      data_window = tkinter.Toplevel(self.root)
      data_window.title("Data Mahasiswa")
      data_window.configure(bg="#31363F")

      # Menempatkan window di tengah layar
      window_width = 600
      window_height = 400
      screen_width = data_window.winfo_screenwidth()
      screen_height = data_window.winfo_screenheight()
      x_center = (screen_width - window_width) // 2
      y_center = (screen_height - window_height) // 2
      data_window.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")

      # Membuat tombol untuk setiap mahasiswa
      for numberMahasiswa, mahasiswa in enumerate(self.listMahasiswa):
        dataButton = tkinter.Button(data_window, text=f"Data Mahasiswa ke-{numberMahasiswa+1}", command=lambda m=mahasiswa: m.getProfileMahasiswa(self.root, CheckStudentGPA(mahasiswa.nilai)),bg="#FD9B63", justify="center")
        dataButton.grid(row=0, column=numberMahasiswa, padx=5, pady=5, sticky="ew")
      
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
      self.dataFrame.configure(bg="#31363F")
      self.listMahasiswa.clear()
  
  def downloadData(self):
    if len(self.listMahasiswa) == 0:
      messagebox.showerror("Error", "Tidak ada data untuk diunduh")
    else:
      pdf = FPDF()
      pdf.add_page()
      pdf.set_font("Arial",size = 15)
      pdf.cell(200, 10, txt = "Data Mahasiswa", align = "C")
      pdf.ln(10)
      for mahasiswa in self.listMahasiswa:
        pdf.cell(0, 10, txt = f"Name : {mahasiswa.name}, NIM : {mahasiswa.idCard}, IPK : {mahasiswa.nilai}, Major : {mahasiswa.major}, Title : {CheckStudentGPA(mahasiswa.nilai).getTitle()}", ln = True, align = 'C')
      pdf.output(f"dataMahasiswa.pdf")
      messagebox.showinfo("Success", "Data telah diunduh dalam format PDF")

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
    nilai = float(self.nilaiEntry.get())
    idCard = self.idEntry.get()
    major = self.majorEntry.get()
      
    # Menghapus spasi dari name dan major
    nameSplit = "".join(name.split())
    majorSplit = "".join(major.split())
      
    # Validasi input
    if idCard.isdigit() and nameSplit.isalpha() and type(nilai) == float and majorSplit.isalpha():
      lenIdMahasiswa = len(str(idCard))
      lenDigitId = 8
          
      if lenIdMahasiswa <= lenDigitId:
        messagebox.showerror("Error", "The ID length must be at least 8 digits")

      if len(self.listMahasiswa) < 20:
        if showMessage:
          messagebox.showinfo("Success", "Data has been added")
        return name, nilai, idCard, major
      else:
        messagebox.showerror("Alert", "Data tidak bisa ditambah lagi")
        
    else:
      messagebox.showerror("Error", "Please input valid data")
      return None
