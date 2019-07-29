# mixed tests of py basics 



a, b = 0, 1


while b < 1000:
    print(b, end=' ', flush = True)
    a, b = b, a + b
      

print() # line ending

# test functions
def fun(n): 
    print(n) 

fun(47)


# bitwise 

x = 0x0a
y = 0x02
z= x & y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
