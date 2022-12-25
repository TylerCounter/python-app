# empty_dict_1 = {}
# print(type(empty_dict_1))

# empty_dict_2 = dict()
# print(type(empty_dict_2))

# mountain = tuple('Alps')
# print(mountain) 

# my_list = [1, 4, 3, 4, 5, 6, 7, 4]
# my_tuple = tuple(my_list)
# print(type(my_tuple), my_tuple)

# my_tuple = ("wakabayashi",) # sonunda VİRGÜL olmasa tuple olmazdı
# print(my_tuple, type(my_tuple), sep="\n") 
# my_tuple2 = "wakabayashi"
# print(my_tuple2, type(my_tuple2), sep="\n") # BİR ÜSTTEKİNİN AYNISI
# my_tuple2 = tuple("wakabayashi")
# print(my_tuple2, type(my_tuple2), sep="\n") 
# print(my_tuple)
# print(my_tuple2)


# my_tuple = (1, 2, 3, 4, 564, 863)
# print(my_tuple[3:5])
# print(my_tuple[0])
# my_tuple[5] = 5
# print(my_tuple) # tuple'a ekleme çıkartma yapılamaz

# sehirler = ["Istanbul", "Izmir", "Ankara", "Van", "Erzurum", "Sivas", "Gonya", "Ssinop", "Mugla", "Gaziantep"]
# print(sehirler)
# print(type(sehirler))
# sehirler_tuple = tuple(sehirler)
# print(type(sehirler_tuple))
# sehirler[9] = "Yozgat"  ## Listeye ekleme yapılabilir
# print(sehirler)

# # sehirler_tuple[0] = "Yozgat" # # OLMAZ ÇÜNKÜ TUPLE
# sehirler[9] = 2
# print(sehirler)

# # DICTIONARIES
# grocer1 = {'fruit':'apple', 'drink':'water'}
# grocer2 = dict(fruit='apple', drink='water')
# print(grocer1)
# print(grocer2)


# state_capitals = {'Arkansas': 'Little Rock', 
#                   'Colorado': 'Denver', 
#                   'California': 'Sacramento', 
#                   'Georgia': 'Atlanta'}
# print(state_capitals['Colorado'])       # accessing method
# state_capitals['Virginia'] = 'Richmond'   # adding a new item
# print(state_capitals)


# # keys and values can be of different types.
# mix_values = {'animal': ('dog', 'cat'),        # tuple type
#               'planet': ['Neptun', 'Saturn', 'Jupiter'],      # list type
#               'number': 40,          # int type
#               'pi': 3.14,         # float type
#               'is_good': True}        # bool type


# mix_keys = {22 : "integer",
#             1.2 : "float",
#             True : "boolean",
#             "key" : "string"}
# print(mix_keys.values())
# print(mix_keys)

# my_dictionary = dict(animal='dog', planet='neptun', number=40, pi=3.14, is_good=True) # bu şekilde e dict oluşturulabilir.
# print(my_dictionary)

# my_dictionary = {'animal': 'dog',
#                 'planet': 'neptun',
#                 'number': 40,
#                 'pi': 3.14,
#                 'is_good': True}
# print(my_dictionary.items(), '\n')  ## sadece item'leri  listeler dict_items([('animal', 'dog'), ('planet', 'neptun'), ('number', 40), ('pi', 3.14), ('is_good', True)])
# print(my_dictionary.keys(), '\n')   ## sadece keys'leri listeler dict_keys(['animal', 'planet', 'number', 'pi', 'is_good'])
# print(my_dictionary.values())       ## sadece values'leri listeler dict_values(['dog', 'neptun', 40, 3.14, True]


# my_dictionary = {'animal': 'dog',
#                  'planet': 'neptun',
#                  'number': 40,
#                  'pi': 3.14,
#                  'is_good': False}
# my_dictionary['is_bad'] = 'False' # ADDING a new item  ## 2 türlü ekleme yapılabilir
# print(my_dictionary)

# my_dictionary.update({'is_bad': True}) # ADDING a new item  ## 2 türlü ekleme yapılabilir ## UPDATE
# print(my_dictionary)

# del my_dictionary['is_good'] # silmek için key adını yazacağız  ## SİLME  ## DEL
# print(my_dictionary)


# my_dictionary = {'planet': 'neptun',
#                'number': 40,
#                'pi': 3.14,
#                'is_good': True,
#                'is_bad': False}

# print('pi' in my_dictionary) 
# print('animal' not in my_dictionary)  # DİCT'İMİZ İÇİNDE KEY VAR / YOK, we have deleted 'animal' animal listede artık yok.

# # Let's Practice : Write a code to print Clark's age. ##dict içinden VALUE okumak için KEY kullanmak
# student_ages = {"Harry": 29,
#                 "Clark": 32,
#                 "Peter": 22,
#                 "Bruce": 36}
# print(student_ages['Clark'])


# Nested Dictionaries   ### İç içe geçmiş dict'ler
# school_records = {
#     "personal_info":
#         {"kid":{"tom": {"class": "intermediate", "age": 10},
#                 "sue": {"class": "elementary", "age": 8}},
#          "teen":{"joseph":{"class": "college", "age": 19},
#                  "marry":{"class": "high school", "age": 16}},},
        
#     "grades_info":
#         {"kid":{"tom": {"math": 88, "speech": 69},
#                 "sue": {"math": 90, "speech": 81}},
#          "teen":{"joseph":{"coding": 80, "math": 89},
#                  "marry":{"coding": 70, "math": 96}},},}

# print(school_records['personal_info']['teen']['marry']['age']) # We can use square brackets to access internal dicts
# print(school_records["grades_info"]["kid"]["sue"]["speech"])

# family = {
#     "erkek" : {
#                "baba" : {"yas" :40, "meslek" :"eyt emeklisi"},
#                "kardes" : {"yas" :22, "meslek" :"ogrenci"}
#     },
#     "kadin" : {
#                "anne" : {"yas" :40, "meslek" :"emekli albay"},
#                "abla" : {"yas" :27, "meslek" :"influencer"}}
# }
# print(family["kadin"]["anne"]["meslek"])

# # How can we access and print Lisa’s age? Write the syntax???
# customers = { 
# 'bank': 
# {1: {'name': 'James', 'age': '27', 'sex': 'Male'}, 
#  2: {'name': 'Nicole', 'age': '25', 'sex': 'Female'},  
#  3: {'name': 'Andy', 'age': '38', 'sex': 'Male'}, 
#  4: {'name': 'Alex', 'age': '19', 'sex': 'Male'}, 
#  5: {'name': 'Linda', 'age': '33', 'sex': 'Female'}, 
# },
# 'insurance':
# {1: {'name': 'Jashua', 'age': '33', 'sex': 'Male'}, 
#  2: {'name': 'Marry', 'age': '66', 'sex': 'Female'},  
#  3: {'name': 'Adam', 'age': '56', 'sex': 'Male'}, 
#  4: {'name': 'Samuel', 'age': '54', 'sex': 'Male'}, 
#  5: {'name': 'Lisa', 'age': '22', 'sex': 'Female'},
# },
# }
# print(customers["insurance"][5]["age"])


# # LİST   ## SET

# s = set('unselfishness')
# print(s) # As you can see, the letters of the string type data are only written once in the set.
# #           ##Within this scope, using sets can help you avoid repetitions. Tekrar edenleri 1 defa yazar. 
# print(type(s))
# set_1 = {'red', 'blue', 'pink', 'red'}  ## set
# print(type(set_1))
# colors = 'red', 'blue', 'pink', 'red'   ## tuple
# print(type(colors))
# set_2 = set(colors)
# print(set_1)  ## {'red', 'blue', 'pink'}
# print(set_2)  ## {'blue', 'red', 'pink'}


# flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
# print(type(flower_list))
# flowerset = set(flower_list)
# flowerlist = list(flowerset) ## LİST -> SET    VEYA    SET -> LİST DÖNÜŞÜMÜ YAPILABİLİR
# print(flowerset) 
# print(flowerlist)


# # add() : Adds a new item to the set.
# # remove() : Allows us to delete an item.
# # intersection() : Returns the intersection of two sets.
# # union() : Returns the unification of two sets.
# # difference() : Gets the difference of two sets.

# a = set('abracadabra')
# print(a) 

# a = set("Angara")
# b = set("Istanbul")
# print(a, b, sep= "\n")

# a = set('abracadabra')
# b = set('alacazam')
# print(a - b)            ##### same as '.difference()' method
# print(a.difference(b))  ##### a difference from b


# a = set("Angara")
# b = set("Istanbul")
# c = set("Izmir")
# print(a - b)           ### same as '.difference()' method
# print(a.difference(b)) ### a difference from b
# print(b.difference(a))
# print(b.difference(a, c))

# print(a | b)          ### same as '.union()' method
# print(a.union(b))     ### unification of a with b

# print(a & b)             ### same as '.intersection()' method
# print(a.intersection(b)) ### intersection of a and b



# a = set('abracadabra')
# a.remove('c')          ### we delete 'c' from the set
# print(a)

# a = set('abraadabra')
# print(a)
# a.add('c') # we add 'c' again into the set
# print(a)

# #  Additionally, you can:
# # Get the number of set’s elements using len() function,
# # Check if an element belongs to a specific set(in / not in operators), you get the boolean value.

# print(set('listen to the voice of enlisted'))
# print(len(set('listen to the voice of enlisted')))


# numbers = {}              ### Boş bir dict oluşturduk
# print(type(numbers))      ### <class 'dict'>
# numbers['x'] = 12         ### Boş olan numbers dict içine eleman atama
# numbers['y'] = 4          ### Boş olan numbers dict içine eleman atama
# numbers.update({'z': 3})  ### Boş olan numbers dict içine eleman atama
# print(numbers)            ### {'x': 12, 'y': 4, 'z': 3}
# print(numbers['x'] + numbers['y'] + numbers['z']**2)  ### 25

############  INSERT  ############
# numbers_10 = [10, 30, 40, 50, 60, 70, 80, 90, 100]  ### Liste oluştur numbers_10
# print(numbers_10)        ### [10, 30, 40, 50, 60, 70, 80, 90, 100]
# print(type(numbers_10))  ### <class 'list'>
# numbers_10.insert(1,20)  ### istediğimiz sıraya istediğimizi ekleriz  INSERT
# print(numbers_10)        ### [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# fruits_vegetables = ["fruit", "vegetable", ["apple", "banana", ["mango", "avocado"]], ["spinach", "broccoli"]]
# print(fruits_vegetables[3][0])   ### spinach

# family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']
# print(type(family_members))     ### ['Meghan', 'Tom', 'Nicole', 'Tim']
# print(type(family_members))     ### <class 'list'>
# # family_members = ('Meghan', 'Tom', 'Nicole', 'Tim')
# # print(type(family_members))   ### <class 'tuple'>
# print(family_members)           ### ('Meghan', 'Tom', 'Nicole', 'Tim')

