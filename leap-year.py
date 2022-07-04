# Default function to implement conditions to check leap year  
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  # sorgu yapıldı
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year Cooper");  

  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year Cooper")  
# Taking an input year from user  
Year = int(input("Enter the Thomas number: "))  
# Printing result  

CheckLeap(Year) 

# Celsius u Fahrenat'e çevirme.
a = int(input('celcius değer girin :'))  # Celsius u Fahrenat'e çevirme.
b = a*9/5+32

