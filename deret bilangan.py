print("Program mencari suku ke-n dari deret bilangan.")

while True:
    soal = input("Pilih soal (a - j) atau ketik 'exit' untuk berhenti: ").lower()
    if soal == 'exit':
        break

    n = int(input("Masukkan nilai n yang diinginkan: "))

    if soal == 'a':
        a = 1
        d = 4
        suku_n = a + (n - 1) * d
        print("Hasil suku ke-", n, "dari deret a adalah:", suku_n)

    elif soal == 'b':
        a = 3
        d = 9
        suku_n = a + (n - 1) * d
        print("Hasil suku ke-", n, "dari deret b adalah:", suku_n)

    elif soal == 'c':
        a = 100
        d = -6
        suku_n = a + (n - 1) * d
        print("Hasil suku ke-", n, "dari deret c adalah:", suku_n)

    elif soal == 'd':
        a = 35
        d = -7
        suku_n = a + (n - 1) * d
        print("Hasil suku ke-", n, "dari deret d adalah:", suku_n)

    elif soal == 'e':
        a = 1
        suku_n = a
        beda = 1
        for i in range(1, n):
            suku_n += beda
            beda += 1
        print("Hasil suku ke-", n, "dari deret e adalah:", suku_n)

    elif soal == 'f':
        a = 30
        d = -1
        suku_n = a + (n - 1) * d
        print("Hasil suku ke-", n, "dari deret f adalah:", suku_n)

    elif soal == 'g':
        a = 1
        r = 2
        suku_n = a * (r ** (n - 1))
        print("Hasil suku ke-", n, "dari deret g adalah:", suku_n)

    elif soal == 'h':
        a = 6
        d = 3
        suku_n = a + (n - 1) * d
        print("Hasil suku ke-", n, "dari deret h adalah:", suku_n)

    elif soal == 'i':
        a = 0.1
        d = 0.1
        suku_n = a + (n - 1) * d
        print("Hasil suku ke-", n, "dari deret i adalah:", suku_n)

    elif soal == 'j':
        a = 1
        r = 0.5
        suku_n = a * (r ** (n - 1))
        print("Hasil suku ke-", n, "dari deret j adalah:", suku_n)

    else:
        print("Soal tidak ditemukan. Silakan pilih antara a - j.")
    
    print() 

print("Program selesai.")
