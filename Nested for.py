# Nested for loop
'''
for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")
print("-------------")
for i in range(5):
    for j in range(97,102,1):
        print(chr(j),end="")
    print("")
print("-------user----------")
a=int(input("Enter The Number:"))
for i in range(a+1):
    for j in range(i):
        print("*",end="")
    print()
print("-------user----------")
a=int(input("Enter The Number:"))
for i in range(a,0,-1):
    for j in range(i):
        print("*",end="")
    print()

# 1Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
print()
# 2Multiplication Table
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{i * j:2}', end=' ')
    print()
print()
'''
n=int(input("Enter The Number:"))
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
# 3Checkerboard Pattern
n = 8
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
print()

# 4Square Pattern
n=int(input("Enter The Number:"))
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()
print()

# 5Right-Angled Triangle
n = 5
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()
print()

# 6Inverted Right-Angled Triangle
n=int(input("Enter The Number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end='')
    print()

# 7Pyramid Pattern
n=int(input("Enter The Number:"))
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
print()

# 8Diamond Pattern
n=int(input("Enter The Number:"))
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
'''
