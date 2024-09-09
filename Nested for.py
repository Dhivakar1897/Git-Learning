# Nested for loop
# Checkerboard Pattern
n = int(input("Enter The Number:"))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
print()

# Square Pattern
n = int(input("Enter The Number:"))
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()
print()

# Right-Angled Triangle
n = int(input("Enter The Number:"))
for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()
print()

# Inverted Right-Angled Triangle
n = int(input("Enter The Number:"))
for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end='')
    print()

# Pyramid Pattern
n = int(input("Enter The Number:"))
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
print()

# Diamond Pattern
n = int(input("Enter The Number:"))
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '* ' * (i + 1))
print()
# Number Triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
print()

# Multiplication Table
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{i * j:2}', end=' ')
    print()
print()
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
'''
