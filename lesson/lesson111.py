from tokenize import Name

from xml.dom.minidom import NamedNodeMap


class Person:
    age = 17
    hp = 10

def __init__(self,name,damage):
    self.name = name
    self.damage = damage

Vadim = Person('Вадим',10) 
Aziz = Person('aziz',10)

Vadim.age = 17
Vadim.hp =  100

Aziz.age = 17
Aziz.damage =100 


class katana:
    damage = 44
    strange = 30


def __init__(self, name, damage):
    self.name = Name
    self.damage = damage





print(f' имя :{Vadim.name} жизнь: {Vadim.hp} возраст: {Vadim.age} лет урон: {Vadim.damage}')
print(f'{Aziz.name} {Aziz.hp} {Aziz.age} {Aziz.damage}')






















# vadim = Person()

# print(vadim.age)
