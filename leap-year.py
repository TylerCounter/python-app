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
# I've (Bugra) put the input inside a while loop and managed exceptions by putting the codes inside try/except. 
while True:
  try : 
    Year = int(input("Enter the Thomas number: "))  
    # Printing result  

    CheckLeap(Year) 

    break

  except : 
    print("The value you gave is not an integer. Please give me a valid value!")
    continue

# Celsius u Fahrenat'e çevirme.
a = int(input('celcius değer girin :'))  # Celsius u Fahrenat'e çevirme.
b = a*9/5+32

print(b)
print("Hello Cohort-12")
