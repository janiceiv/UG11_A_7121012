def ambildanbalik(kalimat, mulai, akhir, perintah):
    if perintah == True:
        a = int(mulai) - 1
        b = int(akhir) - 1
        kata = kalimat[a] kalimat[b]
        print(reversed(kata))

    else:
        a = int(mulai) - 1
        b = int(akhir) - 1
        kata = kalimat[a], kalimat[b]
        print(kata)


ambildanbalik("abcdefg", 2, 4, True)
ambildanbalik("abcdefg",1,5,False)
ambildanbalik("Qwerty",3,4,True)
ambildanbalik("Qwerty",2,2,False)
