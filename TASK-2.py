# Aslan - Instructor
 
#####  Task -1 #####
# Write a Python program to convert month name to a number of days:
# Expected Output:
# Input the name of Month: February                                       
# No. of days: 28/29 days
 
# month_name = input('Please, enter a month name : ')
# a_31days = ("january", "march", "may", "july", "august", "october", "december")
# print(type(a_31days))     ############ TUPLE #############
# b_30days = ("april", "june", "september", "november")
# c_28_29days = ("february")
# if month_name in a_31days:
#     print("No. of days : 31")
# elif month_name in b_30days:
#     print("No. of days : 30")
# else:
#     print("No. of days : 28/29")

# month_name = input('Please, enter a month name : ')
# a_31days = ["january", "march", "may", "july", "august", "october", "december"]
# print(type(a_31days))  ############ List #############
# b_30days = ["april", "june", "september", "november"]
# c_28_29days = ["february"]
# if month_name in a_31days:
#     print("No. of days : 31")
# elif month_name in b_30days:
#     print("No. of days : 30")
# else:
#     print("No. of days : 28/29")


#####  Task -2 #####
# Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
# December 21 - March 19 winter.
# March 20 - June 19 spring.
# June 20 - September 20 summer.
# September 21 - December 20 autumn.
# Expected Output:
# Input the month (e.g. January, February etc.): july                     
# Input the day: 31                                                       
# Season is autumn

# winter = ["December", "January", "February", "March"]
# spring = ["March", "April", "May", "June"]
# summer = ["June", "July", "August", "September"]
# autumn = ["September", "October", "November", "December"]
# month = input('Please, enter a month name : ')
# day = int(input('Please, enter the number of day : '))
# if month in winter:
#     if (month == "December" and day >= 21):
#         print("Season is winter")
#     elif (month == "March" and day <= 19):
#         print("Season is winter")
#     elif (month == "January" or "February"):
#         print("Season is winter")
# if month in spring:
#     if (month == "March" and day >= 20):
#         print("Season is spring")
#     elif (month == "June" and day <= 19):
#         print("Season is spring")
#     elif (month == "April" or "May"):
#         print("Season is spring")
# if month in summer:
#     if (month == "June" and day >= 20):
#         print("Season is summer")
#     elif (month == "September" and day <= 20):
#         print("Season is summer")
#     elif (month == "July" or "August"):
#         print("Season is summer")
# if month in autumn:
#     if (month == "September" and day >= 21):
#         print("Season is autumn")
#     elif (month == "December" and day <= 20):
#         print("Season is autumn")
#     elif (month == "October" or "November"):
#         print("Season is autumn")


##### TASK_2 ŞU ŞEKİLDE DE OLUR ######

# month = input("enter a month: ")
# day = input("enter a day: ")
# d = float(day)
# if (month == "december" and d >= 21) or month == "january" or month == "february" or ( month == "march" and d <= 19):
#     print("Season is Winter")
# elif (month == "march" and d >= 20) or month == "april" or "may" or (month == "june" and d <= 19):
#     print("Season is Spring")
# elif (month == "june" and d >= 20) or month == "july" or "august" or (month == "september" and d <= 20):
#     print("Season is Summer")
# elif (month == "September" and d >= 21) or month == "october" or "november" or (month == "December" and d <= 20):
#     print("Season is Autumn")
# else:
#     print("Please check your spelling and use lowercase")



#####  Task -3 #####
# Write a Python program to display astrological sign for given date of birth.
# Expected Output:
# Input birthday: 15                                                      
# Input month of birth (e.g. march, july etc): may                        
# Your Astrological sign is : Taurus

# day= int(input("Please input your birthday : "))
# month = input("Please input month of your birth : ")
# if (month == "January" and day >= 21):
#     print("Your Astrological sign is Aquarius")
# elif (month == "February" and day <= 19):
#     print("Your Astrological sign is Aquarius")
# if (month == "February" and day >= 20):
#     print("Your Astrological sign is Pisces")
# elif (month == "March" and day <= 20):
#     print("Your Astrological sign is Pisces")
# if (month == "March" and day >= 21):
#     print("Your Astrological sign is Aries")
# elif (month == "April" and day <= 20):
#     print("Your Astrological sign is Aries")
# if (month == "April" and day >= 21):
#     print("Your Astrological sign is Taurus")
# elif (month == "May" and day <= 21):
#     print("Your Astrological sign is Taurus")
# if (month == "May" and day >= 22):
#     print("Your Astrological sign is Gemini")
# elif (month == "June" and day <= 21):
#     print("Your Astrological sign is Gemini")
# if (month == "June" and day >= 22):
#     print("Your Astrological sign is Cancer")
# elif (month == "July" and day <= 22):
#     print("Your Astrological sign is Cancer")
# if (month == "July" and day >= 23):
#     print("Your Astrological sign is Leo")
# elif (month == "August" and day <= 22):
#     print("Your Astrological sign is Leo")
# if (month == "August" and day >= 23):
#     print("Your Astrological sign is Virgo")
# elif (month == "September" and day <= 22):
#     print("Your Astrological sign is Virgo")
# if (month == "September" and day >= 23):
#     print("Your Astrological sign is Libra")
# elif (month == "October" and day <= 22):
#     print("Your Astrological sign is Libra")
# if (month == "October" and day >= 23):
#     print("Your Astrological sign is Scorpio")
# elif (month == "November" and day <= 21):
#     print("Your Astrological sign is Scorpio")
# if (month == "November" and day >= 22):
#     print("Your Astrological sign is Sagittarius")
# elif (month == "December" and day <= 21):
#     print("Your Astrological sign is Sagittarius")
# if (month == "December" and day >= 22):
#     print("Your Astrological sign is Capricorn")
# elif (month == "January" and day <= 20):
#     print("Your Astrological sign is Capricorn")

##### TASK_3 ŞU ŞEKİLDE DE OLUR ######

# day = int(input("Input birthday: "))
# month = str(input("Input month of birth (e.g. march, july etc): "))
# if month == "january":
#     if day < 20:
#         print("Your Astrological sign is : capricorn")
#     else:
#         print("Your Astrological sign is : aquarius")
# if month == "february":
#     if day < 19:
#         print("Your Astrological sign is :aquarius")
#     else:
#         print("Your Astrological sign is :pisces")
# if month == "march":
#     if day < 21:
#         print("Your Astrological sign is :pisces")
#     else:
#         print("Your Astrological sign is :aries")
# if month == "april":
#     if day < 20:
#         print("Your Astrological sign is :aries")
#     else:
#         print("Your Astrological sign is :taurus")
# if month == "may":
#     if day < 21:
#         print("Your Astrological sign is :taurus")
#     else:
#         print("Your Astrological sign is :gemini")
# if month == "june":
#     if day < 21:
#         print("Your Astrological sign is :gemini")
#     else:
#         print("Your Astrological sign is :cancer")
# if month == "july":
#     if day < 23:
#         print("Your Astrological sign is :cancer")
#     else:
#         print("Your Astrological sign is :leo")
# if month == "august":
#     if day < 23:
#         print("Your Astrological sign is :leo")
#     else:
#         print("Your Astrological sign is :virgo")
# if month == "september":
#     if day < 23:
#         print("Your Astrological sign is :virgo")
#     else:
#         print("Your Astrological sign is :libra")
# if month == "october":
#     if day < 23:
#         print("Your Astrological sign is :libra")
#     else:
#         print("Your Astrological sign is :scorpio")
# if month == "november":
#     if day < 22:
#         print("Your Astrological sign is :scorpio")
#     else:
#         print("Your Astrological sign is :sagittarius")






#####  Task -4 #####
# Write a Python program to find the median of three values.
# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0

# a = float(input("Input first number: "))
# b = float(input("Input second number: "))
# c = float(input("Input third number: "))
# if a > b:
#     if a < c:
#         median = a
#     elif b > c:
#         median = b
#     else:
#         median = c
# else:
#     if a > c:
#         median = a
#     elif b < c:
#         median = b
#     else:
#         median = c

# print("The median is", median)



#####  Task -5 #####
# Write a Python program to check whether year is a leap year.
# The year can be evenly divided by 4, is a leap year, unless:
#     The year can be evenly divided by 100, it is NOT a leap year, unless:
#         The year is also evenly divisible by 400. Then it is a leap year.
# Input a year: 2004
# 2004 is a leap year.


# year = int(input("Input a year : "))
# if year % 4 == 0:
#     print(f"{year} is a leap year")
# elif year % 100 != 0:
#     print(f"{year} is not a leap year")
# elif year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year") 

# year = int(input("Input a year : "))
# if year % 4 == 0:
#     print(f"{year} is a leap year")
#     if year % 100 != 0:
#         print(f"{year} is no a leap year")
#     if year % 400 == 0:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year") 

# year = int(input("Input a year : "))
# if (year % 4 == 0 or year % 100 == 0 or year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year") 


