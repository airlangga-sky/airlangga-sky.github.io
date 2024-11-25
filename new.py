import tkinter as tk
import random

class UlarTanggaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Permainan Ular Tangga")
        self.posisi_pemain = 0
        self.ujung_papan = 100
        self.ular = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75}
        self.tangga = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.jebakan = {30: "Berapa 6 x 7?", 50: "Berapa 8 x 5?", 70: "Berapa 9 x 3?"}
        
        self.label = tk.Label(master, text="Posisi Pemain: 0")
        self.label.pack()

        self.button = tk.Button(master, text="Lempar Dadu", command=self.lempar_dadu)
        self.button.pack()

    def lempar_dadu(self):
        langkah = random.randint(1, 6)
        self.posisi_pemain += langkah
        if self.posisi_pemain > self.ujung_papan:
            self.posisi_pemain = self.ujung_papan
        self.label.config(text=f'Posisi Pemain: {self.posisi_pemain}')
        self.cek_posisi()

    def cek_posisi(self):
        if self.posisi_pemain in self.ular:
            self.posisi_pemain = self.ular[self.posisi_pemain]
            self.label.config(text=f'Kena ular! Posisi Pemain: {self.posisi_pemain}')
        elif self.posisi_pemain in self.tangga:
            self.posisi_pemain = self.tangga[self.posisi_pemain]
            self.label.config(text=f'Naik tangga! Posisi Pemain: {self.posisi_pemain}')
        elif self.posisi_pemain in self.jebakan:
            self.kerjakan_soal(self.jebakan[self.posisi_pemain])

    def kerjakan_soal(self, soal):
        jawaban = tk.simpledialog.askinteger("Soal", soal)
        if not self.periksa_jawaban(soal, jawaban):
            self.posisi_pemain -= 1
            self.label.config(text=f'Salah! Mundur satu langkah. Posisi Pemain: {self.posisi_pemain}')

    def periksa_jawaban(self, soal, jawaban):
        if soal == "Berapa 6 x 7?":
            return jawaban == 42
        elif soal == "Berapa 8 x 5?":
            return jawaban == 40
        elif soal == "Berapa 9 x 3?":
            return jawaban == 27
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = UlarTanggaApp(root)
    root.mainloop()