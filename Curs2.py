# x = 10
# while x>1:
#     #print ("x este:",x)
#     x = x-1

# while True:
#     euro = input("Val euro:")
#     if euro.isdigit():
#         euro=int(euro)
#         print("Valoare convertita :",euro*4.5,"RON")
#     else:
#         print("Val nu e numar")
#
#     quit = input("Apasa q pt a iesi")
#     if quit.upper() == "Q":
#         break
#     else:
#         pass

#infinite loop:
# x = 10
# while x>1:
#     print("x este {}".format(x))
#     continue
#     x-=1


# for i in range(0,50,5):
#     print(i)
#
# for var in "abcde":
#     print (var)


#strings are immutable
#can't change strings like below :
#   str = "Hello"
#   str[0] = 'd'
#   print (str)

#interpolare:
x = "abcde"
print("litrra cautate este r. Ea exista? {}".format(x.find("r")))
print(x.find("bc"))
print(x.find("d"))

#split:
y = "sir de car"
print(y.split(" "))

#tuple
x = ()
coordonate = (3,4,5)

#mutable
l = [1,2,3,'Gugal',[5,4,6]]
l[0] = 'Salut'

#sortarea unei liste
p = [7,4,1]
p.sort()
sorted(p) #va afisa doar o noua lista sortata nu se va atige de p si functia e mai inceata decat sort ca face o copie

#in lista poti avea duplicate
print(l[:]) #afiseaza toata lista
print(l[2:])
print(l[::2]) #afiseaza din 2 in 2

#SET - nu poti avea dupolicate

#Dictionar
#Used in google search engine
#fiecare cuv sunt niste chei din dictionar
#gen hashmap
#mutable
d = { 1: "Marius",
      2: "Lore",
      3: "Ale",
      'varsta' : 32}

d[1]
d[2]
var1 = d.get(2,'')
var2 = d.get(4,"NUP")
print(var1)
print(var2)

for k,val in d.items():
    #print(k,val)

for k,val in dict.iteritems():
    print(k,val)
