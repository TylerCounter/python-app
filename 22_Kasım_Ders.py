# def multiply(a, b) :
#     print(a * b)
# multiply(3, 5)


# def ilk_fonksiyonumuz(a,b) :
#     print(a**2 + b**2)
# ilk_fonksiyonumuz(2,3)  # here, the values (2 and 3) are allocated to the arguments
# a = 5
# b = 10
# ilk_fonksiyonumuz(2,3)


# def multiply(a, b) :
#     print(a * b)
# multiply(3, 5)
# multiply(-1, 2.5)
# multiply('amazing ', 3)  # it's really amazing, right?


# def motto() :     #### we can define a function without using any arguments.
#     print("Don't hesitate to reinvent yourself!")
# motto()  # it takes no argument


# def my_function(a, b) :
#     print(a*b)
# my_function(10, 20)


# def topla(a, b) :
#     print(a+b)
# topla(10, 20)


# def calculator(a,b,c):
#     if c == "+":
#         print(f"{a}+{b}={a + b}")
#     elif c == "-" :
#         print(f"{a}-{b}={a - b}")
#     elif c == "*" :
#         print(f"{a}*{b}={a * b}")
#     elif c == "//" :
#         print(f"{a}/{b}={a // b}")
#     else:
#         print("Düzgün birşey girermisin lütfen?")
# calculator(88,22,"*")



# def calculator(x,y,opr):
#     if opr == "+":
#         print(x+y)
#     elif opr == "-" :
#         print(x-y)
#     elif opr == "*" :
#         print(x*y)
#     elif opr == "/" :
#         print(x/y)
#     else:
#         print("Düzgün birşey girermisin lütfen?")
# calculator(88,22,"*")



# x = float(input("İlk Rakamı Giriniz : "))
# y = float(input("İkinci Rakamı Giriniz : "))
# opr = input("Yapılacak işlemi Giriniz : ")
# def calculator(x,y,opr):
#     if opr == "+":
#         print(x+y)
#     elif opr == "-" :
#         print(x-y)
#     elif opr == "*" :
#         print(x*y)
#     elif opr == "/" :
#         print(x/y)
#     else:
#         print("Düzgün birşey girermisin lütfen?")
# calculator(x,y,opr)



# def calculator():
#     a = int(input("a değerini giriniz: "))
#     b = int(input("b değerini giriniz: "))
#     c = input("hangi işlemi yapmak istiyorsunuz: ")
#     if c == "+":
#         print(f"{a}+{b}={a + b}")
#     elif c == "-" :
#         print(f"{a}-{b}={a - b}")
#     elif c == "*" :
#         print(f"{a}*{b}={a * b}")
#     elif c == "/" :
#         print(f"{a}/{b}={a / b}")
#     else:
#         print("lütfen bir işlem giriniz!")
# calculator()


# def multiply(a, b):
#     print(a*b)
# multiply(2,3)

# def carpma(a, b):
#     return a*b
# print(carpma(2, 3))   ### return değerini çağırmak için print kullanmak gerekli

# print(type(multiply(2,3)))   ## <class 'NoneType'>
# print(type(carpma(2,3)))   ## <class 'int'>


# x = float(input("İlk Rakamı Giriniz : "))
# y = float(input("İkinci Rakamı Giriniz : "))
# opr = input("Yapılacak işlemi Giriniz : ")
# def calculator(x,y,opr):
#     if opr == "+":
#         return x+y
#     elif opr == "-" :
#         return x-y
#     elif opr == "*" :
#         return x*y
#     elif opr == "/" :
#         return x/y
#     else:
#         print("Düzgün birşey girermisin lütfen?")  ## return "Düzgün bir değer giriniz."   diye de yazabiliriz
# print(calculator(x, y, opr))


# x = abs(float(input("İlk Rakamı Giriniz : ")))
# y = abs(float(input("İkinci Rakamı Giriniz : ")))
# opr = input("Yapılacak işlemi Giriniz : ")
# def calculator(x,y,opr):
#     if opr == "+":
#         return x+y
#     elif opr == "-" :
#         return x-y
#     elif opr == "*" :
#         return x*y
#     elif opr == "/" :
#         return x/y
#     else:
#         print("Düzgün birşey girermisin lütfen?")  ## return "Düzgün bir değer giriniz."   diye de yazabiliriz
# print(calculator(x, y, opr))


# def absolute_value(x):
#     if x < 0:
#         return -1 * x
#     if x >= 0:
#         return x

# print(absolute_value(3.3))
# print(absolute_value(-4))


# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(absolute_value(-5))


# k = []
# m =[]
# for i in range(4):
#     kelime = input("Lütfen bir kelime giriniz  : ")
#     k.append(len(kelime))
#     print(k)
#     m.append(kelime)
# print(f"{m[k.index(max(k))]} kelimesi daha uzun bir kelimedir : {max(k)}")


# def max_length():
#     l = []
#     k =[]
#     for i in range(4):
#         kelime = input("Lütfen bir kelime giriniz  : ")
#         l.append(len(kelime))
#         print(l)
#         k.append(kelime)
#         print(k)
#     return(f"{k[l.index(max(l))]} kelimesi daha uzun bir kelimedir : {max(l)}")   ## max(l) en uzun kelimenin uzunluk değeri olur
# print(max_length())                                                               ## l.index(?) en uzun değerin index numarası


# def uzunlugu_bul():
#     k = []
#     l = []
#     for i in range(4):
#         kelime = input("Lütfen 4 kelime giriniz  : ")
#         k.append(kelime)
#     print(k)
#     a = 0
#     for i in k:
#         if a < len(i):
#             l.append(i)
#             a = len(i)
#         # else:
#         #     continue
#     return f"{l[-1]} is the longest one."
# print(uzunlugu_bul())

###### APPEND   APPEND  APPEND  ######
# k = [1, 222222, 44, 4444444444]
# print(max(k))    ###  en uzun olan elemanın adını verir 4444444444
# k.append(len(k))
# print(k)

# fruits = ['apple', 'banana', 'cherry']
# fruits.append("orange")   ### APPEND ensona ekleme yapar
# print(fruits)

# a = ["apple", "banana", "cherry"]
# b = ["Ford", "BMW", "Volvo"]
# a.append(b)   ### ["Ford", "BMW", "Volvo"]  tek bir eleman olarak atandı
# print(a)    ### ['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']]
# print(len(a))  ### 4