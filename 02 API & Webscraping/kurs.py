import requests
print('Selamat datang')
print('Pilih opsi: (1) USD=>IDR (2) IDR=>USD')
pilihan = input('Pilihan Anda (1/2): ')
nominal = int(input('Ketik nominal USD/RP: '))
kode = (input('Ketik pilihan Bank: ')).lower()

url = f'https://kurs.web.id/api/v1/{kode}'
data = requests.get(url)

if data.json()['error'] == 'false':
    hrg_jual = data.json()['jual']
    hrg_beli = data.json()['beli']
    waktu = data.json()['timestamp']
    hasil1 = nominal * int(hrg_jual)
    hasil2 = nominal / int(hrg_jual)

    if pilihan == '1':
        print(f'Hasil konversi USD {nominal} adalah Rp {hasil1}')
    elif pilihan == '2':
        print(f'Hasil konversi Rp {nominal} adalah USD {round(hasil2, 2)}')
    else:
        print('Anda salah ketik')
    print(f'Sekedar informasi nilai tukar 1 USD pada {waktu} yaitu: Rp {hrg_jual} (harga jual) atau Rp {hrg_beli} (harga beli)')
else:
    print('Maaf pilihan Bank tidak ada')



