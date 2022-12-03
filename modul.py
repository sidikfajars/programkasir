import os
import mylist


def garis(a=0):
    global b
    b = a + 57
    return print('-'*b)


def oss():
    return os.system('cls')


# def keranjangi(m=yu, u=yu):
#     global po, l
#     po = u
#     kode = mylist.menu[m][u][0]
#     nama = mylist.menu[m][u][1]
#     harga = mylist.menu[m][u][2]
#     jenis = mylist.menu[m][u][3]
#     l = [kode, nama, harga, jenis]
#     if u >= 0:
#         mylist.keranjang.update({yu: l})
#     return l
