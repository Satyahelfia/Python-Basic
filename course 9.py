#Loop
"""
Loop pada python terdiri dari : while, for, nested loop
"""

print("-----While loop-----")
angka = 0
while (angka < 9):
    print ("angka adalah : ", angka)
    angka = angka + 1
print("\n")

print("-----For loop-----")
for i in range(0, 10):
    print ("angka adalah : ", i)
print("\n")

print("-----For loop-----")
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
    print("saya suka makan: ", makanan)
print("\n")

print("-----Nested loop-----")
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
        if(j > i/j):
            print(i, "is prime")
            i = i + 1

