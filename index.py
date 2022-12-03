import modul
import mylist

modul.garis()
modul.oss()
nama = input('Masukkan Nama Pelanggan : ')
nama_pelanggan = nama.title()
modul.oss()
modul.garis()
print(f"| {'Masukkan Kode Pelanggan Untuk Mendapatkan Diskon':<25}{'|':>7}")
modul.garis()
print(f"| {'M = Member (disc 7%)':<25}{'|':>30}")
print(f"| {'N = Non Member (disc 0%)':<25}{'|':>30}")
modul.garis()
# Kode Pelanggan
kode_pelanggan = input('Kode Pelanggan : ')
if (kode_pelanggan.lower() == 'm'):
    diskon_m = 0.07
    diskon_s = '7%'
    status_pelanggan = 'Member'
elif (kode_pelanggan.lower() == 'n'):
    diskon_m = 0
    diskon_s = '0%'
    status_pelanggan = 'Non Member'
modul.oss()
ulang = 'y'
yu = 0

while ulang.lower() == 'y':
    g = 2  # garis
    modul.garis(g)
    print(f"| {'Nama Pelanggan   :':>} {nama_pelanggan:>36} |")
    print(f"| {'Status Pelanggan :':>} {status_pelanggan:>36} |")
    print(f"| {'Diskon Member    :':>} {diskon_s:>36} |")
    modul.garis(g)
    print(f"|{'List Produk':^57}|")
    modul.garis(g)
    print(f"|{'Kode':^8}| {'Jenis':^8}| {'Nama Produk ':^25}| {'Harga':^10}| ")
    modul.garis(g)
    for i in range(0, 6):
        print(
            f"|{mylist.minuman[i][0].upper():^8}| {mylist.minuman[i][3]:^8}| {mylist.minuman[i][1]:<25}| RP{mylist.minuman[i][2]:>7} | ")
    for x in range(0, 6):
        print(
            f"|{mylist.makanan[x][0].upper():^8}| {mylist.makanan[x][3]:^8}| {mylist.makanan[x][1]:<25}| RP{mylist.makanan[x][2]:>7} | ")
    modul.garis(g)

    def keranjangi(m=yu, u=yu):
        global po, l
        po = u
        kode = mylist.menu[m][u][0]
        nama = mylist.menu[m][u][1]
        harga = mylist.menu[m][u][2]
        jenis = mylist.menu[m][u][3]
        l = [kode, nama, harga, jenis]
        if u >= 0:
            mylist.keranjang.update({yu: l})
        return l

    kd_barang = str(input('Masukkan Kode Barang   : '))
    if (kd_barang.lower() == 'p1'):
        keranjangi(0, 0)
    elif (kd_barang.lower() == 'p2'):
        keranjangi(0, 1)
    elif (kd_barang.lower() == 'p3'):
        keranjangi(0, 2)
    elif (kd_barang.lower() == 'p4'):
        keranjangi(0, 3)
    elif (kd_barang.lower() == 'p5'):
        keranjangi(0, 4)
    elif (kd_barang.lower() == 'p6'):
        keranjangi(0, 5)
    elif (kd_barang.lower() == 'm1'):
        keranjangi(1, 0)
    elif (kd_barang.lower() == 'm2'):
        keranjangi(1, 1)
    elif (kd_barang.lower() == 'm3'):
        keranjangi(1, 2)
    elif (kd_barang.lower() == 'm4'):
        keranjangi(1, 3)
    elif (kd_barang.lower() == 'm5'):
        keranjangi(1, 4,)
    elif (kd_barang.lower() == 'm6'):
        keranjangi(1, 5,)

    jumlah = int(input('Masukkan Jumlah pembelian :'))
    l.append(jumlah)
    mylist.keranjang.update({yu: l})
    keys = mylist.keranjang.keys()
    yu += 1
    modul.oss()
    ulang = input("Ingin menambah data? Y/N : ")
    modul.oss()
p = 8  # garis
modul.garis(p)
print(f"| {'TOKO MULYO MAKMUR SENTOSA':^61} |")
modul.garis(p)
print(f"| {'Nama Pelanggan        :':>} {nama_pelanggan:>37} |")
print(f"| {'':>23} {status_pelanggan:>37} |")
modul.garis(p)
modul.garis(p)
print(f"|{'Kode':^8}| {'Jenis':^8}| {'Nama Produk ':^25}| {'Harga':^15} | ")
modul.garis(p)
hrgg = {
}
for i in mylist.keranjang.keys():
    hrg = mylist.keranjang.get(i)[2]
    jml = mylist.keranjang.get(i)[4]
    harga = hrg * jml
    hrgg.update({i: harga})
    print(
        f"|{mylist.keranjang.get(i)[0].upper():^8}| {mylist.keranjang.get(i)[3]:^8}| {mylist.keranjang.get(i)[1]:^25}|    RP.{hrg:<4,.0f}*{jml:>3}{' |'} ")
x = sum(hrgg.values())
if x > 50000:
    pot_m = diskon_m * x
    pot_lebih = 5/100*(x - 50000)
else:
    pot_m = diskon_m * x
    pot_lebih = 0/100*(x - 50000)
harga_bayar = x - (pot_m + pot_lebih)
modul.garis(p)
print(f"| {'Diskon Member         :':<40} {'RP.':>11} {pot_m:>8,.0f} |")
print(f"| {'Diskon lebih dari 50k :':<40} {'RP.':>11} {pot_lebih:>8,.0f} |")
print(f"| {'Total Bayar           :':<40} {'RP.':>11} {harga_bayar:>8,.0f} |")
modul.garis(p)
print(f"| {'TERIMAKASIH':^61} |")
modul.garis(p)

input("Press ENTER to exit")
