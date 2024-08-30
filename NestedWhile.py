# Nested While Loop
i = 1
while i <= 5:
    print("Hello", end=" ")
    j = 1
    while j <= 3:
        print("World", end=" ")
        j += 1
    i += 1
    print()
print("----------2--------------")
i = 0
while i <= 5:
    print("Hello", end=" ")
    j = -i
    while j <= 0:
        print("world", end=" ")
        j += 1
    i += 1
    print()
print("-----------3-------------")

i = 0
while i <= 5:
    print("Hello", end=" ")
    j = i
    while j <= 5:
        print("World", end=" ")
        j += 1
    i += 1
    print()
print("----------4--------------")
i = 0
while i <= 5:
    print("*", end="")
    j = -i
    while j <= -1:
        print("*", end="")
        j += 1
    i += 1
    print()
print("----------user--------------")
a = int(input("Enter The Number:"))
i = 1
while i <= a:
    print("*", end="")
    j = -i
    while j <= -2:
        print("*", end="")
        j += 1
    i += 1
    print()

