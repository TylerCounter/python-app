# queue = ['John', 'Amy', 'Bob', 'Adam']
# item = input("Please enter an item : ")
# queue.append(item)
# print(queue)

# letters = ["a", "b", "c"]
# letters += ["d"]
# print(len(letters))

# x ="abc"
# x *= 2
# print(len(x))


# print("{0}{1}{0}".format("abra", "cad"))

# x = "never give up"
# words = x.split(" ")
# print(words)
# res = words[1]
# print(res)

# x = "Hello ME"
# print(x.replace("ME", "world")) 


# print("This is a sentence.".upper())
# print("AN ALL CAPS SENTENCE".lower())


# msg = input("gir : ")
# msg = msg.replace("#"," ")
# print(msg)

# txt = "hello"
# print(max(txt))


# f = open("demofile.txt", "r")
# print(f.read())      ### demofile.txt dosyasının olduğu klasörde çalıştırmalısın

# f = open("demofile.txt", "r")
# print(f.read(5))

# f = open("demofile.txt", "r")
# print(f.readline())
# print(f.readline())  ## By calling readline() two times, you can read the two first lines:

# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()  ## It is a good practice to always close the file when you are done with it.


### To write to an existing file, you must add a parameter to the open() function:
# f = open("demofile2.txt", "a")  ## "a" - Append - will append to the end of the file
# f.write("Now the file has more content!")  ## "w" - Write - will overwrite any existing content
# f.close()
# f = open("demofile2.txt", "r")  ## open and read the file after the appending:
# print(f.read())
### f = open("myfile.txt", "x")  ##" x" - Create - will create a file, returns an error if the file exist

## Remove the file "demofile.txt":
# import os
# os.remove("demofile.txt")


# import os   ### Check if file exists, then delete it:
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")


# import os  ## To delete an entire folder, use the os.rmdir() method:
# os.rmdir("denemew3")

# import os    ## Check if file exists, then delete it:
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")



# N = int(input("Enter a number : "))
# sum = 0
# for i in range(1,N+1):
#     sum += i
# print(sum)
# print(f" Output : {sum}")


# def printMax(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
# printMax(3, 4)



# x = 50
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# func(x)
# print('x is now', x)
# ############
# x = 50
# def func(x):
#     print('x is', x)
# x = 2
# print('Changed local x to', x)
# func(x)
# print('x is now', x)

# ############
# def func(x):
#     x = 50
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# func(x)
# print('x is now', x)


# def function1(var1=5, var2=7):
#     var2=9
#     var1=3
#     print (var1, " ", var2)
# function1(10,12)






# Myvar = 2
# print(Myvar)

# map()
# round()
# diff()
# repr()

### nested if ile büyükten küçüğe sıralama
# if x > y and x > z:
#     if y > z:
#         print(x, y. z, sep=", ")
#     else:
#         print(x, z, y, sep=", ")
# elif y > x and y > z:
#     if x > z:
#         print(y, x, z, sep=", ")
#     else:
#         print(y, z, x, sep=", ")

# elif z > y and z > x:
#     if y > x:
#         print(z, y, x, sep=", ")
#     else:
#         print(z, x, y, sep=", ")
# else:
#     print("x, y, z eşittir")
###########


# aList = [5, 10, 15, 25]
# # print(aList[0])
# # print(aList[-1])
# # print(aList[-2])
# print(aList[::2])
# print(aList[::-2])

# print(format("Welcome", "10s"), end = '#')  ## welcome kelimesinden başlar 10. karakterden sonra '#' yazar
# print(format(111, "4d"), end = '#')  ## integer olunca başından saymaya başladı '#' yazdı 1 karakter boş ve 3 karakterlik 111'i yazdı
# print(format(924.656, "3.2f"))     ## tam sayı kısmından 3 basamak float kısmından 2 basamak alır ama yuvarlar alır 924.66 alır


# print(repr(10))
# print(repr(10.5))
# print(repr(True))
# print(repr(4+2))

# print("xyyzxyzxzxyy".count('xyy', 2, 11))  ## 2.'den başlayarak 11.basamağa kadar xyy sayacak
# print('abcdefcdgh'.split('cd'))
# listOne = ['a', 'b', 'c', 'd']
# listTwo = ['e', 'f', 'g']
# listOne.extend(listTwo)  ## ikinci listeyi birinciye ekledi
# print(listOne)


# example = "snow world"
# print("%s" % example[4:7])  ## boşluğu almadan yazar   wo  çıkar


# print(chr(ord('b')+1))   ## karakteri verir

# print("xyyzxyzxzxyy".endswith("xyy", 0, 2))  ## Cevap False  eğer 3 yazsak True olurdu

# times = int(input("How many times should I say 'I love you' : "))
# for i in range(times):
#     print('I love you')


# n = int(input('enter a number between 1-10 : '))
# for i in range(11):
#     print('{}x{} = '.format(n, i), n*i)


# n = int(input('enter a number between 1-10 : '))
# for i in range(11):
#     print(f"{n, i} x {n*i}")

# print(set(range(5)))
# print(range(5))  # it will not print the numbers in sequence
# print(*range(5))  # '*' separates its elements

# text = ['one','two','three','four','five']
# numbers = [1, 2, 3, 4, 5]
# for x, y in zip(text, numbers):     ## zip() function make an iterator that aggregates elements from each of the iterables.
#     print(x, ':', y)

# who = ['I am ', 'You are ']
# mood = ['happy', 'confident']
# for i in who:
#     for ii in mood:
#         print(i + ii)


# a = 3
# while a**2 < 199:
#     print(a**2)
#     print('I will stop smoking')
#     a += 3


# ps4_price = 400
# saved_amount = int(input('Please enter your saved amount: '))
# if saved_amount <= ps4_price/2:
#     print('You must save more, keep saving!')
# elif saved_amount > ps4_price/2 and saved_amount < ps4_price:
#     print('You saved more than half, keep saving!')
# else:
#     print('Yippee! You can buy your PS4')


# math_mark = int(input('Please enter the mark: '))
# if math_mark >= 85:
#     print('A (Excellent)')
# elif math_mark < 85 and math_mark >= 70:
#     print('B (Good)')
# elif math_mark < 70 and math_mark >= 60:
#     print('C (Medium)')
# elif math_mark < 60 and math_mark >= 45:
#     print('D (Not Bad)')
# else:
#     print('F (Failed)')

# number = int(input('Please enter a number: '))
# count = 0
# while count < number:
#     print(count**2)
#     count += 1


# sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

# for i in sample_list:
#    print ("The type of", i, "is", type(i))

# a=[1,2,3,4]
# b=[sum(a[0:x+1]) for x in range(0,len(a))]
# print(b)


# L1 = []
# L1.append([1, [2, 3], 4])
# L1.extend([7, 8, 9])
# print(L1[0][1][1] + L1[2])


# T = (1, 2, 3, 4, 5, 6, 7, 8)
# print(T[T.index(5)], end = " ")
# print(T[T[T[6]-3]-6])

# D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}
# D['1'] = 2
# print(D[D[D[str(D[1])]]])


# set1 = {1, 2, 3}
# set2 = set1.copy()
# set2.add(4)
# print(set1)


# def function_name(arguments) :
#     execution body

# def first_function(argument_1, argument_2) :
#     print(argument_1**2 + argument_2**2)


# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")


# x = 200
# print(isinstance(x, int))

# print(bool(0))


# if 5 != 10:
#   print("5 and 10 is not equal")


# fruits = ["apple", "banana", "cherry"]
# "apple" = 'kiwi'
# print(fruits)


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.get("model"))


# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car["year"] = 2020
# print(car.get("year"))

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car["color"] = "red"
# print(car.get("color"))


# i = 1
# while i < 6:
#     print(i)
#     i += 1


# i = 1
# while i < 6:
#   if i == 3:
#     break    ## Stop the loop if i is 3.
# i += 1


# i = 0
# while i < 6:  
#   i += 1
#   if i == 3:
#     continue   ## ## In the loop, when i is 3, jump directly to the next iteration.
#   print(i)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:    #### Print a message once the condition is false.
#   print("i is no longer less than 6")


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue     ### In the loop, when the item value is "banana", jump directly to the next item.
#   print(x)


#   fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break   ### Exit the loop when x is "banana".
#   print(x)


# def my_function():   ####  Create a function named my_function.
#   print("Hello from a function")


# def my_function():
#   print("Hello from a function")
# my_function()    ### Execute a function named my_function.


# def my_function(fname, lname):
#   print(fname)   ## Inside a function with two parameters, print the first parameter.


# def my_function(x):  
# return x + 5  ## Let the function return the x parameter + 5.


# def my_function(*kids):  ## If you do not know the number of arguments that will be passed into your function, 
                          ### there is a prefix you can add in the function definition, which prefix?
#   print("The youngest child is " + kids[2])


# def my_function(**kid):  ## If you do not know the number of keyword arguments that will be passed into your function,
#                         ### there is a prefix you can add in the function definition, which prefix?
#   print("His last name is " + kid["lname"])


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)   ## ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


### The remove() method removes the specified item.
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

#### The pop() method removes the specified index.
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)


### If you do not specify the index, the pop() method removes the last item.
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)


### The del keyword also removes the specified index:
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)


## The del keyword can also delete the list completely.
# thislist = ["apple", "banana", "cherry"]
# del thislist

## The clear() method empties the list.The list still remains, but it has no content.
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

#### Print all items by referring to their index number:
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

### Print all items, using a while loop to go through all the index numbers
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

## A short hand for loop that will print all items in a list:
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)
###With list comprehension you can do all that with only one line of code:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)




















