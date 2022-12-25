# # Structure of the 'if' Statements

# if True:
#     print('it is true')

# if True:
#     print("This is true.")  ## This is true.

# if ["Ali"]:
#     print("This is true.")  ## This is true.

# if [0]:
#     print("This is true.")  ## This is true.

# if 0:
#     print("This is true.")  # birşey yazmaz


# empty_seat = 14
# if empty_seat > 3:  # in this case, 14>3=True, so the body will execute
#     print('there is still seat to sit')


# empty_seat = int(input('boş koltuk sayısı : '))
# yeni_yolcu_sayisi = int(input('Yeni yolcu sayısı : '))
# if empty_seat >= yeni_yolcu_sayisi:
#     print('There is still seat to sit.')
# else:
#     print('Yerimiz yoktur.')


# empty_seat = 14
# if empty_seat >15:  # in this case, 14>15=False, so the body will NOT execute
#     print('there is still seat to sit')


# x = 6
# y = 9
# print ("is x equal to y?                 :" , x == y)   ### is x equal to y?                 : False
# print ("is x not equal to y?             :" , x != y)   ### is x not equal to y?             : True
# print ("is x less than y?                :" , x < y)    ### is x less than y?                : True
# print ("is x greater than y?             :" , x > y)    ### is x greater than y?             : False
# print ("is x less than or equal to y?    :" , x <= y)   ### is x less than or equal to y?    : True
# print ("is x greater than or equal to y? :" , x >= y)   ### is x greater than or equal to y? : False


# a = set("TWELVE PLUS ONE")
# b = set("ELEVEN PLUS TWO")
# print(a)
# print(b)
# if a == b:
#     print("We are the same!")



# course = 'clarusway'
# if course == "clarusway":
#     print("you guaranteed the job")
# else:
#     print("think about it again")


# course = input("Select the course please, Clarusway or Other : ").capitalize()
# if course == 'Clarusway':
#     print(f"You guaranteed the job with {course.capitalize()}")
# else:
#     print("Think about it again!")


# weight = 80
# if weight > 100:
#     print("That's too heavy!")
# elif weight > 75:
#     print("I can lift that!")
# else:
#     print("That's too light!")


# number = 49
# if number >= 72:    
#     print("Number is smaller than or equal to 3") 
# else:  # Optional clause (you can only have one else)
#     print("Number is bigger than 3")


# number = 49
# if number >= 72:    
#     print(f"{number} is bigger than or equal to 72") 
# else:  # Optional clause (you can only have one else)
#     print(f"{number} is smaller than or equal to 72") 

##### GİRİLEN SAYI TEK Mİ ÇİFT Mİ #####
# number = float(input("Bir sayi giriniz :"))
# if number % 2 == 0:
#     print("sayı çift")
# else :
#     print("sayı tektir")

# number = int(input("Bir sayi giriniz :"))
# if number % 2 == 0:
#     print(f"{number} is even.")
# else :
#     print(f"{number} is odd.")


# number = int(input("Bir sayi giriniz :"))
# if number >= 0:
#     print(f"{number} is positive.")
# else :
#     print(f"{number} is negative.")


# number1 = int(input("Birinci sayıyı giriniz : "))
# number2 = int(input("İkinci sayıyı giriniz : "))
# if number1 > number2:
#     print(f"The large number is {number1}.")
# else :
#     print(f"The large number is {number2}.")



# #audience = "baby"
# audience = input("Enter audience type (baby \ kid \ teen \ adult) : ").lower()  ## .lower() ile küçük büyük hangi harfle input yapılırsa  değiştirecek
# if audience == "kid":
#     print("it is free to go to cinema")
# elif audience == "teen":
#     print("discounted price!")
# elif audience == "adult":
#     print("normal price")
# else:
#     print("No such audience, stay at your home!")

######   GİRİLEN 3 SAYININ EN BÜYÜK OLANINI BULMA  ######
# a = int(input('Birinci değeri giriniz : '))
# b = int(input('İkinci değeri giriniz : '))
# c = int(input('Üçüncü değeri giriniz : '))
# if a > b and a > c:
#     print(f"The largest number is {a}.")
# elif b > c and b > a:
#     print(f"The largest number is {b}.")
# elif c > a and c > b:
#     print(f"The largest number is {c}.")
# else:
#     print("get lost")


# number = int(input("Bir sayi giriniz :"))
# if number > 0:
#     print(f"{number} is positive.")
# elif number == 0:
#     print(f"{number} is neither negative nor positive.")
# else :
#     print(f"{number} is negative.")


# audience_group = 'kid', 'teen', 'adult'
# # audience_group = ['kid', 'teen', 'adult']  # bu şekilde de olur
# audience = input("Enter audience type : ")
# if audience in audience_group:
#     if audience == "kid":
#         print("it is free to go to cinema")
#     elif audience == "teen":
# 		print("discounted price!")
#     elif audience == "adult":
#         print("normal price")
# else:
#     print("No such audience, stay at your home!")


# score = int(input('Enter your score :'))
# if score >=90:
# 	if score >=95:
# 		Score_letter='A+'
# 	else:
# 		Score_letter='A'
# elif score >=80:
# 	if score >=85:
# 		Score_letter = 'B+'
# 	else:
# 		Score_letter = 'B'
# else:
# 	Score_letter = 'below B'
# print(f'Your degree: {Score_letter}')

