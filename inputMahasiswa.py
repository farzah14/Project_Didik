import tkinter
from tkinter import messagebox
from profileMahasiswa import *
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
    
    # Membuat judul
    self.judul = tkinter.Label(self.root, text="Form Input Mahasiswa", font=("Roboto", 48), bg="#222831", fg="#E7F0DC")
    self.judul.pack(pady=(60, 40))
    
    # Mendapatkan ukuran layar
    screenWidth = self.root.winfo_screenwidth()
    screenHeight = self.root.winfo_screenheight()
        
    # Menghitung posisi tengah jendela
    windowWidth = 1280    # lebar jendela
    windowHeight = 720   # tinggi jendela
    x = (screenWidth - windowWidth) // 2
    y = (screenHeight - windowHeight) // 2
        
    # Menempatkan jendela di posisi tengah layar
    self.root.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")
        
    # Membuat frame untuk menampung label, input, dan button
    self.mainFrame = tkinter.Frame(self.root)
    self.mainFrame.pack(pady=0)
    self.mainFrame.configure(bg="#31363F")

    # Membuat label dan entry untuk Name
    self.nameLabel = tkinter.Label(self.mainFrame, text="Name", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
    self.nameLabel.grid(row=0, column=0, padx=30, pady=11, sticky="w")
    
    self.nameEntry = tkinter.Entry(self.mainFrame, width=40, font=26)
    self.nameEntry.grid(row=0, column=1, padx=30, pady=11)

    # Membuat label dan entry untuk Nilai
    self.labelIpk = tkinter.Label(self.mainFrame, text="IPK", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
    self.labelIpk.grid(row=1, column=0, padx=30, pady=11, sticky="w")
    self.inputIpk = tkinter.Entry(self.mainFrame, width=40, font=26)
    self.inputIpk.grid(row=1, column=1, padx=30, pady=11)

    # Membuat label dan entry untuk NIM
    self.idLabel = tkinter.Label(self.mainFrame, text="NIM", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
    self.idLabel.grid(row=2, column=0, padx=30, pady=11, sticky="w")
    self.nimEntry = tkinter.Entry(self.mainFrame, width=40, font=26)
    self.nimEntry.grid(row=2, column=1, padx=30, pady=11)

    # Membuat label dan entry untuk jurusan
    self.labelJurusan = tkinter.Label(self.mainFrame, text="Jurusan", font=("Roboto", 30), fg="#76ABAE", bg="#31363F", anchor="w")
    self.labelJurusan.grid(row=3, column=0, padx=30, pady=11, sticky="w")
    self.inputJurusan = tkinter.Entry(self.mainFrame, width=40, font=26)
    self.inputJurusan.grid(row=3, column=1, padx=30, pady=11)

    # Membuat tombol untuk menambahkan data
    self.addButton = tkinter.Button(self.mainFrame, text="Add Data", command=self.addData, width=11, height=2, bg="#365E32", fg="#E7F0DC", font=("Roboto", 12))
    self.addButton.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    # Membuat tombol untuk melihat data
    self.seeButton = tkinter.Button(self.mainFrame, text="See Data", command=self.seeData, width=11, height=2, font=("Roboto", 12), bg="#6295A2", fg="#E7F0DC")
    self.seeButton.grid(row=4, column=1, columnspan=1, padx=10, pady=10)
    
    # Membuat button untuk menghapus data
    self.clearButton = tkinter.Button(self.mainFrame, text="Clear Data", command=self.clearButtonDataMahasiswa, width=11, height=2, font=("Roboto", 12), bg="#E2DFD0")
    self.clearButton.grid(row=4, column=2, columnspan=1, padx=25, pady=10)
    
    # Membuat button untuk download file pdf
    self.download = tkinter.Button(self.mainFrame, text="Download", command=self.downloadData, bg="#C40C0C", fg="#E7F0DC")
    self.download.grid(row=3, column=2, columnspan=2)
    
    # Mengatur agar konten tetap di tengah saat jendela diubah ukurannya
    self.mainFrame.grid_rowconfigure(0, weight=1)
    self.mainFrame.grid_columnconfigure(0, weight=1)
    self.mainFrame.grid_rowconfigure(1, weight=1)
    self.mainFrame.grid_columnconfigure(1, weight=1)
  
  def addData(self):
    self.listMahasiswa.append(Mahasiswa(*self.mahasiswaInput()))
    self.clearPlaceholder()

  def seeData(self):
    if len(self.listMahasiswa) == 0:
      errMessage = messagebox.showerror("Error", "Tolong masukkan data yang valid")
      return errMessage

    else:
      # Membuat window baru
      self.dataGUI = tkinter.Toplevel(self.root)
      self.dataGUI.title("Data Mahasiswa")
      self.dataGUI.configure(bg="#31363F")

        # Menempatkan window di tengah layar
      window_width = 800
      window_height = 400
      self.dataGUI.geometry(f"{window_width}x{window_height}")
      
      for index, data in enumerate(self.listMahasiswa):
        data.getProfileMahasiswa(self.dataGUI, index)
        
  def clearPlaceholder(self):
    self.nameEntry.delete(0, tkinter.END)
    self.inputIpk.delete(0, tkinter.END)
    self.nimEntry.delete(0, tkinter.END)
    self.inputJurusan.delete(0, tkinter.END)
    
  def clearButtonDataMahasiswa(self):
    if len(self.listMahasiswa) == 0:
      messagebox.showerror("Error", "Tidak ada data yang dapat dihapus")
    else:
      self.dataGUI.destroy()
      self.listMahasiswa.clear()
      messagebox.showinfo("Success", "Data berhasil di hapus")
  
  def downloadData(self):
    if len(self.listMahasiswa) == 0:
      messagebox.showerror("Error", "Tidak ada data untuk diunduh")
    else:
      pdf = FPDF()
      pdf.add_page()
      pdf.set_font("Arial", size = 25)
      pdf.cell(200, 10, txt = "Data Mahasiswa", ln = True, align = "C")
      pdf.ln(10)
      for mahasiswa in self.listMahasiswa:
        pdfForSetFont = pdf
        pdfForSetFont.set_font("Arial", size = 13)
        pdfForSetFont.cell(0, 10, txt = f"Name : {mahasiswa.name}, NIM : {mahasiswa.nim}, IPK : {mahasiswa.ipk}, Major : {mahasiswa.jurusan}, Title : {CheckStudentGPA(mahasiswa.ipk).getTitle()}", ln = True, align = "C",)
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
    super().__init__(root) #mengakses parameter class GUI
    
  def mahasiswaInput(self):
    # Mengambil input dari entry
    name = self.nameEntry.get()
    ipk = float(self.inputIpk.get())
    nim = int(self.nimEntry.get())
    jurusan = self.inputJurusan.get()
      
    # Menghapus spasi dari name dan jurusan
    nameSplit = "".join(name.split())
    jurusanSplit = "".join(jurusan.split())

    # Validasi input
    if type(nim) == int and nameSplit.isalpha() and type(ipk) == float and jurusanSplit.isalpha():
      messagebox.showinfo("Success", "Data telah ditambahkan")
      return name, ipk, nim, jurusan
    else:
      errMessage = messagebox.showerror("Error", "Tolong masukkan data yang valid")
      return errMessage
