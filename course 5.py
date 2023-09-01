#Program input data dari user menggunakan casting

#data yang dimasukkan pasti string
data = input("Masukkan data: ")
print("data: ", data )
print("type: ", type(data))

#jika ingin mengambil data integer dari user
angka = int(input("masukkan angka: "))
print("data: ", angka )
print("type: ", type(angka))

#jika ingin mengambil data boolean
#harus casting data menjadi integer terlebih dahulu
bool = bool(int(input("masukkan nilai boolean:")))
print("data: ", bool)
print("type: ", type(bool))