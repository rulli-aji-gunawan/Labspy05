
daftar = {}
no = int(0)


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
        print ('='*garis)
        for i in daftar.items():
            print('| {0:2d} |  {1:7d}  |  {2:20s}  |  {3:5d}  |  {4:3d}  |  {5:3d}  |  {6:5.2f}  |'.format(i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], i[1][5], i[1][6]))
            # print (i)
        print('=' * garis)
    elif c.lower() == 't':
        print("Tambah Daftar")
        no += 1
        nim = int(input('Masukkan NIM : '))
        nama = str(input('Masukkan Nama : '))
        tgs = int(input('Masukkan Nilai Tugas : '))
        uts = int(input('Masukkan Nilai UTS : '))
        uas = int(input('Masukkan Nilai UAS : '))
        akr = float((uts * 0.35) + (uas * 0.35) + (tgs * 0.3))
        daftar [nim] = [no, nim, nama, tgs, uts, uas, akr]
    elif c.lower() == 'u':
        print("Ubah Daftar")
        nim = int(input('Masukkan NIM : '))
        if nim in daftar.keys():
            nama = str(input('Masukkan Nama : '))
            uts = int(input('Masukkan Nilai UTS : '))
            uas = int(input('Masukkan Nilai UAS : '))
            tgs = int(input('Masukkan Nilai Tugas : '))
            akr = float((uts * 0.35) + (uas * 0.35) + (tgs * 0.3))
            daftar [nim] = [no, nim, nama, tgs, uts, uas, akr]
        else:
            print("NIM {0} yang anda input tidak ada atau salah".format(nim))
    elif c.lower() == 'h':
        print("Hapus Daftar")
        nim = int(input("NIM: "))
        if nim in daftar.keys():
            del daftar[nim]
        else:
            print("NIM {0} yang anda input tidak ada atau salah".format(nim))
    elif c.lower() == 'c':
        print("Cari Daftar")
        nim = int(input("NIM: "))
        if nim in daftar.keys():
            print("NIM {0} adalah  \n"
                  "Nama         : {1}\n"
                  "Nilai Tugas  : {2}\n"
                  "Nilai UTS    : {3}\n"
                  "Nilai UAS    : {4}\n"
                  "Nilai Akhir  : {5}\n"
            .format(nim,
                    daftar[nim][2],
                    daftar[nim][3],
                    daftar[nim][4],
                    daftar[nim][5],
                    daftar[nim][6]))
        else:
            print("NIM {0} yang anda input tidak ada atau salah".format(nim))
    else:
        print("Pilih menu yang tersedia")
