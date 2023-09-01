#Operator Bitwise

a = 9
b = 5

#bitwise or (|)
c = a | b
print ('\n ======OR======')
print ('nilai : ',a, ',binary : ',format(a, '08b'))
print ('nilai : ',b, ',binary : ',format(b, '08b'))
print ('---------------------------------(|)')
print ('nilai : ',c, ',binary : ',format(c, '08b'))

#bitwise and (&)
c = a & b
print ('\n ======AND======')
print ('nilai : ',a, ',binary : ',format(a, '08b'))
print ('nilai : ',b, ',binary : ',format(b, '08b'))
print ('---------------------------------(&)')
print ('nilai : ',c, ',binary : ',format(c, '08b'))

#bitwise xor (^)
c = a ^ b
print ('\n ======XOR======')
print ('nilai : ',a, ',binary : ',format(a, '08b'))
print ('nilai : ',b, ',binary : ',format(b, '08b'))
print ('---------------------------------(^)')
print ('nilai : ',c, ',binary : ',format(c, '08b'))

#bitwise not (~)
c = ~ a
print ('\n ======NOT======')
print ('nilai : ',a, ',binary : ',format(a, '08b'))
print ('---------------------------------(~)')
print ('nilai : ',c, ',binary : ',format(c, '08b'))

