nr = 3 #input("Rogu-te introdu numar")
try:
    # nr+7
    int(nr)+7
    print(nr)
except:
    print("eroare")

def nume():
    print("nume")
nume()

def zi(nume,vr = 6):
    print("numa {} vr {}".format(nume,vr))

zi("Lore")

x = 2
def Test():
    global x
    print(x)
    x = 3
    print(x)

def suma(a,b,*c):
    #c is a tuple with all elements introduced
    "cel putin 2 parametrii"
    x = a+b
    if c:
        print("c=> {}".format(c))
        for e in c:
            x += e
    return x

print(suma(1,2,3,5))

def f(a,**b):
    print(a,b)

f("paramb", unu=1, doi=2)