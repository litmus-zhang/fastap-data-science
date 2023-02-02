from random import randint, seed

seed(10)
random_elements = {i: randint(0, 10) for i in range(5)}
print(random_elements)
#print(list(random_elements))