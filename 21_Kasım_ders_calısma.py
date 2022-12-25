# word = "clarusway"
# count = 0
# for i in word:
#     count += 1
#     if count < len(word):
#         i = i + "-"
#     print(i, end="")


# word = input("Please enter a word : ")
# letter = 0
# for i in word:
#     letter +=1
#     if letter < len(word):
#         print(i, end="-")
#     else:
#         print(i)
        

# word = "Clarusway"
# a = 0
# for i in word:
#     a += 1
#     if a <= 8:
#         print(i, end="-")
#     else:
#         print(i)


# word = "clarusway"
# r = 0
# while r < len(word):
#     if r+1 < len(word):
#         x = word[r] + "-"
#     else:
#         x = word[r]
#     r+=1
#     print(x, end="")



# print ("Don't say I never make a mistake"

# print ("""Don't say I never make a mistake")

# pirnt ("Don't say I never make a mistake"

# x = i
# for i in range(14,X):
# print(i)

# if 1 >= 0 :
#     print("hi")
# print("hi")


# status = []  ## boş olduğu için
# if status:   ### False verir
#     print("''Hello universe")
# else   #### :    SyntaxError: expected ':'
#     print("Hello universe")


# x = ["1", "2", "3"]
# y = ["USA", "Japan", "Spain"]
# for i in y:
#     for j in X:
#         print(type([tuple(i+j)]))

# print("Here we go") 
# print("I will be the second text")
# a = "3"
# b = 5
# print("It's time for an error message :(")
# print(a+b)
# print("Sorry, but i won't be printed")

# for i in range("x"):   ## TypeError: 'str' object cannot be interpreted as an integer
#     print(i)

# print("2"+2)  ## TypeError: can only concatenate str (not "int") to str


# while True:
#     number1 = int(input("Enter a first number :"))
#     number2 = int(input("Enter a second number :"))  
#     division = number1 / number2   ### ZeroDivisionError: division by zero
#     print(f"The result is : {division}")
#     break

# while True:
#     number1 = int(input("Enter a first number :"))
#     number2 = int(input("Enter a second number :"))
#     try:
#         division = number1 / number2
#         print(f"The result is : {division}")
#         break
#     except:
#         print("Something went wrong... Try again!!!")



# while True:
#     number1 = int(input("Enter a first number :"))
#     number2 = int(input("Enter a second number :"))
#     try:
#         division = number1 / number2
#         print(f"The result is : {division}")
#         break
#     except ZeroDivisionError:      ##### Gelecek Hatayı Biliyorsak. Hatayı DOĞRU yazmalısın...
#         print("You can't divide by zero.")
#     except TypeError:
#         print("You can't divide by zero.")
#     except ValueError:      ##### Gelecek Hatayı Biliyorsak. Hatayı DOĞRU yazmalısın...
#         print("Acaba!!")

#     except:      ##### Gelecek Hatayı Biliyorsak. Hatayı DOĞRU yazmalısın...
#         print("Ben de anlamadım")

# try:
#     file = open("my_file.txt", "r")
#     print(file.read())
# except:
#         print('There is no file named "my_file.txt')  ## There is no file named "my_file.txt



# while True:
#     number1 = int(input("Enter a first number :"))
#     number2 = int(input("Enter a second number :"))
#     try:
#         division = number1 / number2
#     except ZeroDivisionError:
#         print("You can't divide by zero!!!")
#     else:
#         print(f"The result is : {division}")
#     finally:
#         print("It's done!")
#         break



# while True:
#     try:
#         number1 = int(input("Enter a first number :"))
#         number2 = int(input("Enter a second number :"))
#         division = number1 / number2
#     except ZeroDivisionError:
#         print("You can't divide by zero!!!")
#     except ValueError:
#         print("You need to write appropriate value")
#     else:
#         print(f"The result is : {division}")
#     finally:
#         print("It's done!")
#         break



# while True:
#     try:
#         number1 = int(input("Enter a first number :"))
#         number2 = int(input("Enter a second number :"))
#         division = number1 / number2
#     except Exception as k:
#         print("Something went wrong!!!")
#         print(f"Probably it is because of {k}")
#     else:
#         print(f"The result is : {division}")
#     finally:
#         print("It's done!")
#         break



# try:
#     x = 2 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except:
#     print("Something went wrong!!!")   ### önce başa bilindik except'leri yaz, en sona "except:" yani hata kodu boş olanı yaz.




# fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
# while True:
#     try:
#         x = int(input("Please enter a number to choose a fruit from the list :"))
#         print(f"Your favorite fruit is {fruits[x]}.")
#     except IndexError:
#         print("Please enter a valid number between 0-5(including0).")
#     except:
#         print("Unknown error, please report to the coding!") 
#     finally:
#         print("Thank you for trying our fruits!")
#         break


# fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
# while True:
#     try:
#         indeks = int(input("indeks numarasını giriniz :"))
#         yazdir = fruits[indeks]
#     except IndexError:
#         print("İndeks mevcut değil")
#     except ValueError:
#         print("Değeri yanlış girdiniz")
#     else:
#         print(f"My favorites fruit is {fruits[indeks]} ")
#     finally:
#         break



# count = 0
# while count < 5 :
#     print("Halil Pazarlama")
#     count += 1
# print("Osman Pazarlama")


# isim = "M.Osman"
# for i in isim:
#     print(i, end=" ")


# times = int(input("How many times should I say 'I love you'? : "))
# for i in range(times):
#     print('I love you!')


# times = int(input("How many times should I say 'I love you'?: "))

# for i in range(times):
#     print (f"{i+1} - I love you!")


# times = int(input("How many times should I say 'I love you'? : "))
# count = 0
# while count <= 1:
#     count += 1
#     print('I love you!')

# number = int(input("enter a number between 1 and 10: "))
# for i in range(11):
#     print("{}x{}=".format(number,i), number * i)  ## format   bu şekilde de yazılır    
#     print(f"{number}x{i}={number * i}")
#     i += 1

# sayi = int(input("enter a number between 1 and 10: "))
# for i in range(1,11):
# # for i in range(11):   ## bu da olur
#     print(f"{sayi} x {i} = {sayi * i}")

# i=1
# sayi=int(input("Bir ile on arasında bir sayı giriniz: "))
# while i<=10:
#     if 1<=sayi<=10:
#         print(f"{sayi} * {i}= {sayi * i}")
#         i=i+1
#     if sayi >10:
#         print("Yazdığınız sayıyı kontrol ediniz")
#         break


# i=1
# sayi=int(input("Bir ile on arasında bir sayı giriniz: "))
# while i<=10:
#     if 1<=sayi<=10:
#         print(f"{sayi} * {i}= {sayi * i}")
#         i=i+1
#     else:
#         print("Yazdığınız sayıyı kontrol ediniz")
#         break

# b = list(range(11))
# print(b)


# b = list(range(5, 11, 1))
# print(b)

# b = list(range(11, 5, -1))
# print(b)


# b = list(range(10))
# print(b)
# a = set(b)
# print(a)
# c = "Havva Nur"
# c P= set(c)
# print(c)


# print(range(5))
# print(*range(5))
# print(*range(5,22,2))

# print(*("seperate"))
# print(*(range(10,0,-2)))

# numbers = [0,1,2,3,4,5]
# text = ["zero", "one", "two", "three", "four", "five"]
# for x, y in zip(numbers,text):    #### zip komutu
#     print(x, ":", y)


# numbers = [0,1,2,3,4,5]
# text = ["zero", "one", "two", "three", "four"]
# for x, y in zip(numbers,text):    #### zip komutu  eşleştiği kada verdi
#     print(x, ":", y)

# numbers = list(range(10))
# print(numbers)
# tekler = (range(10,0,-2)
# ciftler = 

# cift = []
# tek = []
# for sayi in range(10):
#     if sayi % 2 == 0:
#         cift.append(sayi)
#     else:
#         tek.append(sayi)
# print(cift)
# print(tek)


# even_list = []
# odd_list = []

# for i in range(10):
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(f"evens: {even_list}")
# print(f"odds: {odd_list}")

# numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
# for i in numbers:
#     if i % 2 == 0:
#         print(f"{i}: evens")
#     else:
#         print(f"{i}: odd")



# numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
# even_list = []
# odd_list = []
# for i in numbers:
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(len(even_list))
# print(len(odd_list))
# print(f" The number of even numbers : {len(even_list)}")
# print(f" The number of even numbers : {len(odd_list)}")

# numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
# evens = 0
# odds = 0
# for i in numbers:
#     if i % 2 == 0:
#         evens += 1
#     else:
#         odds += 1
# print(f" The number of even numbers : {evens}")
# print(f" The number of even numbers : {odds}")


# for i in range(1, 10):
#     print(f"{i}" * i)

# num = range(10)
# for i in num:
#     print(f"{i}"* i)

# a = range(10)
# for i in a:
#     print(str(i) * i)

# for i in range(1, 10):
#     print(str(i) * i)

# toplam = 0
# for i in range(1,75):
#     toplam += i
# print(toplam)
# print(f" Output : {toplam}")


# who = ["I am", "You are"]
# mood = ["happy", "confident"]
# for i in who:
#     print(i)
#     for k in mood:
#         print(k)

# who = ["I am ", "You are "]
# mood = ["happy", "confident"]
# for i in who:
#     for k in mood:
#         print(i + k)


# names = ["susan", "tom", "edward"] 
# mood = ["happy", "sad"]
# for i in names:
#     for k in mood:
#         print(f"{i.capitalize()} is {k}")

# for i in range(1, 11):
#     for k in range(1, 11):
#         print(f"{i} * {k} = {i * k}")   #### çarpım tablosu ###
#     print(" ")

# for i in range(10): ######### piramit
#      print ((9-i) * f" " + (2*i-1)* f"{i}")

# for i in range(10): # piramit  yıldızlı
#     print ((9-i) * f" " + (2*i-1)* "*")

# for i in range(1, 7):
#     for k in range(i):
#         print("* ", end="")
#     print("") ### üçgen

# for i in range(1, 7):
#     for k in range(1, 7):
#         print("* ", end="")
#     print("") ### kare

# for i in range(7, 0, -1):
#     for k in range(i):
#         print("* ", end="")
#     print("") ### ters üçgen



# for i in range(1, 7):
#     for k in range(i):
#         print("* ", end="")
#     print("") ### 2 döngü beraber ters piramit

# for i in range(7, 0, -1):
#     for k in range(i):
#         print("* ", end="")
#     print("") ### 2 döngü beraber ters piramit



# for i in range(9,0,-1): # ters yıldızlı piramit
#     print ((9-i) * f" " + (2*i-1)* "*")

# for i in range(10): # yıldızlı piramit boşluklu
#     print ((9-i) * f" " + i* "* ")


# n = 5
# for i in range(n):
#     print(" " * (n - i - 1) + "* " * (i + 1))
# for k in range(n-1, 0, -1):
#     print(" " * (n - k) + "* " * k)



# for k in range(9,0,-1):                      ### range(9,1,-1)  0 yerine 1 yazarsan 1 tane 1 görünür piramitte (alt kısmında)
#     print ((10-k) * " " + (2*k-1)* f"{k}")   ### (2*k-1) için k=9 ise 17 adet 9 yazar  sonra k=8 ise 15 adet 8 yazar
#                                              ### (10-k) * " " k=9 ise baştan 1 boşluk  sonra k=8 baştan 2 boşluk bırakır
# for i in range(10): # piramit
#     print ((10-i) * " " + (2*i-1)* f"{i}")


# n = int(input("Enter a number : "))
# if n > 0:
#     for i in range(2, n):
#         print(i)
#         if n % i == 0:
#             print(f"{n} is not a prime number.")
#             break
#     else:
#         print(f"{n} is a prime number.")
# else:
#     print('Positive numbers only')



# n = int(input("How many steps do you want?: ")) # inputlu yıldızlı piramit boşluklu
# for i in range(n): 
#     print ((n-i) * f" " + (i+1)* "* ")



# user = {"name": "Daniel", "surname": "Smith", "age": 35}
# for i in user.values():
#     print(i, end=" ")

# user = {"name": "Daniel", "surname": "Smith", "age": 35}
# for i in user.values():
#     print(i)


# user = {"name": "Daniel", "surname": "Smith", "age": 35}
# for i, k in user.items():
#     print(i,":",k)



