class Mahasiswa: 
    
    jumlah_mahasiswa = 0
    
    def __init__(self, name, nim, prodi): 
        self.name = name 
        self.nim = nim 
        self.prodi = prodi
        Mahasiswa.jumlah_mahasiswa += 1
        print("Membuat Object Mahasiswa dengan nama " + self.name)
        
mhs1 = Mahasiswa("Adam", "21051214005", "Teknik Informatika")
print("Total Mahasiswa : " + str(mhs1.jumlah_mahasiswa))
mhs2 = Mahasiswa("Budi", "21051214006", "Teknik Industri")
print("Total Mahasiswa : " + str(mhs2.jumlah_mahasiswa))

print()
print("Total Mahasiswa : " + str(Mahasiswa.jumlah_mahasiswa))