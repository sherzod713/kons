# Дан список [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8, ]

# Напишите функцию принимающую в себя этот список. Она должна возвращать следующий словарь:

# {3: 6, 5: 10, 6: 12, 8: 16, 13: 26, 15: 30, 'source': [3, 5, 6, 8, 13, 15], 'total': 50}



# Задание 2
# Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой.
# Результат: "AAiddialneat"
# В решении обязательно должнен испрользоваться цикл for



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






a = "Aidana"
b = "Adilet"

result = ''

if len(a) != len(b):
    print("dlina doljna byt odinakovoi")
else :
    for i in range(len(a)):
        result += a [i] + b[i]

print(result)





