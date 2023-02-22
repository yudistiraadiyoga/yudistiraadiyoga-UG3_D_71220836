plat = input('Masukkan Plat Nomor :').split()[1]
print(plat)
p = int(plat)
try:
    if p<=3000:
        print(f'Plat nomor tersebut diperuntukan untuk mobil')
    elif p>3000 and p<=4000:
        print(f'Plat nomor tersebut diperuntukan untuk motor')
    elif p>4000 and p<=5000:
        print(f'Plat nomor tersebut diperuntukan untuk angkutan umum')
    else:
        print('Plat Nomor Tidak Terinidikasi, harus terdapat nomor kendaraan setelah kode Daerah')
except:
    ()