from collections import deque

# Membuat queue (antrian)
antrian = deque()

while True:
    print("\n=== SISTEM ANTRIAN PASIEN ===")
    print("1. Tambah Pasien (Enqueue)")
    print("2. Layani Pasien (Dequeue)")
    print("3. Lihat Antrian")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama pasien: ")
        antrian.append(nama)
        print(f"Pasien {nama} masuk ke antrian.")

    elif pilihan == "2":
        if len(antrian) > 0:
            pasien = antrian.popleft()
            print(f"Pasien {pasien} sedang dilayani.")
        else:
            print("Antrian kosong!")

    elif pilihan == "3":
        if len(antrian) > 0:
            print("Daftar Antrian:")
            for i, pasien in enumerate(antrian, start=1):
                print(f"{i}. {pasien}")
        else:
            print("Antrian kosong!")

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")