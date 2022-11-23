from ast import BinOp
from re import A


qwerty="qwerty"
qwerty2="qwerr" # -> str() 
num = 16 # -> int()
num2 = 14.5 # -> float()

name ='John'
surname = 'Nash'
company = 'Google'
bio = """
{0}{1}is a talented Python developer.
he works at {2}.
""".format(name, surname, company)

print(bio)
"""
мы получим следующее:

John Nash is a talented Python developer.
He works at Google.

"""

biio = f"{name}{surname} is a talented Python developer. \
    \nHe works at {company}."
print(biio)

























# value = int(input("Введите что то: "))

# print(f"Тип: {type(value)} Знач.: {value}")

# res = f"Значение -> {num} {value}"
# print(res)
# print(value)

# print(type(qwerty))

# print(type(num))

# print(type(num2))


name = input("Введите свое имя: ")
age = int(input("Введиите возраст: ")) # ----> Имя: Tima Возраст: 18

res = f"{name}  {age}"

print(res)