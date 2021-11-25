def calculator():
    print("======= Calculator Sederhana =======")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    
calculator()

pilih = int(input("Masukkan pilihan : "))
bil1 = int(input("Masukkan bilangan 1 : "))
bil2 = int(input("Masukkan bilangan 2 : "))

def tambah():
    tambah = bil1 + bil2
    print ("Hasilnya: ", tambah)

def kurang():
    kurang = bil1 - bil2
    print ("Hasilnya: ", kurang)

def bagi():
    bagi = bil1/bil2
    print ("Hasilnya: ", bagi)

def kali ():
    kali = bil1 * bil2
    print ("Hasilnya: ", kali)

def pangkat():
    pangkat = bil1 ** bil2
    print ("Hasilnya: ", pangkat)
    

if pilih == 1:
    tambah()

elif pilih == 2:
    kurang()

elif pilih == 3:
    bagi()

elif pilih == 4:
    kali ()

elif pilih == 5:
    pangkat()

else:
    print("Hasilnya: Maaf input operasi antara 1-5")

