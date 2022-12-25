######### Task - 1  ########
# # Write a Python program to display the first and last colors from the following list.
# # color_list = ["Red","Green","White" ,"Black"]

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0])     ### 0. index yani 1. sıradakini yazar     : Red
# print(color_list[3])     ### 3. index yani 4. sıradakini yazar     : Black
# print(color_list[0:])    ### baştan sona tümünü sırasıyla listeler : ['Red', 'Green', 'White', 'Black']
# print(color_list[0:3])   ### 0. index ile sonuncu index arasını (0.index dahil sonuncu yani 3. hariç) sırayla yazar : ['Red', 'Green', 'White']
# print(color_list[0::3])  ### 0. index'ten başlayarak  3'er atlayarak yazar : ['Red', 'Black']
# print(color_list[0:4:3]) ### 0. index ile 4. index(4.index yok zaten, amaç son indexi alması) arasında 3'er atlayarak alır

#######  Task - 2   ########
#  #Write a Python program to accept a filename from the user and print the extension of that.
# # Sample filename : abc.java
# # Output : java

# dosya_adi = input("Please enter a filename with its extension:")  ### Please enter a filename with its extension:hhhhhh.pyy
# print(type(dosya_adi))                ### <class 'str'>
# dosya_uzantisi = dosya_adi.split(".") ### .split(".") NOKTAYI referans ALARAK BÖLER VE nokta öncesi ile nokta sonrasını LİSTELER
# print(dosya_uzantisi)                 ### ['hhhhhh', 'pyy']
# print(type(dosya_uzantisi))           ### <class 'list'>
# print(dosya_uzantisi[1])              ### LİSTENİN BİRİNCİ KARAKTERİ UZANTISI OLUR  : pyy


# filename = input("Enter a filename: ")    ### Enter a filename: gggggg.pyy
# i = filename.index(".")   ### KAÇINCI KARAKTERDE AYIRDIĞINI GÖSTERİR integer değerdir.
# print(type(filename))  ## <class 'str'>
# print(i)  ## noktanın kaçıncı karakter olduğunu gösteren integer bir değer  : 6
# print(type(i))  ## <class 'int'> 
# print(filename[i+1:])  ## noktadan(yani filename[i]'den) sonrakileri (yani filename[i+1] ile başlayan) sonuna kadar listeler   :pyy

######  Task_3   ######
# # Write a Python program which accepts a sequence of comma-separated numbers 
# # from user and generate a list and a tuple with those numbers.
# # Sample data : 3, 5, 7, 23   Output :
# # List : ['3', ' 5', ' 7', ' 23']
# # Tuple : ('3', ' 5', ' 7', ' 23')

# numbers = input("Please enter four numbers and seperate them with comma :")
# print(numbers.split(','))
# my_liste = list(numbers.split(','))
# print(my_liste)
# my_tuple = tuple(numbers.split(','))
# print(my_tuple)

# numbers = input("Please enter four numbers and seperate them with comma :")
# my_liste = list(numbers.split(','))
# print(my_liste)
# my_tuple = tuple(my_liste)
# print(my_tuple)


######   Task - 4   ######
# # Write a Python program to print the following string in a specific format (see the output).
# # Sample String : "Twinkle, twinkle, little star, How I wonder what you are!
# # Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star,
# # How I wonder what you are" Output :
# # Twinkle, twinkle, little star,
# 	# How I wonder what you are! 
# 		# Up above the world so high,   		
# 		# Like a diamond in the sky. 
# # Twinkle, twinkle, little star, 
# 	# How I wonder what you are

# sample = "Twinkle, twinkle, little star,\n  How I wonder what you are! \n      Up above the world so high,\n      Like a diamond in the sky.\nTwinkle, twinkle, little star,\n  How I wonder what you are"
# print(sample)


# # Task - 5
# # Write a Python program which accepts the radius of a circle from the user and compute the area.
# # Sample Output : r = 1.1  Area = 3.8013271108436504

# yaricap = input("Please enter the radius of the circle : ")
# yaricap_1 = float(yaricap)
# alan = (3.14 * yaricap_1 ** 2)
# print('r =',yaricap_1)
# print('Alan :',alan)


# yaricap = float(input("Please enter the radius of the circle : "))
# alan = (3.14 * yaricap ** 2)
# print('r =',yaricap)
# print('Alan =',alan)