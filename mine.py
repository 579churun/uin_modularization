nama = 'Churun Jauharoh A'
program = 'Gerak lurus'

print(f'program {program} oleh {nama}')

def hitung_usaha(gaya, perpindahan):
    usaha = gaya * perpindahan
    print(f'gaya = {gaya}Newton bekerja pada materi sejauh = {perpindahan}meter')
    print(f'sehingga usaha = {usaha} Nm')
    return usaha

# gaya = 10
# perpindahan = 27
usaha = hitung_usaha(10, 27)
usaha = hitung_usaha(5 * 10, 70)

