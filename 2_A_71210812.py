def ambil_tengah(kalimat, tambahan = "0"):
    tengah = len(kalimat)/2
    if tengah %2 == 0:
        hasil = int(tengah) + int(tambahan)
        print(kalimat[hasil])
    else:    
        akhir = round(tengah) - 1 + int(tambahan)
        print(kalimat[akhir])


ambil_tengah("abcdefg", 1)
ambil_tengah("abcdefg", 2)
ambil_tengah("abcd")
