plat = input('Masukkan Plat Nomor :').split()
print(plat)

try:
    if plat[1]<=3000:
        print(f'Plat nomor {plat} diperuntukan untuk mobil')
    elif plat[1]>3000 and plat[1]<=4000:
        print(f'Plat nomor {plat} diperuntukan untuk motor')
    elif plat[1]>4000 and plat[1]<=5000:
        print(f'Plat nomor {plat} diperuntukan untuk angkutan umum')
    else:
        print('Plat Nomor Tidak Terinidikasi, harus terdapat nomor kendaraan setelah kode Daerah')
except:
    ()