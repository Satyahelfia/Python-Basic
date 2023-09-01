#Operasi Aritmatika

a = 10
b = 3

#operasi tambah +
print("----OPERASI PENJUMLAHAN DENGAN INPUTAN DARI USER---- ")
angka1 = int(input("masukkan a: "))
angka2 = int(input("masukkan b: "))
print("data pertama: ", angka1)
print("data kedua: ", angka2)
hasil = angka1 + angka2
print(angka1, '+' ,angka2, '=' ,hasil)


#operasi pengurangan -
print("----OPERASI PENGURANGAN---- ")
hasil = a - b
print(a, '-' ,b, '=' ,hasil)

#operasi perkalian *
print("----OPERASI PERKALIAN---- ")
hasil = a * b
print(a, '*' ,b, '=' ,hasil)

#operasi pembagian /
print("----OPERASI PEMBAGIAN---- ")
hasil = a / b
print(a, '/' ,b, '=' ,hasil)

#operasi eksponen (pangkat) **
print("----OPERASI EKSPONENSIAL---- ")
hasil = a ** b
print(a, '**' ,b, '=' ,hasil)

#operasi modulus (sisa pembagian) %
print("----OPERASI MODULUS---- ")
hasil = a % b
print(a, '%' ,b, '=' ,hasil)

#operasi floor division (kebalikan modulus) //
print("----OPERASI FLOOR DIVISION---- ")
hasil = a // b
print(a, '//' ,b, '=' ,hasil)

#prioritas operasi
print("----OPERASI PRIORITAS")
'''
1. ()
2. eksponen
3. perkalian dkk * / ** % //
4. penjumlahan dan pengurangan
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y & z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'&',z,'//',x)

hasil = x + y *z
print(x,'+',y,'*',z, '=',hasil)

hasil = (x + y) * z
print('(',x,'+',y,')*',z, '=',hasil)

