numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
product = 1
for _ in numbers:
    print(_, _ ** 2)
    total += _
    product *= _
print(total, product)