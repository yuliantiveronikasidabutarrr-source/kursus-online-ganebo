while True:
    print('KURSUS ONLINE "GANEBO"')
    print("______________________")

    jumlah = int(input("Masukkan Jumlah Data          : "))

    data = []
    total = 0

    for i in range(jumlah):
        print(f"\nData ke-{i+1}")
        nama = input("Masukkan Nama Siswa           : ")
        paket = input("Masukkan Paket Kursus [1/2/3] : ")

        if paket == "1":
            nama_paket = "Cerdas"
            materi = "Android Programming"
            harga = 3000000
        elif paket == "2":
            nama_paket = "Ceria"
            materi = "Desain Grafis"
            harga = 2500000
        elif paket == "3":
            nama_paket = "Smile"
            materi = "Multimedia"
            harga = 2000000
        else:
            print("Paket tidak valid!")
            continue

        total += harga
        data.append([i+1, nama, nama_paket, harga, materi])

    print("REKAPITULASI PENDAFTARAN KURSUS ONLINE")
    print("____________________________________________________")
    print("No  Nama Siswa     Nama Paket   Harga       Materi")
    print("____________________________________________________")

    for d in data:
        print(d[0], d[1], d[2], "Rp.", d[3], d[4])

    print("____________________________________________________")
    print(f"Total               Rp. {total}")

    uang_bayar = int(input("Uang Bayar          Rp. "))
    kembali = uang_bayar - total

    print(f"Uang Kembali        Rp. {kembali}")

    lagi = input("Transaksi Lagi [Y/T] ? ").lower()
    if lagi != "y":
        print("=== Terima Kasih ===")
        break
