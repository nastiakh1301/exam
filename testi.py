import random

x = 2 ** 3
x = x + 3
print(x)

num_list = []
for i in range(x):
    num = random.randint(1, x)
    num_list.append(num)
    i += 1

print(num_list[::-1], step = " ")

center = len(num_list) // 2
num_list = num_list[:center] + "11" + num_list[center:]

print(num_list)
    



def create_country_info(country, population, cities):
    data = {"Country": 'country', "Population": 'population', "Cities": 'cities'}
    return data