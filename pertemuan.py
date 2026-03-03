list1 = [1,2,3]
list2 = [2.1, 2.2, 2.3]
list3 = ['a', 'b', 'c']
listgabungan = [list1, list2, list3]
print(list1)
print(list2)
print(list3)
print(listgabungan)

list_tipe_data = [100, 3.78, 'Caca Marica', True]
a=[list_tipe_data[0], list_tipe_data[2]]
print(a)

warna = ['merah', 'hijau', 'kuning', 'biru', 'pink', 'ungu']
warna2 = warna.copy()

print("list setelah di copy")
print(warna2)
del warna2[4]
print("list setelah di edit")
print(warna2)
print("list asli")
print(warna)