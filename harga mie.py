HARGA_INDOMIE_GORENG = 60000
HARGA_INDOMIE_KUAH = 50000
HARGA_SEDAP_GORENG = 55000
HARGA_SEDAP_KUAH = 45000
HARGA_SARIMI_GORENG = 52000
HARGA_SARIMI_KUAH = 47000

while True:
    nama_pembeli = input("Masukkan nama pembeli: ")
    jenis_mie = input("Pilih jenis mie (Indomie, Sedap Mie, Sarimi): ").lower()
    tipe_mie = input("Pilih tipe mie (goreng, kuah): ").lower()
    jumlah_beli = int(input("Masukkan jumlah beli (dalam karton): "))

    if jenis_mie == "indomie" and tipe_mie == "goreng":
        harga_mie = HARGA_INDOMIE_GORENG
    elif jenis_mie == "indomie" and tipe_mie == "kuah":
        harga_mie = HARGA_INDOMIE_KUAH
    elif jenis_mie == "sedap mie" and tipe_mie == "goreng":
        harga_mie = HARGA_SEDAP_GORENG
    elif jenis_mie == "sedap mie" and tipe_mie == "kuah":
        harga_mie = HARGA_SEDAP_KUAH
    elif jenis_mie == "sarimi" and tipe_mie == "goreng":
        harga_mie = HARGA_SARIMI_GORENG
    elif jenis_mie == "sarimi" and tipe_mie == "kuah":
        harga_mie = HARGA_SARIMI_KUAH
    else:
        print("Jenis atau tipe mie tidak valid.")
        continue  

    total_harga = harga_mie * jumlah_beli

    if jumlah_beli > 20:
        total_harga *= 0.9  

    bonus = ""
    if total_harga > 2000000:
        bonus = "Jas Hujan"
    elif total_harga > 1000000:
        bonus = "Payung"

    print(f"\nNama Pembeli: {nama_pembeli}")
    print(f"Total Harga: Rp {total_harga:,}")  
    if bonus:
        print(f"Bonus: {bonus}")
    else:
        print("Tidak ada bonus yang diterima.")
    lagi = input("Apakah ingin melakukan transaksi lain? (ya/tidak): ").lower()
    if lagi != "ya":
        print("Terima kasih")
        break 
