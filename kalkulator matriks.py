#CALCULATOR MATRIKS
import numpy as np

nama = str(input("Masukkan Nama Lengkap : "))
nim = int(input("Masukkan NIM Anda : "))
prodi = str(input("Masukkan Program studi : "))

identitas = ("Hallo, Perkenalkan nama saya " + str(nama),"NIM " + str(nim) ,
             "dari Program Studi " + str(prodi), "\n Ini adalah Program perhitungan matriks")
print(identitas)
print("================== SELAMAT DATANG DI KALKULATOR MATRIKS ==================")

def menu(): # definisi menu
    # tampilan menu

    print('Menu:')
    print('1. Penjumlahan Matriks')
    print('2. Pengurangan Matriks')
    print('3. Perkalian Matriks')
    print('4. Determinant')
    print('5. Exit')
    print()

    # variabel untuk inputan pemilihan proses matriks yang akan dieksekusi
    pilihan = input('Pilih menu: ')

    # logika untuk masukkan nilai yang di input oleh user
    if pilihan == '1':
        penjumlahan()
        tanya()
    elif pilihan == '2':
        pengurangan()
        tanya()
    elif pilihan == '3':
        perkalian()
        tanya()
    elif pilihan == '4':
        determinant()
        tanya()
    elif pilihan == '5':
        print("Anda Keluar")
        exit()
    else:
        print('Pilihan Menu Salah')
        menu()

def penjumlahan(): # definisi untuk proses penjumlahan matriks
    print()
    print("Penjumlahan Matriks")
    menuordo()
    rumustambah() # pemanggilan definisi rumus tambah matriks
def pengurangan():
    print()
    print("Pengurangan Matriks")
    menuordo()
    rumuskurang() # pemanggilan definisi rumus kurang matriks
def perkalian():
    print()
    print("Perkalian Matriks")
    menuordo()
    rumuskali() # pemanggilan definisi rumus perkalian matriks
def determinant():
    print()
    print("Determinant Matriks")
    menuordo()
    rumusdeterminant() # pemanggilan definisi rumus determinan matriks

# menuordo()
# pemanggilan definisi menu ordo diperuntukan untuk user
# jika ingin menggunakan ordo 2x2 atau 3x3
def menuordo():
    print('a. Matriks ordo 2x2')
    print('b. Matriks ordo 3x3')
    print('c. Kembali')
    print()
    # logika pilih menu
    pilihan = input('Pilih menu: ')

    if pilihan in ['a', 'A']:
        print()
        print("================== MATRIKS ORDO 2X2 ==================")
    elif pilihan in ['b', 'B']:
        print()
        print("================== MATRIKS ORDO 3x3 ==================")
    elif pilihan in ['c', 'C']:
        print()
        menu()
    else:
        print('Pilihan Menu Salah')

def rumustambah(): # mendefinisikan rumus tambah
    x = int(input("Masukkan Ordo: "))
    print()
    print("================== Matriks A ==================")
    matrix_a = [[int(input())
    for i in range(x)] for i in range(x)]
    print("Matriks A: ")
    for n in matrix_a:
        print(n)
    print()
    print("================== Matriks B ==================")
    matrix_b = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks B: ")
    for n in matrix_b:
        print(n)
    print()
    result = [[0 for i in range(x)] for i in range(x)]
    for i in range(x):
        for j in range(x):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    print("Hasil Penjumalahan Matriks A + B: ")
    for r in result:
        print(r)

def rumuskurang(): # mendefinisikan rumus kurang
    x = int(input("Masukkan Ordo: "))
    print()
    print("================== Matriks A ==================")
    matrix_a = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks A: ")
    for n in matrix_a:
        print(n)
    print()
    print("================== Matriks B ==================")
    matrix_b = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks B: ")
    for n in matrix_b:
        print(n)

    print()
    result = [[0 for i in range(x)] for i in range(x)]
    for i in range(x):
        for j in range(x):
            result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    print("Hasil Pengurangan Matriks A - B: ")
    for r in result:
        print(r)

def rumuskali():
    x = int(input("Masukkan Ordo: "))
    print()
    print("================== Matriks A ==================")
    matrix_a = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks A: ")
    for n in matrix_a:
        print(n)

    print()
    print("================== Matriks B ==================")
    matrix_b = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks B: ")
    for n in matrix_b:
        print(n)
    print()

    result = [[0 for i in range(x)] for i in range(x)]

    for i in range(x):
        for j in range(x):
            for k in range(x):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    print("Hasil Pengurangan Matriks A * B: ")
    for r in result:
        print(r)

def rumusdeterminant():
    x = int(input("Masukkan Ordo: "))
    print()
    print("================== Matriks A ==================")
    matrix_a = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks A: ")
    for n in matrix_a:
        print(np.array(n))
    print()
    print("================== Matriks B ==================")
    matrix_b = [[int(input()) for i in range(x)] for i in range(x)]
    print("Matriks B: ")
    for n in matrix_b:
        print(np.array(n))
    print()

    result_a = np.linalg.det(matrix_a)
    result_b = np.linalg.det(matrix_b)

    print("Hasil Determinat Matriks A : ")
    print(result_a)
    print("Hasil Determinat Matriks B : ")
    print(result_b)

def tanya():
    pilih = input('Kembali ke menu? (y/t)')
    if pilih in ['y', 'Y', 'yes', 'Yes', 'YES', 'ya', 'YA','Ya']:
        menu()
    else:
        exit("Anda Keluar")

menu()