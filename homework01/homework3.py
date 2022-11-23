# задание 1


# a  = [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8, ]

# def func(arg):
#     my_list = sorted(arg)
#     my_dict = list(set(my_list))


#     for i in range(len(my_dict)):
#         my_dict = {number: number + number for number in my_list}

#     source = {'source': list (set(my_list))}
#     my_dict.update (source)
#     total = {"total":sum(list(set(my_list)))}
#     my_dict.update (total)

#     return my_dict

# print(func(a))



S = '72 101 108 108 111 '
S1 = map(int, S.split())
S1 = [chr(x) for x in S1]
print(S1)