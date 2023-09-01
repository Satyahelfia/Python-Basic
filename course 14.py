# Operasi dan Manipulasi String Part 1

# 1. Menyambung string (concatenate)
nama_pertama = "Monkey"
nama_tengah = "D"
nama_akhir = "Luffy"
nama_lengkap = nama_pertama +" "+nama_tengah +" "+ nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print('panjang string :', str(panjang))

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string
D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing
print("index ke-0 dari : " + nama_lengkap + " adalah " + nama_lengkap[0])
print("index ke-(-1) dari : " + nama_lengkap + " adalah " + nama_lengkap[-1])
print("index ke-(0,3) dari : " + nama_lengkap + " adalah " + nama_lengkap[0:3]) # artinya indeks ke 0 sampai 3
print("index ke-(0,2,4,6,8,10) dari : " + nama_lengkap + " adalah " + nama_lengkap[0:10:2]) # artinya indeks ke 0 sampai 10 dengan selisih 2 

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap))

# 4. operator dalam bentuk method
data = " roronoa zoro"
jumlah = data.count("o")
print("jumlah huruf o pada " + data + " adalah sebanyak : " + str(jumlah))