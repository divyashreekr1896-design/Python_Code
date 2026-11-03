a=lambda x,y,z :print(x+y+z)
a(1,2,3)

# Program to find  the square and cube of every number

numbers = [2,4,5,1]

squares = list(map(lambda x: x ** 2, numbers))
cubes = list(map(lambda x: x ** 3, numbers))

print("print the Numbers:", numbers)
print("print the  Squares:", squares)
print("print the  Cubes:", cubes)

# Program to count even and odd numbers

numbers = [2,5,7,13,16]
numbers_2=[1,2,3,4,5]

even_num = list(filter(lambda x: x % 2 == 0, numbers))
odd_num = list(filter(lambda x: x % 2 != 0, numbers))
print("Even numbers:", even_num)
print("Odd numbers:", odd_num)

my_tuple=(3,2,1,5)
##x=list(my_tuple)
y=list(sorted(my_tuple,key=lambda z:z))
print(y)
print(tuple(y))

# Program to add two lists using map and lambda
outpt_value = list(map(lambda x, y: x + y, numbers, numbers_2))
print("adding two list using map and lambda", outpt_value )