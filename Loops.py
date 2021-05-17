# For loop.
for i in [0, 1, 3, 4]:
    print(i)

# Itering through lists.
list = ['a', 'b', 'c', 'd', 'e', 'f']
for j in list:
    print(j)
# Making an index to the iterated list.
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, ':', item)

# Applying lambda function on each element in list.
x = map(lambda e: e.upper(), ['one','two', 'three', 'four'])
print(x)

# Loops with an else clause.
for i in range(3):
    print(i)
else:
    print('done')
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')


a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
    else:
        print('no exception')

# The pass statement.
for x in range(10):
    pass
x = range(1, 5)
y = range(1, 5)
while x == y:
    pass
    break
a = 10
while True:
    a = a-1
    print(a)
    if a<7:
        break
    print('Done')


collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
for i1, i2, i3 in collection:
    print(i)

# While loop.
