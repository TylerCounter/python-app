# print(set('pqr'))  ## {'p', 'r', 'q'}
# print(type(set('pqr')))
# for x in set('pqr'):
#     print(x*2)


# d = {}
# d = {“john”:40, “peter”:45}
# d = {40 : "john", 45 : "peter"}
# print(d)
# print(type(d))


# d = {"john":40, "peter":45}
# print(d["john"])


# d = {"john":40, "peter":45}
# print(list(d.keys()))


# a={}
# a['a']=1
# a['b']=[2,3,4]
# print(a)   ## {'a': 1, 'b': [2, 3, 4]}


# z=set('abc')
# print(z)  ## {'c', 'a', 'b'}
# z.add('san')   ### add ile 'san' set'in tek bir elemanı olarak atandı  add komutu ile tek bir argüman eklenebilir
# print(z)
# z.update(set(['p', 'q']))  ## update ile  'p' ve 'q' ayrı birer eleman olarak atandı
# print(z)  ## {'a', 'c', 'p', 'san', 'b', 'q'}


# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)  ## ('apple', 'banana', 'cherry')
# print(type(thistuple))  ## <class 'tuple'>


# my_tuple = (2, 'apple', 3.5)
# count, fruit, price = (2, 'apple', 3.5)
# print(count)
# print(my_tuple)


# r, g, *other = (192, 210, 100, 0.5)
###  192  assigns 192 to r
###  210  2assigns 10 to g
### [100, 0.5]  packs the remaining elements 100 and 0.5 into a list and assigns it to the other variable.


# odd_numbers = (1, 3, 5)
# even_numbers = (2, 4, 6)
# numbers = (*odd_numbers, *even_numbers)
# print(numbers)   ### (1, 3, 5, 2, 4, 6)
# print(type(numbers))  ## <class 'tuple'>




### .pop() method      =>  remove items from a list
## example
# my_list = [1,2,3]
# my_list.pop(0)
# my_list
# print(my_list) ## [2,3]


# college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
# print(list(enumerate(college_years, 2019)))
#### [(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]


