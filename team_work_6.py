
# def san(x):
#  print(x+1)
# x=-2
# x=4
# san(12)


# def foo(fname, val):
#  print(fname(val))
# foo(max, [1, 2, 3])
# foo(min, [1, 2, 3])


# count = 0
# my_string = "Clarusway"
# my_char = "a"
# for i in my_string:
#     if i == my_char:
#         count += 1
# print(count)


# num = 2013
# reversed_num = 0
# while num != 0:
#  digit = num % 10
#  reversed_num = reversed_num * 10 + digit
#  num //= 10
# print(reversed_num)


# f=lambda x:bool(x%2)
# print(f(20), f(21))

# import random
# print(random.randrange(0,91,5))



# while True:
#   try:
#    a=int(input("bi sayı :"))
#    print("doğru")
#   except():
#     print("lütfen integer gir")
#   else:
#     a=int(input("bi daha dene"))
#   finally:
#     print("final:tebrikler")
#     if a == 5:
#       break


# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)


# x=10
# y=8
# assert x>y, 'X too small'


# x=5
# y=8
# assert x>y, 'X too small'

# valid = False
# while not valid:
#     try:
#         n=int(input("Enter a number"))
#         while n%2==0:
#             print("Bye")
#         valid = True
#     except ValueError:
#         print("Invalid")


# def f(x, y, z): return x + y + z
# f(2, 30, 400)


# {a**2 for a in range(4)}  ###  {0, 1, 4, 9}



# import copy
# a=[10,23,56,[78]]
# b=copy.deepcopy(a)
# a[3][0]=95
# a[1]=34
# print(b)


# a=[1,2,3,4]
# b=[sum(a[0:x+1]) for x in range(0,len(a))]
# print(b)


# print('abcefd'.replace('cd', '12'))   #### abcefd
