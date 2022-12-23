######  While   ######
# while True:
#     print(1)  ##  sürekli 1 yazar, sonsuz döngüye girer

# a = 0
# while a < len("True"):   ## a değeri "True" ifadesinin karakter sayısından küçük olduğu kadar 1 yazacak
#     print(1)
#     a += 1


# number = 0
# while number < 6:
#     print(number)    ## her defasında number arttığı için 0'dan başlayarak 5'e (6'dan küçük) kadar ALT ALTA yazar
#     # number = number + 1
#     number +=1
# print("now, number is bigger or equal to 6")    ### printin YERİ ÇOK ÖNEMLİ while'ın ALT HİZASINDA ise DÖNGÜDEN ÇIKINCA yazacak


# number = 0
# while number <= 6:
#     print(number)
#     number +=1
# print("now, number is equal to 6")   


# my_list = ["a", "b", "c", "d", "e"]
# a = 0
# while a < len(my_list):
#     print(f"square of {a} is : {a**2}")
#     a +=1


# my_list = ["a", "b", "c", "d", "e", "r", "l"]
# a = 0
# while a < len(my_list):
#     print(f"square of {a} is : {a**2}")
#     a +=1


# my_list = ["a", ("b", "c"), "d", "e", "r", "l"]   ## ("b", "c") LİSTE içinde TEK BİR ELEMAN
# print(type(my_list))
# a = 0
# while a < len(my_list):
#     print(f"square of {a} is : {a**2}")
#     a +=1

# age = input("Please enter your age : ")
# while age.isdigit():             ###### isdigit  sayısal ise
#     print(f"Great you entered valid input: {age}")
#     break 


# age = input("Please enter your age : ")
# while age.isdigit():             ###### isdigit  sayısal ise
#     print(f"Great you entered valid input: {age}")
#     age = input("Please enter your age : ")
# print("You entered invalid input!!")

# age = input("Please enter your age : ")
# while not age.isdigit():
#     print("You entered incorrectly!")            ###### isdigit  sayısal ise
#     age = input("Enter your age : ")
# print(f"Great you entered valid input: {age}")
 


# cevap = 9
# soru = 'what number am i thinking of? :'
# print("Let's play the guessing game!!!")
# while True:
#     tahmin = int(input(soru))
#     if tahmin < cevap:
#         print("Little higher...")
#     elif tahmin > cevap:
#         print("Little lower")
#     else:
#         print("Are you MINDREADER!!")
#         break              #######break nerdeyse önemli   oradan çıkar  #####  else ile işlem yapar print eder ve çıkar.


##### GİRİLEN CÜMLEDEKİ EN UZUN KELİMEYİ BULMA  ######
# sentence = input("Give me a sentence : ")
# words = sentence.split()  ### split() ile girdiğimiz cümlenin kelimelerini boşluklarından ayıracak ve ayrı bir eleman olarak alacak
# counter = 0               ### split(" ") , split("-"), split(".") içine ne yazarsak ondan ayırır
# longest = 0
# print(words)
# while counter < len(words):
#     if len(words[counter]) > longest:
#         longest = len(words[counter])
#     counter += 1
# print(f"the lenght of the longest word : {longest}")   ### print'in nerede olduğu ÖNEMLİ ### while döngüsü tamamlanınca
                                                       ### yani counter = 3 olduğunda artık yazar


# word1 = len(input("First word: "))
# word2 = len(input("Second word: "))
# word3 = len(input("Third word: "))
# words = [word1, word2, word3]
# words.sort()   #### sort() kelimelerin uzunluklarını küçükten büyüğe sıralayacak
# print(words[-1]) ### -1 yani sonuncu kelimenin uzunluğunu verecek


######   For   #######
# liste = [1,2,3,4,5]
# for i in liste:
#     print(i)   ### LİSTE'deki elemanları tek tek sırasıyla ALT ALTA print eder.

# seasons = ['spring', 'summer', 'autumn', 'winter']
# for i in seasons:
#     print(i)  ### LİSTE'deki elemanları tek tek sırasıyla ALT ALTA print eder.


# seasons = ['spring', 'summer', 'autumn', 'winter']
# for mevsim in seasons:
#     print(mevsim)  ### LİSTE'deki elemanları tek tek sırasıyla ALT ALTA print eder.

# seasons = "aaasakajkşlmqşlmşlqlk"    ### harfleri alt alta yazar
# for i in seasons:
#     print(i)


# seasons = "aaasakajkşlmqşlmşlqlk",    ### TUPLE ve içinde tek eleman olduğu için  : aaasakajkşlmqşlmşlqlk
# seasons = ("aaasakajkşlmqşlmşlqlk", )  ### TUPLE ve içinde tek eleman olduğu için : aaasakajkşlmqşlmşlqlk
# for i in seasons:
#     print(i)


# seasons = ['spring', 'summer', 'autumn', 'winter']
# for i in seasons:
#     print(i)
#     print(len(i))  ### ALT ALTA yazacağı elemanların uzunluklarını yazar, alt alta 4 defa 6 yazar

# names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
# for i in names:
#     print(f"Hello, {i}!")  ### ALT ALTA Hello, Ahmed! gibi tüm isimler için yazdırır.

#####  APPEND  ####
# list = []    ## BOŞ bir LİSTE oluşturdum.
# print(list)  ##  Oluşturduğum BOŞ LİSTE'mi gör
# for i in range(1, 6):  ## 1-6 arası (1 ile başla 6'ya kadar, 6 hariç) değerler
#     list.append(i)  #### append ile oluşturduğum BOŞ LİSTEYE 1-6(6 hariç) arası i değerlerini atıyoruz [1, 2, 3, 4, 5]
# print(list)  


# word = "clarusway"
# for i in word:
#     # print(i, end="-")     #### end="-" yazarsam string olan ifadenin harflerini arasına - koyarak (en sona dahil) yan yana yazar  c-l-a-r-u-s-w-a-y-
#     # print(i, end="")      #### end=""  yazarsam tüm harfleri YAN YANA Boşluk BIRAKMADAN yazar.    clarusway
#     print(i)       #### end="-" yazmazsam string olan ifadenin harflerini alt alta teker teker yazar.


# word = "clarusway"
# count = 0
# for i in word:
#     count += 1
#     if count < len(word):
#         i = i + "-"
#     print(i, end="")    ####  if olmaz ise tüm harfleri YAN YANA Boşluk BIRAKMADAN yazar   c-l-a-r-u-s-w-a-y

# print()

# word = "clarusway"
# count = 1
# for i in word:
#     if count < len(word):
#         count += 1
#         i = i + "-"
#     print(i, end="")    #### tüm harfleri YAN YANA Boşluk BIRAKMADAN yazar  if olmaz ise

# course= "clarusway"
# for i in course:
#     if i==course[len(course)-1]:
#         print(i, end="")
#     else:
#         print(i, end="-")


# names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
# for name in names:
#     print(f"Hello {name}!")

# for i in range(1, 11):
#     print(f"{i}**2 = {i**2}")


# n = int(input('enter a number between 1-10'))
# for i in range(11):
#     print('{}x{} = '.format(n, i), n*i)
#     print(f"{n} x {i} = {n*i}")


#####  ÇARPIM TABLOSU  #####
# for i in range(1, 11):
#     print("\n")
#     for k in range(1, 11):
#         print(f"{i} x {k} = {i * k}")


#####  ZİP  #####
# text = ['one','two','three','four','five']
# numbers = [1, 2, 3, 4, 5]
# for x, y in zip(text, numbers):
#     print(x, ':', y)

# who = ['I am ', 'You are ']
# mood = ['happy', 'confident']
# for i in who:
#     for ii in mood:
#         print(i + ii)


# print(range(5))  # it will not print the numbers in sequence

# print(*range(5))  # '*' separates its elements

# print(*range(5,25,2))
# print(*('separate'))
# print(*range(10,0,-2))