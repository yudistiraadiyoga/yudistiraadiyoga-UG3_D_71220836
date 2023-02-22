nama = str(input('Masukkan Nama Lengkap Anda\t\t\t:'))
prodi = str(input('Masukkan Prodi Anda\t\t\t\t:'))
nilai = str(input('Masukkan Nilai (dalam huruf) yang Anda Dapat\t:')).upper()
try:
    if nilai == 'A':
        print('Nilai anda adalah 4.0, tbl tbl serem bgt lohh')
    elif nilai == 'A-':
        print('Nilai anda adalah 3.75, kamu keren!')
    elif nilai == 'B+':
        print('Nilai anda adalah 3.25, kamu keren!')
    elif nilai == 'B':
        print('Nilai anda adalah 3.0, kamu keren!')
    elif nilai == 'B-':
        print('Nilai anda adalah 2.75, kurang semangat belajar nihh')
    elif nilai == 'C+':
        print('Nilai anda adalah 2.25, waduhh gimana ni')
    elif nilai == 'C':
        print('Nilai anda adalah 2.0, kok segini?')
    elif nilai == 'D':
        print('Nilai anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan?')
    elif nilai == 'E':
        print('Nilai anda adalah 0, niat kuliah nggak sih???')
    else:
        print('Inputan nilai yang Anda masukkan tidak valid')
except:
    ()