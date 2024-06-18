import tkinter as tk
from tkinter import messagebox


class Mahasiswa:
    def __init__(self, name, nilai, idCard, major):
        self.name = name
        self.nilai = nilai
        self.idCard = idCard
        self.major = major

    def getProfileMahasiswa(self, parent):
        top = tk.Toplevel(parent)
        top.title("Profile Mahasiswa BSI")

        header = "Profile Mahasiswa".center(30)
        header_frame = tk.Label(top, text=header, font=("Arial", 20, "bold"))
        header_frame.pack()

        profile_info = f"Nama : {self.name}\nNilai : {self.nilai}\nNIM : {self.idCard}\nJurusan : {self.major}"
        profile_label = tk.Label(
            top, text=profile_info, font=("Arial", 18), anchor="w", justify="left"
        )
        profile_label.pack()


def mahasiswaInput(show_message=True):
    # Mengambil input dari entry
    name = name_entry.get().strip()
    nilai = nilai_entry.get().strip()
    idCard = id_entry.get().strip()
    major = major_entry.get().strip()

    # Menghapus spasi dari name dan major
    nameSplit = "".join(name.split())
    majorSplit = "".join(major.split())

    # Validasi input
    if (
        idCard.isdigit()
        and nameSplit.isalpha()
        and nilai.isdigit()
        and majorSplit.isalpha()
    ):
        lenIdMahasiswa = len(str(idCard))
        lenDigitId = 8

        if lenIdMahasiswa < lenDigitId:
            messagebox.showerror("Error", "The ID length must be at least 8 digits")
            return None

        if show_message:
            messagebox.showinfo("Success", "Data has been added")

        return name, nilai, idCard, major
    else:
        messagebox.showerror("Error", "Please input valid data")
        return None


def addData():
    mahasiswa_data = mahasiswaInput()
    if mahasiswa_data:
        mahasiswa = Mahasiswa(*mahasiswa_data)
        mahasiswa_list.append(mahasiswa)
        name_entry.delete(0, tk.END)
        nilai_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)
        major_entry.delete(0, tk.END)


def seeData():
    for widget in data_frame.winfo_children():
        widget.destroy()

    for idx, mahasiswa in enumerate(mahasiswa_list):
        tk.Button(
            data_frame,
            text=f"Data Mahasiswa {idx+1}",
            command=lambda m=mahasiswa: m.getProfileMahasiswa(root),
        ).pack()


# Membuat jendela utama
root = tk.Tk()
root.title("Input Data Mahasiswa")

# Daftar untuk menyimpan objek Mahasiswa
mahasiswa_list = []

# Membuat label dan entry untuk Name
name_label = tk.Label(root, text="Name :")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Nilai
nilai_label = tk.Label(root, text="Nilai :")
nilai_label.grid(row=1, column=0, padx=10, pady=5)
nilai_entry = tk.Entry(root)
nilai_entry.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entry untuk NIM
id_label = tk.Label(root, text="NIM :")
id_label.grid(row=2, column=0, padx=10, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=2, column=1, padx=10, pady=5)

# Membuat label dan entry untuk Major
major_label = tk.Label(root, text="Major :")
major_label.grid(row=3, column=0, padx=10, pady=5)
major_entry = tk.Entry(root)
major_entry.grid(row=3, column=1, padx=10, pady=5)

# Membuat tombol untuk menambahkan data
add_button = tk.Button(root, text="Add Data", command=addData)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

# Membuat tombol untuk melihat data
see_button = tk.Button(root, text="See Data", command=seeData)
see_button.grid(row=6, column=0, columnspan=2, pady=10)

# Membuat frame untuk melihat data
data_frame = tk.Frame(root)
data_frame.grid(row=5, column=0, columnspan=2, pady=10)


# Menjalankan aplikasi
root.mainloop()
