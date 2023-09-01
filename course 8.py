#pengondisian 
print("-----KONDISI IF-----")
angka = int(input("masukkan nilai : "))
if(angka > 7):
    print("anda lulus")

print("\n")

print("-----KONDISI IF ELSE-----")
angka = int(input("masukkan nilai : "))
if(angka > 7):
    print("anda lulus")
else:
    print("anda tidak lulus")

print("\n")

print("-----KONDISI ELIF-----")
angka = int(input("masukkan nilai : "))
if(angka > 7 and angka < 10):
    print("anda lulus")
elif(angka < 7 and angka >= 1):
    print("anda tidak lulus")
elif(angka > 10):
    print("nilai yang anda input salah")
    
