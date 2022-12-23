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