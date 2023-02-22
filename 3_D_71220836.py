awal = int(input('Masukkan awal deret :'))
akhir = int(input('Masukkan akhir deret :'))
nilai = range(awal,akhir)
print(nilai) if nilai%6 and nilai%8 else print('Angka tidak valid')