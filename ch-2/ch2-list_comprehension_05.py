def even_numbers(max):
    for i in range(2, max + 1):
        if i % 2 == 0:
            yield i

print(even_numbers(10))