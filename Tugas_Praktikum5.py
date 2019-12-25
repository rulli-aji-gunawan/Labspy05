
daftar = {}

while True:
    print("")
    c = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")
    if c.lower() == 'k':
        break
    elif c.lower() == 'l':
        print("Daftar Nilai")
        garis = 79
        print('=' * garis)
        print( '| No |    NIM    |          Nama          |  Tugas  |  UTS  |  UAS  |  Akhir  |')
        print('=' * garis)
        for no, i in zip (range (1,len(daftar)+1), daftar.items()) :
            print('| {0:2d} |  {1:7d}  |  {2:20s}  |  {3:5d}  |  {4:3d}  |  {5:3d}  |  {6:5.2f}  |'
                  .format(no, i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5]))
        print('=' * garis)

    elif c.lower() == 't':
        print("Tambah Daftar")
        nim = int(input('Masukkan NIM : '))
        nama = str(input('Masukkan Nama : '))
        tgs = int(input('Masukkan Nilai Tugas : '))
        uts = int(input('Masukkan Nilai UTS : '))
        uas = int(input('Masukkan Nilai UAS : '))
        akr = float((uts * 0.35) + (uas * 0.35) + (tgs * 0.3))
        daftar [nim] = [nim, nama, tgs, uts, uas, akr]
        print ('\nData dengan NIM {0} telah berhasil dimasukkan kedalam Daftar Nilai'.format(nim))

    elif c.lower() == 'u':
        print("Ubah Daftar")
        nim = int(input('Masukkan NIM : '))
        if nim in daftar.keys():
            nama = str(input('Masukkan Nama : '))
            uts = int(input('Masukkan Nilai UTS : '))
            uas = int(input('Masukkan Nilai UAS : '))
            tgs = int(input('Masukkan Nilai Tugas : '))
            akr = float((uts * 0.35) + (uas * 0.35) + (tgs * 0.3))
            daftar [nim] = [nim, nama, tgs, uts, uas, akr]
            print('\nData dengan NIM  {0} telah berhasil diubah'.format(nim))
        else:
            print("\nNIM {0} yang anda input tidak ada atau salah".format(nim))

    elif c.lower() == 'h':
        print("Hapus Daftar")
        nim = int(input("Masukkan NIM: "))
        if nim in daftar.keys():
            del daftar[nim]
            print('\nData dengan NIM {0} telah berhasil dihapus dari Daftar Nilai'.format(nim))
        else:
            print("\nNIM {0} yang anda input tidak ada atau salah".format(nim))

    elif c.lower() == 'c':
        print("Cari Daftar")
        nim = int(input("Masukkan NIM: "))
        if nim in daftar.keys():
            print("NIM {0} adalah  \n"
                  "Nama         : {1}\n"
                  "Nilai Tugas  : {2}\n"
                  "Nilai UTS    : {3}\n"
                  "Nilai UAS    : {4}\n"
                  "Nilai Akhir  : {5:.2f}\n"
            .format(nim,
                    daftar[nim][1],
                    daftar[nim][2],
                    daftar[nim][3],
                    daftar[nim][4],
                    daftar[nim][5]))
        else:
            print("\nNIM {0} yang anda input tidak ada atau salah".format(nim))

    else:
        print("\nMenu yang anda pilih tidak tersedia, silahkan pilih menu yang tersedia")
