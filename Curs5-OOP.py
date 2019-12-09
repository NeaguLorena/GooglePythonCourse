class Animal(object):
    def __init__(self, age, name):
        self.age = age  # ! nu mere : self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def speak(self):
        print("ceva")


# a = Animal(4)
# print(a.age)
# print(a.get_age())
# a.age = 5
# print(a.age)
# print(a.get_age())


class Cat(Animal):
    def __init__(self, age, name): # constructorul  nu e necesar aici ca se va folosi ala de la clasa parinte
        self.age = age
        self.name = name

    def speak(self):
        print("Miau")

    def __str__(self):
        return "cat " + str(self.age) + " " + str(self.name)

# pisi = Cat(4, "Pisi")
# print(pisi.age)
# print(pisi.get_age())
# pisi.age = 5
# print(pisi.age)
# print(pisi.get_age())
# print(pisi)


class Person(Animal):
    tag = 1
    def __init__(self,age, name, friends):
        Animal.__init__(self, age, name)
        #self.parent = parent
        self.friends = friends #set(friends) for not duplicates
    def get_friends(self,friends):
        return self.friends
    def __add__(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    def __str__(self):
        return "Animal: " + str(self.age) + " " + str(self.name) + " " + str(self.friends)
    def age_dif(self,b):
        return abs(self.age - b.age)


p1 = Person(100,"Viorica",{"Klaus","Ale"})
p2 = Person(199,"Viorica","Klaus")

p1.__add__("Ale")
print(p1)
print(p1.age_dif(p2))

class Student(Person):
    def __init__(self, age, name,friends, major):
        Person.__init__(self,age,name,friends)
        self.major = major
    def __str__(self):
        return "Student : " + str(self.age) + " " + str(self.name) + " " + str(self.major)
