from pprint import pprint
from tabulate import tabulate

#Dictionary data karyawan
data = [
        {
            'NIK': 100101,
            'Nama':'Muhammad Ghozi Aslam',
            'Umur': 25,
            'Pendidikan': 'S1',
            'Jabatan': 'Staff',
            'Divisi': 'HCGA',
            'Alamat': 'Cipinang Indah Blok A no 26',
            'Jenis Kelamin':'L',
            'Status':'Lajang',
            'Golongan':'1F'
        },
        {
            'NIK': 100102,
            'Nama':'Muhammad Alldi Athayasar',
            'Umur':24,
            'Pendidikan': 'S1',
            'Jabatan': 'Staff',
            'Divisi': 'HCGA',
            'Alamat': 'Duren Sawit Blok AB no 90',
            'Jenis Kelamin':'L',
            'Status':'Lajang',
            'Golongan':'1F'

        },
        {
            'NIK': 100103,
            'Nama':'Ruth Margareta',
            'Umur':23,
            'Pendidikan': 'S1',
            'Jabatan': 'Staff',
            'Divisi': 'Risk Management',
            'Alamat': 'Tebet dalam Blok PR no 19',
            'Jenis Kelamin':'P',
            'Status':'Lajang',
            'Golongan':'1F'
        }
    ]

def find_index(r):
    for i, d in enumerate(data):
        if int(d['NIK']) == int(r):
            return i

#function untuk membuat data baru
def create():
    print('\nSilahkan pilih menu.')
    menus = ['Tambah Data', 'Main Menu']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')
    option = input("Masukan menu pilihan : ")

    if (option == '1'):
        print('\nMasukan data karyawan.')
        forms = ['NIK', 'Nama', 'Umur', 'Pendidikan',
                    'Jabatan', 'Divisi', 'Alamat', 'Jenis Kelamin', 'Status','Golongan']
        temp = []

        for form in forms:
            answer = input(f"{form} : ")
            
            if form == 'NIK':
                index = find_index(answer)
                if index != None:
                        print("\nData sudah ada.")
                        create()

            temp.append(answer)

        new_data = {
            'NIK': temp[0],
            'Nama': temp[1],
            'Umur': temp[2],
            'Pendidikan': temp[3],
            'Jabatan': temp[4],
            'Divisi': temp[5],
            'Alamat': temp[6],
            'Jenis Kelamin': temp[7],
            'Status': temp[8],
            'Golongan':temp[9]
        }
        option = input("Simpan data? (Iya/Tidak): ")

        if option == 'Iya':
            data.append(new_data)
            print('\nData Berhasil disimpan.')
            create()
        else:
            create()
            
    else:
            main()

#function untuk melihat data karyawan
def tampilkan_data():
    menus = ['View All Data', 'View Data', 'Main Menu']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')
    option = input("Masukan Pilihan : ")
        
    if (option == '1'):
        if data == []:
            print("\nData masih kosong")
            tampilkan_data()
        else:
            print('\n')

            header = data[0].keys()
            rows =  [x.values() for x in data]
            print(tabulate(rows, header))

            print('\n')
            tampilkan_data()

    elif (option == '2'):
        NIK = int(input('\nMasukan Nik karyawan yang ingin dilihat : '))
        index = find_index(NIK)

        if index != None:
            print('\n')
            # print(f" {data[index]}")

            header = data[index].keys()
            rows =  [data[index].values()]
            print(tabulate(rows, header))

            print('\n')
            tampilkan_data()
        else:
            print("\nData doesn\'t exist.")
            tampilkan_data()
    else:
        main()


#function untuk perbaharui data
def update():
    menus = ['Perbaharui Data', 'Main Menu']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')
    option = input("Enter your choice here : ")

    if (option == '1'):
        NIK = input("\n Masukan NIK : ")
        index = find_index(NIK)
        if index == None:
            print("\nData tidak ditemukan.")
            update()
        else:
            print('\n')
            option = input("Lanjutkan perbaharui? (Iya/Tidak) : ")

            if (option == 'Iya'):
                print('\nSilahkan pilih data yang ingin diperbaharui.')
                menus = ['NIK', 'Nama', 'Umur', 'Pendidikan',
                            'Jabatan', 'Divisi', 'Alamat', 'Jenis Kelamin', 'Status','Golongan']
                for i, menu in enumerate(menus, start=1):
                    print(f'{i} : {menu}')
                option = int(input("Masukan pilihan : "))-1

                new_data = input(f'\nMasukan data {menus[option]} yang diperbaharui : ')
                proceed = input("Apakah yakin perbaharui data? (Iya/Tidak): ")
                if proceed == 'Iya':
                    print(menus[option])
                    data[index][menus[option]] = new_data

                    print('\nData berhasil diperbaharui!')
                    update()
                else:
                    update()
            else:
                update()
    else:
        main()


#function untuk menghapus data karyawan
def hapus_data_by_nik():
    menus = ['Delete Data', 'Main Menu']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')
    option=input("Silahkan pilih menu:  ")
    if (option == '1'):
        NIK = input("\nMasukan NIK : ")
        index = find_index(NIK)
        if index == None:
            print("\nData tidak ada.")
            hapus_data_by_nik()
        else:
            print('\n')
            header = data[index].keys()
            rows =  [data[index].values()]
            print(tabulate(rows, header))
            print('\n')
            option = input("Lanjutkan menghapus? (Iya/Tidak) : ")

            if (option == 'Iya'):
                del data[index]
                print('\nData Berhasil dihapus!')
                hapus_data_by_nik()
            else:
                hapus_data_by_nik()
    else:
        main()

def main():
        menus = ['Tambah data baru','Lihat data',
                'Perbaharui data', 'Hapus data', 'Keluar']
        for i, menu in enumerate(menus, start=1):
            print(f'{i} : {menu}')

        option = input("Silahkan pilih menu : ")

        if (option == '1'):
            create()
        elif (option == '2'):
            tampilkan_data()
        elif (option == '3'):
            update()
        elif (option == '4'):
            hapus_data_by_nik()
        elif (option == '5'):
            print('\nSelamat tinggal, semoga harimu menyenangkan')
        elif (option == ''):
            print('\nPilihan tidak dapat kosong')
            main()
        else:
            print('\nMenu yang dipilih tidak ada')
            main()


if __name__ == '__main__':
        print('====Selamat datang di Menu data karyawan===\n')
        main()
