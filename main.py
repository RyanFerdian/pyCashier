from menu import menu
from fpdf import FPDF
from datetime import datetime

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

# Membuat PDF untuk struk pembayaran
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="================ Struk Pembayaran ================", ln=True, align='C')

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

    # tambahkan ke PDF
    pdf.cell(200, 10, txt=f"pesanan ke-{i}", ln=True)
    pdf.cell(200, 10, txt=f"Pesanan Makanan  : {makanan:<20} = Rp{harga_makanan}", ln=True)
    pdf.cell(200, 10, txt=f"Pesanan Minuman  : {minuman:<20} = Rp{harga_minuman}", ln=True)
    pdf.cell(200, 10, txt=f"Jumlah Pesanan   : {jumlah}", ln=True)
    pdf.cell(200, 10, txt=f"jumlah Total     : Rp{total_item}", ln=True)
    pdf.cell(200, 10, txt="", ln=True)  # baris kosong

pdf.cell(200, 10, txt="=" * 50, ln=True)
pdf.cell(200, 10, txt=f"TOTAL PEMBAYARAN : Rp {total_bayar}", ln=True)
pdf.cell(200, 10, txt="=" * 50, ln=True)

# Simpan PDF dengan timestamp untuk menghindari overwrite
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f"struk_pembayaran_{timestamp}.pdf"
pdf.output(filename)

print(f"Struk pembayaran telah disimpan sebagai '{filename}'")
