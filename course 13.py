data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# membuat backslash \ menjadi string
print("C:\\user\\ucup")

# tab
print("ucup \t\t otong, semakin jauh")

# backspace
print("ucup \botong")

# newline
print("baris pertama.\nbaris kedua.")
print("baris pertama.\rbaris kedua.")
print("baris pertama.\r\nbaris kedua.")

# 3. String literal atau raw

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan raw
print(r"""
Nama : Ucup
Kelas : 3 SD \ new normal
Website : www.ucup.com/newID
""")