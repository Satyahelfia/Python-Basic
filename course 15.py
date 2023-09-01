# Operasi dan Manipulasi String Part 2

## merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu GanTEng ParaHH"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan menggunakan isX method

#contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam + " is lower = " +str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool
print(salam + " is upper = " +str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n

# istitle() <-- semua kata dimulai dengan huruf besar
judul = "It\'s Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " +str(cek_judul))

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " +str(cek_judul))

## Cek komponen startswith() endswitch() <-- keren
cek_start = "Satya Agustianto".startswith("Satya")
print("start = " + str(cek_start))

cek_end = "Satya Agustianto".endswith("Agustianto")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
print(pisah)

gabungan = ','.join(pisah) 
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "aku sayang kamu"
print(gabungan.split(' '))

## alokasi karakter rjust(). ljust() center()

#rjust = rightjust atau rata kanan
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

#ljust = leftjust atau rata kiri
kiri = "kiri".ljust(10)
print("'"+kiri+"'")

#center = tengah
tengah = "tengah".center(10)
print("'"+tengah+"'")

#center = tengah
tengah = "tengah".center(10,"-")
print("'"+tengah+"'")

# kebalikannua -> strip()
tengah = tengah.strip("-") #menghilangkan tanda -
print("'"+tengah+"'")
