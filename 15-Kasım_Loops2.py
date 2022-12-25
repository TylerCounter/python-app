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
#         print(f"{sayi} * {i} = {sayi * i}")
#         i=i+1
#     if sayi >10:
#         print("Yazdığınız sayıyı kontrol ediniz")
#         break


# i=1
# sayi=int(input("Bir ile on arasında bir sayı giriniz: "))
# while i<=10:
#     if 1<=sayi<=10:
#         print(f"{sayi} * {i} = {sayi * i}")
#         i=i+1
#     else:
#         print("Yazdığınız sayıyı kontrol ediniz")
#         break


# b = list(range(11))
# print(b)

# b = list(range(5, 11, 2))
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
# c = set(c)
# print(c)


# print(range(5))
# print(*range(5))
# print(*range(5,22,2))

# print(*("seperate"))
# print(*(range(10,0,-2)))

#####  ZİP  #####
# numbers = [0,1,2,3,4,5]
# text = ["zero", "one", "two", "three", "four", "five"]
# for x, y in zip(numbers,text):    #### zip komutu
#     print(x, ":", y)


# numbers = [0,1,2,3,4,5]
# text = ["zero", "one", "two", "three", "four"]
# for x, y in zip(numbers,text):    #### zip komutu  eşleştiği kadaR verdi
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


# numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10) ### üstekinin aynısı
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

# num = range(10)  ## üstekinin aynısı
# for i in num:
#     print(f"{i}"* i)

# a = range(10) ## üstekinin aynısı
# for i in a:
#     print(str(i) * i)

# for i in range(1, 10):  ## üstekinin aynısı
#     print(str(i) * i)

### 1'den n' e kadar sayıların toplamı (n hariç)
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

#### çarpım tablosu ###
# for i in range(1, 11):
#     for k in range(1, 11):
#         print(f"{i} x {k} = {i * k}")   
#     print()


######### piramit üst kısmı  ########
# for i in range(10): 
#      print ((9-i) * f" " + (2*i-1)* f"{i}")

#### piramit  YILDIZLI  #####
# for i in range(10): # piramit  yıldızlı
#     print ((9-i) * f" " + (2*i-1)* "*")
#############  alttaki ve üstteki beraber çalışırsa EŞKENAR DÖRTGEN  ########
# ##### piramit YILDIZLI TERSİNE  #####
# for i in range(9,0,-1): 
#     print ((9-i) * f" " + (2*i-1)* "*")

#### sağa açılan dik üçgen ######
# for i in range(1, 7):
#     for k in range(i):
#         print("* ", end="")
#     print("")

#### sağdan sola daralan tersine dik üçgen ######
# for i in range(7, 0, -1):
#     for k in range(i):
#         print("* ", end="")
#     print("")

##### kare  #####
# for i in range(1, 7):
#     for k in range(1, 7):
#         print("* ", end="")
#     print("") 



# for k in range(9,0,-1):                      ### range(9,1,-1)  0 yerine 1 yazarsan 1 tane 1 görünür piramitte (alt kısmında)
#     print ((10-k) * " " + (2*k-1)* f"{k}")   ### (2*k-1) için k=9 ise 17 adet 9 yazar  sonra k=8 ise 15 adet 8 yazar
#                                              ### (10-k) * " " k=9 ise baştan 1 boşluk  sonra k=8 baştan 2 boşluk bırakır
# for i in range(10): # piramit
#     print ((10-i) * " " + (2*i-1)* f"{i}")


##### Girilen Sayı Asal Sayı mı?  ######
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

##### inputlu yıldızlı piramit boşluklu  #####
# n = int(input("How many steps do you want?: ")) 
# for i in range(n): 
#     print ((n-i) * f" " + (i+1)* "* ")


# user = {"name": "Daniel", "surname": "Smith", "age": 35}
# for i in user.values():
#     print(i, end=" ")  ## YAN YANA BOŞLUK BIRAKIP YAZAR

# user = {"name": "Daniel", "surname": "Smith", "age": 35}
# for i in user.values():
#     print(i)    ## ALT ALTA YAZAR


# user = {"name": "Daniel", "surname": "Smith", "age": 35}
# for i, k in user.items():
#     print(i,":",k)