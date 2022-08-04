# Artık Yıl Assignment

year=int(input("4 rakamlı 'artık' bir yıl giriniz :"))
leap=((year % 400 == 0) or (year % 100 != 0 and year % 4 == 0))
print (leap)

a = set('abracadabra')
print(a)



# .difference()
a = set('abracadabra')
b = set('alacazam')
print(a - b)  # same as '.difference()' method
print(a.difference(b)) # a difference from b

# .union()
a = set('abracadabra')
b = set('alacazam')
# c=a+b
# print(c)  bu şekilde kullanılamaz (set komutu + yada - işlemini desteklemedi)
# print(a+b) bu şekilde kullanılamaz
print(a | b)  # same as '.union()' method
print(a.union(b)) # unification of a with b

#   .intersection() methodu kesişimini bulur
a = set('abracadabra')
b = set('alacazam')
print(a & b)  # same as '.intersection()' method
print(a.intersection(b)) # intersection of a and b

#   .remove() methodu
a = set('abracadabra')
#  a.remove('a', 'b') # desteklemez, remove methodu içine yalnız bir adet değer girilir.
a.remove('a') # we delete 'c' from the set
print(a)

print(len(set('listen to the voice of enlisted')))

a=list("ugjkhgkgjkg")
a



Liste de en fazla tekrar eden sayıyı bulma

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
uniq_nbrs=list(set(numbers))
reference = 0
for i in range(len(uniq_nbrs)):
   repeat=numbers.count(uniq_nbrs[i])
   if repeat>reference:
       reference=repeat
       number = uniq_nbrs[i]
print("the most frequent number is {} and it was {} times repeated".format(number, reference))

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]


numbers.count(3)

max(numbers)

max(numbers, key=numbers.count)

numbers.count(max(numbers, key=numbers.count))

key parametresi kullanımı

# Aşağıda yazılı olan şehirlerin en uzun harfli olanınnı bulun
şehirler = ["izmir", "ankara", "yozgat", "van", "istanbul"]

sorted(şehirler) #fonksiyon

sorted(şehirler, key=len, reverse=True)



şehirler = ["izmir", "ankara", "yozgat", "van", "istanbul"]

şehirler.sort()  #method
şehirler

şehirler.sort(key=len)
şehirler

şehirler.sort(key=len, reverse=True)
şehirler

tarih verisini set() fonksiyonu ve manuel olarak oluşturma

tarih="21/05/2022"
set(tarih.split("/"))

date1=set("21/05/2022")
date2={"21/05/2022"}

date1

date2

usa=set("washington")
zeland=set("Wellington")


print(usa-zeland)
print(usa.difference(zeland))

#  birleşim  unification
print(usa|zeland)
print(usa.union(zeland))

# kesişim  intersection
print(usa&zeland)
print(usa.intersection(zeland))



if "False" or 0 and None :
  print("Hello universe")

if 0 or "False" and None :
  print("Hello universe")

print(0 or "False" and None)

print("False" or 0 and None)

# Not : Dosyalar Colab'da oluşturulmuştur.
