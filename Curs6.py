#
items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))

print(squared)

#names that start with 'a' or 'b'
names = ['Ana', 'Cristi', 'Bogdan']
filter_names = list(filter(lambda x: x[0] == 'A' or x[0] == 'B', names))
print(filter_names)


#Redure
product = 1
list = [1,2,3,4,5]
for num in list:
    product *= num
print(product)

from functools import reduce
product = reduce((lambda x, y: x * y), [1,2,3,4,5])
print(product)

#Comprehensions
filter_names_compr = [x for x in names if x[0] == 'A' or x[0] == 'B']
print(filter_names_compr)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)


#dictionary
mcase = {'a': 10, 'b': 34,'A': 7, 'Z': 3}

mcase_frequency = {#get takes the value from the dictionary
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys()
}
print(mcase_frequency)

l = [1,2,3,4]
powers = list