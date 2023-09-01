# tipe data: angka satuan (integer)
data_integer = 71
print("data : ",data_integer, "bertipe : ", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 4.5
print("data : ",data_float, "bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "satya 15"
print("data : ",data_string, "bertipe : ", type(data_string))

#tipe data: biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("bertipe : ", type(data_bool))

## tipe data khusus
# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("bertipe : ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_float
data_c_double = c_double(19.5)
print("data : ", data_c_double)
print("bertipe : ", type(data_c_double))

# tipe data LIST
print("tipe data list")
print([1,2,3,4,5])
print(["satu","dua","tiga","empat"])

# tipe data Tuple
print("tipe data tuple")
print((1,2,3,4,5))
print(("satu","dua","tiga","empat"))




