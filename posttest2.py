from prettytable import PrettyTable
# list untuk menyimpan data item
album = [
    ["101", "Radiohead - OK Computer", 789.999, 2],
    ["102", "The Beatles - Revolver", 859.999, 1],
    ["103", "Mac Demarco - This Old Dog", 659.999, 5],
    ["104", "Sheila on 7 - Berlayar", 777.777, 1],
    ["105", "Metallica - Thunderstruck", 829.999, 2]
]

# menampilkan seluruh item yang terdapat dalam database dengan prettytable
def show_item():
    table = PrettyTable()
    table.field_names = ["ID", "Band - Album", "Harga", "Stok Album"]
    for item in album :
        table.add_row(item)
    print(table)

    
# Pembeli
def transaksi():
    while True:
        # menampilkan seluruh item yang tersedia
        print("Daftar Album yang Tersedia")
        show_item()
        
        # input id item dan jumlah yang ingin dibeli
        id_item = input("Masukkan ID Album yang ingin dibeli : ")
        qty = int(input("Masukkan jumlah yang ingin dibeli : "))
        
        # memeriksa apabila jumlah yang ingin dibeli melebihi stok
        for item in album:
            if item[0] == id_item:
                if qty > item[3]:
                    print("Maaf, stok barang tidak mencukupi!")
                    break
        else:
            # melakukan update stok pada item yg dibeli
            for i in range(len(album)):
                if album[i][0] == id_item:
                    album[i][3] -= qty
                    
                    # menampilkan struk pembayaran
                    if album[i][0] == id_item:
                        nama_album = album[i][1]
                        harga_album = float(album[i][2])
                        total = harga_album * qty
                        print ("=" * 60)
                        print ("                 Struk Pembelian Album")
                        print ("=" * 60)
                        print (f"""
            Album : {nama_album}
            Jumlah  : {qty}
            Total   : Rp {total}
                            """)
                        print ("=" * 60)
                        print("       Terima Kasih Telah Membeli Album di Toko Kami :)")
                        print ("=" * 60)
                        
                        while True:
                            pilihan = input("Apakah Ingin Membeli Lagi? (y/t): ").lower()
                            if pilihan == "t":
                                return
                            elif pilihan == "y":
                                break
                            else:
                                print("pilihan tidak tersedia")
                                
        # menampilkan kembali tampilan daftar item apabila stok tidak mencukupi
        print()

# Admin
def create():
    # input data item yang baru
    id_item = input("Masukkan ID Album: ")
    nama_item = input("Masukkan Nama Album: ")
    harga_item = input("Masukkan Harga Album: ")
    stok_item = int(input("Masukkan Stok Album: "))
    
    # menambahkan item yang baru ke dalam database
    album.append([id_item, nama_item, harga_item, stok_item])
    
    # menampilkan daftar item lengkap dengan item baru yang ditambahkan
    show_item()

def read():
    # menampilkan seluruh item yang terdapat dalam database
    show_item()

def update():
    # input id item yang ingin diperbarui
    id_item = input("Masukkan ID item yang ingin di-update data: ")
    for i in range(len(album)):
        if album[i][0] == id_item:
            # input data item yang baru
            nama_item = input("Masukkan Album Baru: ")
            harga_item = input("Masukkan Harga Album Baru: ")
            stok_item = int(input("Masukkan Stok Album Baru: "))
            
            # melakukan update item yang dipilih
            album[i][1] = nama_item
            album[i][2] = harga_item
            album[i][3] = stok_item
            
            # menampilkan daftar item yang terbaru
            show_item()
            break
    else:
        print("Album tidak ditemukan")

def delete():
    # input id item yang ingin dihapus
    id_item = input("Masukkan ID Album yang ingin dihapus: ")
    for i in range(len(album)):
        if album[i][0] == id_item:
            # menghapus item sesuai input id
            album.pop(i)
            
            # menampilkan daftar item yang terbaru
            show_item()
            break
    else:
        print("Album tidak ditemukan")
    


# program utama
while True:
    print("="*30)
    print("    FJR VINYL ALBUM STORE")
    print("="*30)
    print("1. LOGIN ")
    print("2. KELUAR")
    
    
    menu_login = input("Silahkan Pilih Menu Dibawah ini :")
    
    #login akan langsung menentukan pembeli atau admin
    if menu_login == "1" :
        username = input("Masukkan Username Anda : ")
        password = input("Masukkan Password Anda : ")
        
        #program akan otomatis menentukan pembeli atau admin
        if username == "admin" and password == "admin123" :
            print("="*30)
            print("admin bocah skena mau ngapaen?")
            print("="*30)
            print("1. Tambah Album")
            print("2. Lihat Album")
            print("3. Update Album")
            print("4. Hapus Album")
            print("5. Kembali")

            admin_choice = input("Pilih menu: ")
            if admin_choice == "1":
                create()
            elif admin_choice == "2":
                read()
            elif admin_choice == "3":
                update()
            elif admin_choice == "4":
                delete()
            elif admin_choice == "5":
                continue
            else:
                print("Menu tidak tersedia")
        #jika username dan password yang di input bukan akun admin maka program pembeli akan muncul
        else:
            print("-"*40)
            print("Selamat Berbelanja Album Musik", username)
            print("-"*40)
            transaksi()
    elif menu_login == "2":
        print("Terima kasih telah menggunakan aplikasi ini")
        break
    else:
        print("Input Anda Tidak Valid")