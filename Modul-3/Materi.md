# MODUL - 3 : PRINSIP OOP BAGIAN 2 - INHERITANCE (PEWARISAN)

>**Tujuan:** 
Mahasiswa memahami cara melindungi data object.

**Materi Pembelajaran :**
1. Pengantar Inheritance
2. Super() Memanggil Constructor Parent 
3. Override Method
4. Multiple Inheritance

**Capaian Pembelajaran:**
1. Mahasiswa mampu menjelaskan konsep, tujuan, dan analogi sederhana prinsip OOP inheritance (Pewarisan)
2. Mahasiswa mampu menjelaskan dan menggunakan `super()` untuk memanggil contructor parent pada bahasa pemrograman python
3. Mahasiswa mampu menjelaskan dan menggunakan Override method pada bahasa pemrograman python
4. Mahasiswa mampu menjelaskan dan menggunakan multiple inheritance pada bahasa pemrograman python

---
## 1. Pengantar Inheritance (Pewarisan)
**Inheritance** (Pewarisan) adalah mekanisme di mana sebuah class baru (disebut **Child Class** / Subclass / Anak) dapat mewarisi semua atribut dan method dari class yang sudah ada (disebut **Parent Class** / Superclass / Induk).

Hubungan ini adalah hubungan "**is a**" ("adalah sebuah").
- `Mobil` adalah sebuah (is a) `Kendaraan`.
- `Kucing` adalah seekor (is a) `Hewan`.

**Analogi**: Pikirkan `Class Induk` (Parent) sebagai `Kendaraan`
- **Induk**: `Kendaraan`
    - Atribut: `nama`
    - Method: `maju()`
  
`Class Anak` (Child) adalah `Mobil`. Ia mewarisi semua yang dimiliki `Kendaraan`, lalu bisa menambahkan fiturnya sendiri
- Anak: `Mobil`
    - (Mewarisi `nama` dan `maju()` dari Kendaraan)
    - Method baru: `putar_AC()`

### Praktikum Percobaan - 1
```python
class Kendaraan:
    def __init__(self, nama):
        self.nama = nama
        print(f"Sebuah Kendaraan '{self.nama}' dibuat.")

    def maju(self):
        print(f"{self.nama} bergerak maju.")

class Mobil(Kendaraan):
    def putar_AC(self):
        print(f"{self.nama}: AC dinyalakan, sejuk!")

print("--- Membuat Object Mobil ---")
avanza = Mobil("Avanza Putih") 
avanza.maju() 
avanza.putar_AC()
```
Outputnya : 
```
--- Membuat Object Mobil ---
Sebuah Kendaraan 'Avanza Putih' dibuat.
Avanza Putih bergerak maju.
Avanza Putih: AC dinyalakan, sejuk!
```
Pertanyaan : 

1. Dari kode diatas mana class induk (parent) dan mana class anak (child)?
2. Buat objek dari class kendaraan!
3. Apakah objek yang dibuat dari class kendaaraan bisa mengakses method `putar_AC()`?
4. Apakah objek yang dibuat dari class Mobil bisa mengakses method `maji()`?
5. Mengapa pada class Mobil tidak perlu dibuat konstruktor?

## 2. `super()` - Memanggil Constructor Parent
Ini adalah masalah yang sering muncul:
- `Parent (Kendaraan)` punya `__init__(self, nama)`.
- `Child (Mobil)` juga perlu `__init__ `untuk menambahkan atribut baru, misalnya jumlah_pintu.

Jika kita membuat `__init__` di Child, itu akan mengganti (meng-override) `__init__` milik `Parent`. Akibatnya, `self.nama` tidak akan pernah dibuat.

Solusinya adalah menggunakan `super()`.

`super()` adalah "perwakilan" dari `Parent Class`. Perintah `super().__init__()` berarti: "Hei Parent, tolong jalankan dulu bagian `__init__` milikmu!"

Analogi: Kamu (`Child`) ingin membangun rumahmu sendiri. Kamu tidak perlu membangun fondasinya dari nol. Kamu panggil `super()` (kontraktor fondasi) untuk mengerjakan fondasinya (self.nama), setelah itu baru kamu tambahkan kamarmu sendiri (`self.jumlah_pintu`).

### Praktikum Percobaan - 2
```python
class Kendaraan:
    def __init__(self, nama):
        print("-> (Parent __init__ dipanggil)")
        self.nama = nama

class Mobil(Kendaraan):
    def __init__(self, nama, jumlah_pintu):
        print("-> (Child __init__ dipanggil)")
        
        super().__init__(nama) 
        
        self.jumlah_pintu = jumlah_pintu
        print(f"   -> Mobil {self.nama} dengan {self.jumlah_pintu} pintu dibuat.")

xenia = Mobil("Xenia Hitam", 4)
print(f"Nama object: {xenia.nama}")
```

Outputnya : 
```
-> (Child __init__ dipanggil)
-> (Parent __init__ dipanggil)
   -> Mobil Xenia Hitam dengan 4 pintu dibuat.
Nama object: Xenia Hitam
```

Pertanyaan:

1. Apa yang terjadi jika anda menghapus `super().__init__(nama`?
2. Jika error apa penyebabnya?
3. Menurut anda apakah `super()` bisa dipakai child memanggil method parent?

## 3. Override

**Override** adalah saat `Child Class` menimpa (mengganti) method yang sudah ada di `Parent Class`. Namanya sama, parameternya sama, tapi isinya (implementasinya) berbeda.

Analogi:
- `Parent (Hewan)` punya method `bersuara()` yang menghasilkan "Suara hewan...".
- `Child (Kucing)` mewarisinya, tapi `Kucing` tidak mau bersuara seperti itu.
- `Kucing` membuat ulang method `bersuara()` versi dirinya sendiri yang menghasilkan "Meow!".

### Praktikum Percobaan 3
```python
class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health

	def showInfo(self):
		print("showInfo di class Hero")
		print("{} health: {}".format(
			self.name,
			self.health
			)
		)

class Hero_intelligent(Hero):
	def __init__(self,name):
		super().__init__(name,100)

	def showInfo(self):
		print("showInfo di subclass Hero_intelligent")
		print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
			self.name,
			self.health
			)
		)

class Hero_strength(Hero):
	def __init__(self,name):
		super().__init__(name,200)


lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showInfo()
```
Output:
```
showInfo di subclass Hero_intelligent
lina 
        Tipe: intelligent, 
        health: 100
```
Pertanyaan:

1. Apa yang di override oleh child class?
2. Jika kita ingin menggunakan method `showInfor()` pada `parent class` apa yang harus dilakukan?

## 4. Multiple Inheritance 
Di Python, satu `Child Class` bisa mewarisi dari **lebih dari satu** `Parent Class`.

**Analogi**: Bayangkan sebuah `Smartphone`.
- `Smartphone` adalah sebuah `Telepon` (bisa menelepon).
- `Smartphone` adalah sebuah `KomputerMini` (bisa browsing).
- Jadi, `Class Smartphone` bisa mewarisi dari `Class Telepon` dan `Class KomputerMini` sekaligus.

### Praktikum Percobaan 4 
```python
class Ayah:
    def __init__(self, nama_ayah):
        self.nama_ayah = nama_ayah
    
    def bekerja(self):
        print(f"{self.nama_ayah} sedang bekerja.")

class Ibu:
    def __init__(self, nama_ibu):
        self.nama_ibu = nama_ibu

    def memasak(self):
        print(f"{self.nama_ibu} sedang memasak.")

class Anak(Ayah, Ibu):
    def __init__(self, nama_anak, nama_ayah, nama_ibu):
        Ayah.__init__(self, nama_ayah)
        Ibu.__init__(self, nama_ibu)
        self.nama_anak = nama_anak

    def bermain(self):
        print(f"{self.nama_anak} sedang bermain.")

budi = Anak("Budi", "Hendra (Ayah)", "Wati (Ibu)")

budi.bekerja()
budi.memasak() 
budi.bermain()
```

Outputnya : 
```
Hendra (Ayah) sedang bekerja.
Wati (Ibu) sedang memasak.
Budi sedang bermain.
```

Pertanyaannya : 

Apa yang terjadi jika `Ayah` dan `Ibu` sama-sama punya method dengan nama `mengasuh()`? Versi siapa yang akan dipakai Anak?

## TUGAS PRAKTIKUM 
**Sistem Gaji Karyawan di Perusahaan "TechMaju"**

**Skenario**: Kita akan membuat sistem HRD sederhana untuk perusahaan "TechMaju". Perusahaan ini memiliki berbagai jenis pegawai, tetapi kita akan fokus pada dua: `Manager` dan `StaffTeknis`.

Setiap pegawai (apapun jabatannya) pasti punya `nama`, `NIP` (Nomor Induk Pegawai), dan `gaji_pokok`. Namun, cara menghitung **bonus** mereka berbeda-beda.

Penerapan Konsep

1. Pilar Encapsulasi:
    - Atribut `__gaji_pokok` akan kita buat private di dalam `Class Pegawai`.
    - Tidak ada yang bisa menulis `pegawai.gaji_pokok = 99999` dari luar.
    - Kita hanya akan menyediakan getter (method) untuk `melihat` gaji total, bukan untuk mengubah gaji pokok.
    - Terdapat method getter `get_gaji_pokok()` untuk mendapatkan gaji_pokok private, pada `class Pegawai`
    - Terdapat method getter `get_gaji_total()` untuk menghitung gaji total pegawai yang merupakan hasil penjumlahan gaji pokok + bonus, dan hanya ada pada `class pegawai`
    - Terdapat method `tampilkan_info()` untuk mendapatkan informasi lengkap, `nama`, `nip`, dan `gaji pokok` pada `class pegawai`
    - Sertakan juga bukti enkapsulasi dengan mencoba mengakses gaji pokok dari luar class

2. Pilar Inheritance:
    - `Class Pegawai` akan menjadi **Parent Class**.
    - `Class Manager` akan menjadi **Child Class** yang mewarisi dari `Pegawai`.
    - `Class StaffTeknis` akan menjadi **Child Class** lain yang juga mewarisi dari `Pegawai` 
    - `Manager` dan `StaffTeknis` akan meng-override method `hitung_bonus()` sesuai aturan mereka masing-masing. Aturannya adalah : 
      - Bonus manager 15 persen dari gaji pokok 
      - Bonus staffTeknis adalah 500.000 dikali jumlah proyek yang dimiliki 
    - `Manager` dan `StaffTeknis` akan meng-override `__init__` dengan menambahkan atribut : 
      - `tunjangan_jabatan` untuk `manager`
      - `jumlah_proyek` untuk `staffTeknis`
    - `Manager` dan `StaffTeknis` akan meng-override `tampilkan_info()` dengan menambahkan infomasi `tunjangan_jabatan` (untuk manager) dan `jumlah_proyek` (untuk staffTeknis)

**Output Yang diharapkan** : 
```
--- Info Manager ---
Nama: Budi Hartono, NIP: M-001
Gaji Pokok: Rp 10,000,000
Tunjangan: Rp 5,000,000
Gaji Total Manager: Rp 11,500,000

==============================

--- Info Staff Teknis ---
Nama: Susi Susanti, NIP: S-001
Gaji Pokok: Rp 6,000,000
Jumlah Proyek: 3
Gaji Total Staff: Rp 7,500,000

==============================

--- Tes Keamanan (Encapsulasi) ---
ERROR: 'StaffTeknis' object has no attribute '__gaji_pokok'
-> TIDAK BISA diakses langsung dari luar!
Gaji Total Susi (tetap): Rp 7,500,000
````
