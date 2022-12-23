# programming_languages = ["JavaScript", "Python", "Java", "C++"]
# print(programming_languages)
# print(type(programming_languages))
# programming_languages.remove("JavaScript")
# print(programming_languages)


# my_list = [0, 10, 20, 30, 40, 50]
# print(my_list.pop(0))  ### belirli bir indexteki değeri sil ve silinen değeri göster 0
# print(my_list)  ###  0 silinince geriye kalanları listeler 10,20,30,40,50
# print(my_list.pop(3)) ### belirli bir indexteki değeri sil ve silinen değeri göster 40
# print(my_list)  ###  40 silinince geriye kalanları listeler 10,20,30,50
# print(my_list.pop(-2))  ### belirli bir indexteki değeri sil ve silinen değeri göster 30
# print(my_list)  ###  30 silinince geriye kalanları listeler 10,20,50
# print(my_list.pop())  ### boş bırakırsan son değeri siler  50
# print(my_list)  ### 50 silinince kalanları yazar 10,20


# l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
# l.remove('Alice')  ### remove ile değeri belirli olanı silersin 
# print(l)    ### ['Bob', 'Charlie', 'Bob', 'Dave']
# l.remove('Bob')  ### aynı değerden birden fazla varsa ilkini siler
# print(l)  ### ['Charlie', 'Bob', 'Dave']


# l = [0, 10, 20, 30, 40, 50]
# del l[0]  ### index numarası belirtilerek istenilen silinir
# print(l)  ### [10, 20, 30, 40, 50]

# del l[-1]
# print(l)  ### [10, 20, 30, 40]


# l = [0, 10, 20, 30, 40, 50]
# del l[2:5]  ## birden fazla eleman aynı anda 2. dahil-aradakiler dahil-5.hariç (20,30,40) siler
# print(l)   # [0, 10, 50]


# l = [0, 10, 20, 30, 40, 50]
# del l[:3]  ## 3.'ye kadar 3 hariç (40,50) siler 
# print(l)  # [30, 40, 50]


# l = [0, 10, 20, 30, 40, 50]
# del l[-2:]  ## -2.'den başlar, -2.(40) dahil sonuna kadar (40,50) siler
# print(l)  ## [0, 10, 20, 30]


# l = [0, 10, 20, 30, 40, 50]
# del l[:]  ## hepsini siler
# print(l)  # []


# l = [0, 10, 20, 30, 40, 50]
# del l[::2]  ## baştan başlayarak 2'şer atlayarak (0,20,40) siler
# print(l)  # [10, 30, 50]


# college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
# print(list(enumerate(college_years, 2019)))

# grocery = ['bread', 'milk', 'butter']
# print(type(grocery))
# numaralandırma = enumerate(grocery)  ## liste içini numaralandırıyor virgül ve rakam yazmazsan 0'dan başlıyor
# print(type(numaralandırma))
# print(list(numaralandırma))  # converting to list
# numaralandırma = enumerate(grocery, 10) # changing the default counter
# print(list(numaralandırma))


# fruits = ['apple', 'banana', 'cherry']
# fruits.append("orange")   ## sonuna ekleme yapar
# print(fruits)   ## ['apple', 'banana', 'cherry', 'orange']


# a = ["apple", "banana", "cherry"]
# b = ["Ford", "BMW", "Volvo"]
# a.append(b)
# print(a)


# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4, 8]
# prices = [1.50, 2.25, 0.89]
# i = 0
# output = []
# for fruit in fruits:   ### fruit dersin k dersin  m dersin ...
#     temp_qty = quantities[i]
#     temp_price = prices[i]
#     output.append((fruit, temp_qty, temp_price))
#     i += 1
# print(output)


# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4, 8]
# prices = [1.50, 2.25, 0.89]
# groceries = zip(fruits, quantities, prices)
# print(list(groceries))

# a=[1,2,3,4]
# b=[sum(a[0:4])]
# print(b)
# b=[sum(a[0:3])]
# print(b)
# b=[sum(a[0:2])]
# print(b)
# b=[sum(a[0:1])]
# print(b)

# a=[1,2,3,4]
# b=[sum(a[0:x+1]) for x in range(0,len(a))]
# print(b)


# number_1 = [2, 3, 5]  # create a list
# number_2 = [1, 4]   # create another list
# number_2.extend(number_1)  # add all elements of number_1 to number_2
# print('List after extend():', number_2)  # Output: List after extend(): [1, 4, 2, 3, 5]



# L1 = []
# L1.append([1, [2, 3], 4])
# print(L1)  ## [[1, [2, 3], 4]]
# L1.extend([7, 8, 9])
# print(L1)  ## [[1, [2, 3], 4], 7, 8, 9]
# print(L1[0][1][1] + L1[2])  ## 3 + 8 = 11



# animals = ['cat', 'dog', 'rabbit', 'horse']
# index_number = animals.index('dog')  ### get the index of 'dog' , index numarasını veriyor
# print(index_number)  # Output: 1


# T = (1, 2, 3, 4, 5, 6, 7, 8)
# # print(T.index(5), end = " ")   ## 4
# # print(T[4], end = " ")  ## 5
# print(T[T.index(5)], end = " ")   ## 5
# print(T[T[T[6]-3]-6])  ## 0

# D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}   ####  ??????????
# print(type(D))  ## dict
# D['1'] = 2  ## '1' : 1  artık  '1' : 2 oldu
# print(D)    ## {1: 1, 2: '2', '1': 2, '2': 3}
# print(D[1])  ## output : 1
# print(D[str(D[1])])  ## output : 2 , yani str olan '1' eşiti 2 değeri
# print(D[D[str(D[1])]])
# print(D[D[D[str(D[1])]]])

# set1 = {1, 2, 3}
# set2 = set1.copy()
# set2.add(4)
# print(set1)
