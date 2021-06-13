from random import randint
a = randint(1, 30)
b = input('Enter your lucky number')
if a==b:
    print("Congratulations you Won!")
else:
    print("You loose!")


