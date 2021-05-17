def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num

    return incrementer


c = counter()
print(c())

# Loop
i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Break from loop")
        break
pass
for i in (1, 2, 3, 15, 20):
    if i == 2 or i == 15:
        continue
    print(i)
    break

pass
while True:
    for i in range(1,20):
        if i == 2 or i == 15:
            continue
            print(i)
    break

# Return statement.
def break_loop():
    for i in range(1, 5):
        if (i == 2 or i == 4):
            return(i)
        print(i)
    return(5)


# Return function breaks all loops in a nested loop.
def break_all():
    for j in range(1, 5):
        for i in range(1, 4):
            if i*j == 6:
                return(i)
            print(i*j)
