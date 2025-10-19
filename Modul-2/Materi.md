# MODUL - 2 : PRINSIP OOP BAGIAN 1 - ENCAPSULASI

>**Tujuan:** 
Mahasiswa memahami cara melindungi data object.

**Materi Pembelajaran :**
1. Encapsulasi
2. Akses Modifier : `public`, `private`, `protected`
3. Private Variabel
4. Static Method & Class Method
5. Setter & Getter

**Capaian Pembelajaran:**
1. Mahasiswa mampu menjelaskan konsep, tujuan, dan analogi sederhana prinsip OOP encapsulasi
2. Mahasiswa mampu menjelaskan dan menggunakan akses modifier OOP pada bahasa pemrograman python
3. Mahasiswa mampu menjelaskan dan menggunakan private variabel OOP pada bahasa pemrograman python
4. Mahasiswa mampu menjelaskan dan menggunakan static method dan class method OOP pada bahasa pemrograman python
5. Mahasiswa mampu menjelaskan dan menggunakan konsep setter dan getter pada bahasa pemrograman python


---
## 1. Apa itu Prinsip OOP Encapulation (Pembungkusan)

Kita akan mempelajari pilar pertama dalam OOP, yaitu **Enkapsulasi**

**Enkapsulasi** adalah ide untuk **membungkus** data (atribut) dan fungsi (method) menjadi satu unit tunggal, yaitu `Class`. Tujuannya adalah untuk menyembunyikan detail internal yang rumit dan hanya menyediakan antarmuka (interface) yang sederhana untuk digunakan.

**Analogi :** Pikirkan sebuah **televisi (TV)**
- Antarmuka *Publik*: Tombol `power`, `volume up`, `ganti channel` di remote. Ini adalah *method* yang bisa kita gunakan.
- **Detail Internal**: Sirkuit listrik, prosesor gambar, dan kabel-kabel rumit di dalamnya. Kita tidak perlu tahu (dan tidak boleh sembarangan mengubah) cara kerjanya.

> Sekarang, bayangkan sebuah **mobil**. Mana yang merupakan "antarmuka publik" (seperti remot TV) dan mana yang merupakan "detail internal" yang disembunyikan?


### Praktikum Percobaan - 1
```python
class Hero:

    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        self.__private = 'private'
        selt.__protected = 'protected'

hero_1 = Hero('Atsu', 100)

print(hero_1.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)
```
Pertanyaan:
1. Jelaskan perbedaan class variabel `jumlah` dan `__privateJumlah`!
2. Jelaskan perbedaan output pada tiga perintah `print`, jika terjadi error jelaskan apa yang menyebabkan error terjadi!


## 2. Akses Modifier & Private Variable
Seperti yang kita pahami pada bagian sebelumnya, bahwa enkapsulasi adalah soal "menyembunyikan kerumitan". Nah Akses modifier yang bertugas untuk mengatur bagian mana yang boleh diakses dan bagian mana yang terlarang. 

Pada bahasa pemrograman python terdapat 3 jenis akses modifier, yaitu `public`, `private`, dan `protected`, namun penulisannya pada python berbeda dengan bahasa pemrograman lainnya (seperti java). Dalam python penulisan akses modifier mengandalkan **konvensi** atau *kesepakatan bersama* antar programmer. 

Secara sederhana perbedaan tiap jenis modifier terlihat pada tabel berikut ini:
| Jenis     | Penulisan | Akses dari luar class         | Contoh         |
| --------- | --------- | ----------------------------- | -------------- |
| Public    | `nama`    | Bisa                          | `self.nama`    |
| Protected | `_saldo`  | Bisa tapi *disarankan jangan* | `self._saldo`  |
| Private   | `__saldo` | Tidak bisa langsung           | `self.__saldo` |

Analoginya : 
bayangkan anda memiliki kartu ATM
-   uang di bank = data(__saldo)
-   Mesin ATM = method yang boleh digunakan (misal deposit(), dan withdraw())
-   Di Bank anda tidak bisa langsung mengambil uang, paling tidak harus melewati ATM

### Praktikum Percobaan - 2  
Bayangkan kita mempunyai class `RekeningBank`, yang berisi informasi saldo nasabah, apakah bank mengizinkan nasabah lain melihat saldo kita?

```python
class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo 


akun_budi = RekeningBank("Budi", 1000000)
print(f"Saldo awal Budi: {akun_budi.saldo}")

akun_budi.saldo = -5000000
print(f"Saldo akhir Budi: {akun_budi.saldo}")
```
Pertanyaan : 
1. Apa modifier dari atribut?
2. Perbaiki kode ini agar yang hanya dapat diakses dari luar class hanyalah `nama` saja
3. Kemudian pastikan jika kode lain di luar class ingin mengakses `saldo` muncul peringatan `ERROR`. 
4. Anda dapat menggunakan modifier selain public pada `saldo`

## 3. Static Method dan Class Method
Pada modul sebelumnya kita sudah pernah membuat method (seperti `healthUp()`, `hitung_luas()`, atau `hitung_keliling()`), namun semua method ini adalah **Instance Method**. Artinya kita harus membuat objek dulu (seperti `hero_1`, `persegiPanjang`) sebelum bisa memanggil method ini. Selain itu method ini selalu menerima `self` sebagai penjelas atribut dari objek. 

Nah, pada bagian ini kita akan belajar dua method yang tidak terikat pada objek, namun terikat pada class (sama seperti class variabel yang terikat pada class bukan pada objek). 

### Class Method (`@classmethod`)

Merupakan method yang terikat pada class itu sendiri, dan bukan pada objek, cirinya : 
- menggunakan decorator `@classmethod`
- menerima referensi class berupa `cls` sebagai parameter pertama, dan bukan `self` yang merupakan referensi objek
- Bisa mengakses atribut class (variabel atau atribut yang dimiliki oleh class bukan objek)

Analoginya : Kita tidak perlu punya mobil Avanza (objek), untuk tahu pabrik Toyota (class) memproduksi mobil apa saja dan di negara mana saja. Pertanyaan ini merupakan pertanyaan yang harusnya ditujukan kepada class bukan pada objek. 

### Praktikum Percobaan 3.1 - Class Method
```python
class Mobil:
    
    total_mobil_dibuat = 0 

    def __init__(self, nama):
        self.nama = nama 
        Mobil.total_mobil_dibuat += 1 

    def nyalakan_mesin(self):
        print(f"Mesin {self.nama} menyala!")

    @classmethod
    def get_total_produksi(cls):
        print(f"Pabrik telah memproduksi {cls.total_mobil_dibuat} unit mobil.")


Mobil.get_total_produksi() 

print("--- Membuat mobil ---")
avanza = Mobil("Avanza")
xenia = Mobil("Xenia")
print("---------------------")

Mobil.get_total_produksi()
```
Pertanyaan : 
1. Sebutkan mana atribut class
2. Sebutkan mana atribut objek
3. Jelaskan fungsi dari class atribut pada kode ini?
4. Mana method objek dan jelaskan apa fungsinya pada kode ini?
5. Mana class method dan jelaskan apa fungsinya pada kode ini?
6. Jelaskan apa fungsi dari perintah `Mobil.get_total_produksi()`!


### Static Method (`@staticmethod`)

Method ini merupakan method yang paling terpisah, dan numpang tinggal di dalam class karena secara logika relevan ada di sana. Method ini memiliki ciri : 
- Menggunakan decorator `@staticmethod`
- Tidak menerima `self` dan `cls`

Analoginya : sebuah method untuk menghitung pajak pembelian kendaraan. Method ini tidak perlu tahu data Avanza (objek), dan tidak perlu tahu data pabrik (class). Method ini hanya perlu input harga untuk menghitung pajaknya. Method ini numpang tinggal di dalam class Mobil karena relevan dengan mobil. 

### Praktikum Percobaan 3.2 - Static Method
```python
class Kalkulator:

    def __init__(self, nilai_awal):
        self.nilai = nilai_awal
    
    def tambah(self, angka):
        self.nilai += angka
        return self.nilai

    @staticmethod
    def kali(a, b):
        return a * b

calc = Kalkulator(10)
print(f"Hasil tambah: {calc.tambah(5)}")

print(f"Hasil kali: {Kalkulator.kali(5, 3)}")
```

Pertanyaan : 
1. Jelaskan penjelasan dari perintah `print(f"Hasil tambah: {calc.tambah(5)}")` dan perintah `print(f"Hasil kali: {Kalkulator.kali(5, 3)}")`
2. Jelaskan juga perbedaannya. 

### Perbedaan Class Method dan Static Method
| Jenis Method                    | Parameter Pertama | Cara Panggil     | Kapan Digunakan?                                                       |
| ------------------------------- | ----------------- | ---------------- | ---------------------------------------------------------------------- |
| Instance Method (biasa)         | `self` (object)   | `objek.method()` | Aksi yang spesifik untuk 1 object                                      |
| Class Method (`@classmethod`)   | `cls`(class)      | `Class.method()` | Aksi yang berhubungan dengan Class/Pabrik                              |
| Static Method ('@staticmethod`) | Tidak Ada         | `Class.method()` | Fungsi bantu (utility) yang relevan, tapi tidak butuh data objek/class |


## 4. Setter dan Getter
Konsep `setter` dan `getter` secara khusus merupakan mekanisme utama untuk menjalankan enkapsulasi. Ide sederhanannya jika kita memiliki atribut penting (seperti `__saldo` atau `__nilai`) dibuat private agar tidak bisa diakses sembarangan. Supaya kode diluar class dapat mengubah dan mengakses variabel private, maka disediakan dua mekanisme, yaitu : 
1. **Getter**, digunakan untuk membaca data atau variabel private
2. **Setter**, digunakan untuk menulis variabel private dan disinilah kita memberikan logika validasi

### Praktikum Percobaan 4.1. - Cara Klasik : Method `get_` dan `set_`

Ini merupakan metode setter dan getter yang paling banyak digunakan pada bahasa pemrograman (seperti java). Bayangkan kita memiliki `class Siswa` dengan nilai yang tidak boleh lebih dari 100 atau kurang dari 0

```python
class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = 0  
        self.set_nilai(nilai) 

    # GETTER: Hanya untuk 'membaca'
    def get_nilai(self):
        print(f"(Akses getter untuk {self.nama})")
        return self.__nilai

    # SETTER: 'Satpam' untuk 'menulis'
    def set_nilai(self, nilai_baru):
        print(f"(Akses setter untuk {self.nama} dengan nilai {nilai_baru})")
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
            print("-> Nilai berhasil diupdate.")
        else:
            print(f"-> Gagal! Nilai {nilai_baru} tidak valid. Harus antara 0-100.")


budi = Siswa("Budi", 70) 

budi.set_nilai(95)

budi.set_nilai(105)


print(f"Nilai Budi sekarang: {budi.get_nilai()}")
```
Pertanyaan : 
1. Jelaskan apa fungsi perintah `self.nilai = 0` dan `self.set_nilai(nilai)`!
2. Jelaskan baris per baris apa fungsi dari method `set_nilai()`!
3. Jelaskan apa kelemahan dengan menggunakan cara ini!

### Praktikum Percobaan 4.2 - Cara Pythonic Menggunakan `@property`
Python memiliki cara yang jauh lebih elegan untuk menerapkan setter dan getter, yaitu menggunakan decorator `@property` dan `@<nama_property>.setter`, berikut penjelasannya : 
- `@property`, decorator mengubah method Getter menjadi seperti atribut (bisa diakses tanpa tanda kurung `()`)
- `@<nama_property>.setter`, decorator mengubah method setter agar dapat diisi menggunakan tanda sama dengan (`=`)

```python
class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        # Saat kita menulis 'self.nilai = nilai' di sini,
        # ini OTOMATIS memanggil method 'setter' di bawah.
        self.nilai = nilai 

    # 1. GETTER (menggunakan @property)
    @property
    def nilai(self):
        print("(Memanggil getter @property)")
        return self.__nilai

    # 2. SETTER (menggunakan @<nama_getter>.setter)
    @nilai.setter
    def nilai(self, nilai_baru):
        print(f"(Memanggil setter @nilai.setter dengan nilai {nilai_baru})")
        
        # Logika validasi ('satpam') tetap di sini
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
            print("-> Nilai berhasil diupdate.")
        else:
            print(f"-> Gagal! Nilai {nilai_baru} tidak valid.")

# --- Mari kita coba cara baru ---
susi = Siswa("Susi", 80)
# Output:
# (Memanggil setter @nilai.setter dengan nilai 80)
# -> Nilai berhasil diupdate.

print("-" * 20)

# A. Mengubah nilai (terlihat seperti atribut, tapi memanggil SETTER)
susi.nilai = 101 # Ini memanggil 'def nilai(self, 101)'
# Output:
# (Memanggil setter @nilai.setter dengan nilai 101)
# -> Gagal! Nilai 101 tidak valid.

print("-" * 20)

susi.nilai = 90  # Ini memanggil 'def nilai(self, 90)'
# Output:
# (Memanggil setter @nilai.setter dengan nilai 90)
# -> Nilai berhasil diupdate.

print("-" * 20)

# B. Membaca nilai (terlihat seperti atribut, tapi memanggil GETTER)
print(f"Nilai Susi sekarang: {susi.nilai}")
# Output:
# (Memanggil getter @property)
# Nilai Susi sekarang: 90
```

Pertanyaan : 

Jelaskan dimana letak perbedaan antara cara klasing dengan cara pythonic, dan apa keuntungannya menggunakan cara pythonic!




## TUGAS PRAKTIKUM

**Tugas: Membuat Class `Hero` untuk Sebuah Game**

Anda adalah seorang programmer yang ditugaskan untuk membuat class untuk para `Hero` dalam sebuah game

class ini harus memiliki logika internal yang kuat, dimana status(stats) `Hero` tidak bisa diubah sembarangan dari luar class. Anda harus menggunakan prinsip enkapsulasi secara ketat

**Persyaratan:** 
1. Nama Class:
   - Buat class dengan nama : `Hero`
2. Variabel class (private):
   - class `Hero` harus bisa menghitung berapa total `Hero` yang telah dibuat
   - Buat sebuah private class variabel bernama `__jumlah` yang akan bertambah +1 setiap kali sebuah objek `Hero` baru dibuat
3. Konstruktor (`__init__`):
   - `__init__` harus menerima empat parameter (`nama`, `health`, `attPower`, dan `armor`)
   - **PENTING**: Semua atribut di dalam `__init__` harus bersifat **private** (gunakan `__` di depan nama atribut)
   - Simpan `nama`, `health`, `attPower`, dan `armor` ke dalam atribut standar (base stats), contoh: `self.__name`, `self.__healthStandar`, `self.__attPowerStandar`, `self.__armorStandar`
   - Buat juga atribut `self.__level` (dimulai dari 1) dan `self.__exp` (dimulai dari 0)
   - Buat atribut dimanis yang nilainya bergantung pada level:
     - `self.__healthMax` = `self.__healthStandar * self.__level`
     - `self.__attPower` = `self.__attPowerStandar * self.__level`
     - `self.__armor` = `self.__armorStandar * self.__level`
   - Terakhir buat `self.__health` (darah saat ini) yang nilainya sama dengan `self.__healthMax`
   - Jangan lupa untuk menambahkan 1 ke `Hero.__jumlah` di dalam `__init__`
4. Sistem Level Up (Setter untuk `gainEXP`):
   - Buat sebuah property setter bernama `gainEXP`. ini adalah gerbang untuk menambahkan nilai experience (EXP)
   - Setter ini akan menerima satu parameter, yaitu `addEXP`
   - Logikanya : 
     - Tambahkan `addEXP` ke `self.__exp`
     - Buat perulangan `while` (atau `if` sederhana jika exp tidak akan naik > 1 level sekaligus) yang mengecek apakah `self.__exp >= 100`
     - Jika `True`:
       - Cetak pesan : `[nama hero] level up`
       - naikkan `self.__level` sebanyak 1
       - kurangi `self.__exp` sebanyak 100
       - PENTING : hitung ulang semua atribut dinamis (`__healthMax`, `__attPower`, `__armor`) berdasarkan `__level` baru
     - Anda juga perlu membuat property getter `gainEXP` (cukup diisi `pass`) agar setter-nya bisa berfungsi
5. Method `attack`:
   - Buat sebuah method `attack` yang menerima satu parameter `musuh`
   - Setiap kali `Hero` menyerang, panggil setter `gainEXP` untuk menambahkan 50 exp ke `Hero` tersebut (gunakan `self.gainEXP = 50`)
6. Menampilkan info (Getter untuk `info`):
   - Buat sebuah read-only property (hanya getter) bernama `info`
   - Saat diakses, `info` harus mengembalikan sebuah string multi line yang diformat persis seperti ini : 
        ```
        [nama] level [level]: 
            health = [health]/[healthMax] 
            attack = [attPower] 
            armor = [armor]
        ```
   - Gunakan `\n` untuk baris baru dan `\t` untuk tab

Kode untuk Test Case 
```python
slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)
```

Hasil yang diharapkan 

```
slardar level 1: 
	health = 100/100 
	attack = 5 
	armor = 10
slardar level up
slardar level 2: 
	health = 200/200 
	attack = 10 
	armor = 20
```

