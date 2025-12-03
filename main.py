from menu import menu

# mencatak menu makanan dan minuman
print("-" * 60)
print(f"{'menu':<20} | {'Harga':<7} | {'minuman':<15} | {'Harga':<7} |")
print("-" * 60)

#zip untuk menggabungkan dua dictionary, for untuk perulangan
for (makanan, harga), (minuman, harga_minum) in zip (menu["makanan"].items(), menu["minuman"].items()):
    print(f"{makanan:<20} : Rp{harga} | {minuman:<15} : Rp{harga_minum:<5} |")
print("-" * 60)

# input pesanan dari user
daftar_pesanan = []
ulang = "y"
while ulang == "y":
    pesanan = input("Pilih Menu     : ")
    pesanan_minum = input("Pilih Minuman  : ")
    jumlah = int(input("Jumlah Pesanan : "))
    
    #menyimpan pesanan
    daftar_pesanan.append([pesanan, pesanan_minum, jumlah])

    #opsi mengulang pesanan
    ulang = input("ingin tambah pesanan ? (y/n) : ")

print("================ Struk Pembayaran ================")
total_bayar = 0
for i, item in enumerate(daftar_pesanan, start=1):
    makanan, minuman, jumlah = item
    #fungsi 'enumerate' membuat sebuah loop yang memberikan 2 nilai sekaligus

    # mengambil harga makanan dan minuman dari file menu.py
    harga_makanan = menu['makanan'].get(makanan, 0)
    harga_minuman = menu['minuman'].get(minuman, 0)

    # hitung subtotal untuk makanan dan minuman 
    subtotal_makanan = harga_makanan * jumlah
    subtotal_minuman = harga_minuman * jumlah

    # total untuk item = subtotal makanan + subtotal minuman
    total_item = subtotal_makanan + subtotal_minuman
    total_bayar += total_item

    # cetak struk pembayaran
    print(f"\npesanan ke-{i}")
    print(f"Pesanan Makanan  : {makanan:<20} = Rp{harga_makanan}")
    print(f"Pesanan Minuman  : {minuman:<20} = Rp{harga_minuman}")
    print(f"Jumlah Pesanan   : {jumlah}")
    print(f"jumlah Total     : Rp{total_item}")

print("=" * 50)
print(f"TOTAL PEMBAYARAN : Rp {total_bayar}")
print("=" * 50)
