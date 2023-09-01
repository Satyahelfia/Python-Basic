#Program Casting
#merubah data dari satu tipe ke tipe lain
#tipe data: int, float, str, bool

print("-----MERUBAH TIPE DATA INTEGER-----")
data_int = 7
print("data: ", data_int, "type: ", type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) #akan false jika nilai int adalah 0

print("data= ", data_float, "type: ", type(float(data_int)))
print("data= ", data_str, "type: ", type(data_str))
print("data= ", data_bool, "type: ", type(data_bool))

print("-----MERUBAH TIPE DATA FLOAT-----")
data_float = 9.7
print("data: ", data_float, "type: ", type(data_float))

data_int   = int(data_float) #akan dibulatkan ke bawah
data_str   = str(data_float)
data_bool  = bool(data_float) #akan false jika nilai adalah 0
print("data= ", data_int, "type: ", type(int(data_float)))
print("data= ", data_str, "type: ", type(data_str))
print("data= ", data_bool, "type: ", type(data_bool))

print("-----MERUBAH TIPE DATA BOOLEAN FALSE-----")
data_bool = 0
print("data: ", data_bool, "type: ", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data= ", data_int, "type: ", type(data_int))
print("data= ", data_float, "type: ", type(data_float))
print("data= ", data_str, "type: ", type(data_str))

print("-----MERUBAH TIPE DATA BOOLEAN TRUE-----")
data_bool = True
print("data: ", data_bool, "type: ", type(data_bool))

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data= ", data_int, "type: ", type(data_int))
print("data= ", data_float, "type: ", type(data_float))
print("data= ", data_str, "type: ", type(data_str))

print("-----MERUBAH TIPE DATA STRING-----")
data_str = "10"
print("data: ", data_str, "type: ", type(data_str))

data_int : int(data_str) #string dalam bentuk kata tidak bisa diubah menjadi int
data_float : float(data_str)
data_bool : bool(data_str) #apabila string kosong, maka bool baru bernilai false
print("data : ", data_int, "type: ", type(data_int))
print("data: ", data_float, "type: ", type(data_float))
print("data: ", data_bool, "type: ", type(data_bool))



