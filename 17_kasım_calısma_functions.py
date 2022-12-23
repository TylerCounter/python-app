# def team_names(*teams) :
#     print('The teams in Premier League are :')
#     for i in teams :
#         print('-', i)
# team_names('Liverpool', 'M.United', 'M.City', 'Arsenal')


# def make_sentence(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for i in kwargs.values():
#         result += i
#     return result
# print(make_sentence(a="I ", b="love ", c="Clarusway!"))


# def team_league(team, league='Premier League'):
#     print(team, 'in', league)
# team_league('Liverpool')


# def my_function(first, last) : 
#     print('Your first name is :', first)
#     print('Your last name is :', last)
# my_function(first='Richard', last='Rice') 


# # def function_name(arguments) :
# #     execution body


# def first_function(argument_1, argument_2) :
#     print(argument_1**2 + argument_2**2)
# first_function(2, 3)  # here, the values (2 and 3) are allocated to the arguments


# def multiply(a, b) :
#     print(a * b)
# multiply(3, 5)
# multiply(-1, 2.5)
# multiply('amazing ', 3)  # it's really amazing, right?


# def my_function(a, b) :
#     print(a*b)
# my_function(10, 20)

# def motto() :     #### we can define a function without using any arguments.
#     print("Don't hesitate to reinvent yourself!")
# motto()  # it takes no argument

# def my_function_1():
#     print('My name is John')
# my_function_1()


# city = "I love London!"
# def my_function():
#     print(city)
# my_function()


# def my_function():
#     city = "I love London!"
#     print(city)
# my_function()


# def my_function():
#     print("I love London!")
# my_function()


# city = "I love Paris!"
# def my_function(): 
#     city = "I love London!"
#     print(city) 
# my_function()

# def outer():
#     x = "previous"
#     def inner():
#         nonlocal x
#         x = "later"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()


# def multiply_1(a, b) :
#     print(a * b)  # it prints something
# def multiply_2(a, b) :
#     return a * b  # returns any numeric data type value
# multiply_1(10, 5)
# print(multiply_2(10, 5))
# print(type(multiply_1(10, 2)))   ### <class 'NoneType'>
# print(type(multiply_2(10, 5)))   ###  <class 'int'>


# def my_function(a, b) :  
#     return a * b
# print(my_function(5, 7))


# def longer(a, b):
#     if len(a) >= len(b):
#         return a
#     else:
#         return b
# print(longer('Richard', 'John'))


# def my_function(a, b):
#     hypotenuse = (a**2 + b**2)**0.5
#     return hypotenuse

# def my_function(a, b) :
#     print(a*b)
# a = int(input('Enter first number : '))
# b = int(input('Enter second number : '))
# my_function(a, b)


# def my_function(a, b):
#     area = a * b
#     return area

# def my_function(a, b) :
#     print((a**2 + b**2)**0.5)
# a = int(input('Enter first side lenght : '))
# b = int(input('Enter second side lenght : '))
# my_function(a, b)


# import datetime
# def print_time() :
#     print('task completed')
#     print(datetime.datetime.now())     #### ALTTAKİNİN def ile yapılanı #####
#     print()
# first_name = 'Susan'
# print_time()
# for x in range(0,10):
#     print(x)
# print_time()


# import datetime
# first_name = 'Susan'
# print('task completed')
# print(datetime.datetime.now())     ##### ÜSTEKİNİN def olmadan yapılanı ####
# print()
# for x in range(0,10):
#     print(x)
# print('task completed')
# print(datetime.datetime.now())
# print()



# from datetime import datetime     ##### datetime'ı çağırdık 
# def print_time(task_name) :
#     print(task_name)
#     print(datetime.now())      #### 1 tane datetime yazmak yeterli
#     print()
# first_name = 'Susan'
# print_time('printed first name')
# for x in range(0,10):
#     print(x)
# print_time('completed for loop')


# from datetime import datetime
# first_name = 'Susan'
# print('first name assigned')      ##### ÜSTEKİNİN def olmadan yapılanı ####
# print(datetime.now())
# print()
# for x in range(0,10):
#     print(x)
# print()
# print(datetime.now())
# print('completed for loop')



# first_name = input('Enter your first name : ')
# first_name_initial = first_name[0:1]
# last_name = input('Enter your last name : ')
# last_name_initial = last_name[0:1]
# print('Your initials are : ' + first_name_initial + last_name_initial)


# def get_initial(name) :
#     initial = name[0:1]
#     return initial
# first_name = input('Enter your first name : ')
# first_name_initial = get_initial(first_name)
# last_name = input('Enter your last name : ')
# last_name_initial = get_initial(last_name)
# print('Your initials are : ' + first_name_initial + last_name_initial)


# def get_initial(name) :
#     initial = name[0:1].upper()
#     return initial
# first_name = input('Enter your first name : ')
# first_name_initial = get_initial(first_name)
# last_name = input('Enter your last name : ')
# last_name_initial = get_initial(last_name)
# print('Your initials are : ' + first_name_initial + last_name_initial)


# def get_initial(name) :
#     initial = name[0:1].upper()
#     return initial
# first_name = input('Enter your first name : ')
# last_name = input('Enter your last name : ')
# print('Your initials are : ' + get_initial(first_name) + get_initial(last_name))


# def get_initial(name) :
#     initial = name[0:1].upper()
#     return initial
# first_name = input('Enter your first name : ') 
# first_name_initial = get_initial(first_name)
# print('Your initial is : ' + get_initial(first_name))



# def get_initial(name, force_uppercase) :
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial
# first_name = input('Enter your first name : ') 
# first_name_initial = get_initial(first_name,False)
# print('Your initial is : ' + first_name_initial)


# def get_initial(name, force_uppercase=True) :
#     if force_uppercase:
#         initial = name[0:1].upper()
#     else:
#         initial = name[0:1]
#     return initial
# first_name = input('Enter your first name : ') 
# first_name_initial = get_initial(first_name)
# print('Your initial is : ' + first_name_initial)



# def my_function(*iterable):  # which animal species will be on this farm?
#     for variable in iterable:
#         if len(iterable)<=3:
#             print(variable)
#         else :
#             print("insufficient for more than three species")
#             break

# my_function('cows', 'horses', 'pigs')
# print()
# my_function('cows', 'horses', 'pigs', 'chickens')



# i = 5
# def f(arg=i):
#     print(arg)
# i = 6
# f()


# def f(a, L=[]):
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))
# print(f(3))


# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
# print(f(1))
# print(f(2))
# print(f(3))


# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
# combined_example(1, 2, 3)  # raises TypeError
# combined_example(1, 2, kwd_only=3)
# combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3)  # raises TypeError


# def standard_arg(arg):
#     print(arg)
# standard_arg(2)
# standard_arg(arg=2)


# def pos_only_arg(arg, /):
#     print(arg)
# pos_only_arg(1)  # works
# pos_only_arg(arg=1)  # raises TypeError


# def kwd_only_arg(*, arg):
#     print(arg)
# kwd_only_arg(3)  # raises TypeError
# kwd_only_arg(arg=3)  # works


# def foo(name, /, **kwds):
#     return 'name' in kwds
# foo(1, **{'name': 2})


# def my_function(*iterable):  # which animal species will be on this farm?
#     for variable in iterable:
#         if len(iterable)<=3:
#             print(variable)
#         else :
#             print("insufficient for more than three species")
#             break

# my_function('cows', 'horses', 'pigs')
# print()
# my_function('cows', 'horses', 'pigs', 'chickens')


# def modular_function(n):
#     return lambda x: x ** n

# power_of_3 = modular_function(3)
# print(power_of_3(5))


# print((lambda x: x**3)(5))


# mean = lambda x, y: (x+y)/2
# print(mean(8, 10))


# multiply = lambda x: x * 4
# add = lambda x, y: x + y
# print(add(multiply(10), 5))


# number_list = [1, 2, 3, 4]
# result = map(lambda x:x**3, number_list)
# print(list(result)) 


# number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
# divisible_list = filter(lambda x:x%3==0, number_list) 
# print(list(divisible_list))