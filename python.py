import random

class UlarTangga:
    def __init__(self):
        self.posisi_pemain = 0
        self.ujung_papan = 100
        self.ular = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75}
        self.tangga = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.jebakan = {30: "Berapa 6 x 7?", 50: "Berapa 8 x 5?", 70: "Berapa 9 x 3?"}

    def lempar_dadu(self):
        return random.randint(1, 6)

    def gerak(self, langkah):
        self.posisi_pemain += langkah
        if self.posisi_pemain > self.ujung_papan:
            self.posisi_pemain = self.ujung_papan  # Jika lebih dari 100, tetap di 100
        print(f'Posisi Pemain: {self.posisi_pemain}')

        # Cek ular
        if self.posisi_pemain in self.ular:
            print("Oh tidak! Kena ular!")
            self.posisi_pemain = self.ular[self.posisi_pemain]
            print(f'Posisi Pemain setelah kena ular: {self.posisi_pemain}')

        # Cek tangga
        elif self.posisi_pemain in self.tangga:
            print("Selamat! Naik tangga!")
            self.posisi_pemain = self.tangga[self.posisi_pemain]
            print(f'Posisi Pemain setelah naik tangga: {self.posisi_pemain}')

        # Cek jebakan
        elif self.posisi_pemain in self.jebakan:
            self.kerjakan_soal(self.jebakan[self.posisi_pemain])

    def kerjakan_soal(self, soal):
        print(soal)
        jawaban = int(input("Jawaban Anda: "))
        if not self.periksa_jawaban(soal, jawaban):
            print("Jawaban salah! Anda harus mengerjakan soal ini sampai benar.")
            self.posisi_pemain -= 1  # Mundur satu langkah jika salah
            print(f'Posisi Pemain setelah salah: {self.posisi_pemain}')

    def periksa_jawaban(self, soal, jawaban):
        if soal == "Berapa 6 x 7?":
            return jawaban == 42
        elif soal == "Berapa 8 x 5?":
            return jawaban == 40
        elif soal == "Berapa 9 x 3?":
            return jawaban == 27
        return False

    def main(self):
        print("Selamat datang di permainan Ular Tangga dengan jebakan soal!")
        while self.posisi_pemain < self.ujung_papan:
            input("Tekan Enter untuk melempar dadu...")
            langkah = self.lempar_dadu()
            print(f'Anda mendapatkan angka: {langkah}')
            self.gerak(langkah)

        print("Selamat! Anda telah mencapai 100 dan memenangkan permainan!")

if __name__ == "__main__":
    permainan = UlarTangga()
    permainan.main()