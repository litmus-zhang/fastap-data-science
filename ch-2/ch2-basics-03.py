def euclidean_division(dividend, divisor):
    answer = divmod(dividend, divisor)
    quotient = answer[0]
    remainder = answer[1]
    return quotient, remainder


a, b = euclidean_division(10, 3)
print(a, b)
