# n=int(input("Выбери число "))
# d = dict()
# for x in range(1,n+1):
#     d[x]=x*x**2
# print(d)

# filename = "greetings.txt"
# name = input('Введите ваше имя:')
# with open (filename, 'w') as f:
#     for i in range(10):
#         f.write(f"greetings {name}\n")
#     for i in range(1):
#         f.write(f'edited by {name}')

# file = open('greeting.txt', 'a', encoding = 'utf8')
# name = input()
# for i in range(10):
#     print(name, 'hello')



# def longest_word(f):
#     with open (f) as text:
#         words = text.read().split()
#     max_lenght = len (max(words,key=len))
#     L_words = [word for word in words if len(word) == max_lenght]
# if  len(L_words) == 1:
#     return L_words[0]
# return L_words 










# from unittest import result


# a = "Aidana"
# b = "Adilet"

# result = ''

# if len(a) != len(b):
#     print("dlina doljna byt odinakovoi")
# else :
#     for i in range(len(a)):
#         result += a [i] + b[i]

# print(result)





# def mach():
#     a = [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8, ]


#     b = set (a)
#     s = []
#     summ = 0
#     for i in range(b):
#         summ += 1

#     for i in range(b): 
#         b = {}

# mach()






# def aaa() :   

#    lst = [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8, ]

#    lst1 = set(lst)

#    c = []

#    summ = 0

#    for item in lst1 :

#     summ += item

#    for i in lst1 :

#     a = {lst :lst*2 for lst in lst1}

#     c.append(i)

#     a.update(source = c , total = summ)

#    print(a)

# aaa()














# задание 1
from typing import List

a  = [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8, ]

def func(arg):
    my_list = sorted(arg)
    my_dict = list(set(my_list))


    for i in range(len(my_dict)):
        my_dict = {number: number + number for number in my_list}

    source = {'source': list (set(my_list))}
    my_dict.update (source)
    total = {"total":sum(list(set(my_list)))}
    my_dict.update (total)

    return my_dict

print(func(a))



S = '72 101 108 108 111 '
S1 = map(int, S.split())
S1 = [chr(x) for x in S1]
print(S1)


