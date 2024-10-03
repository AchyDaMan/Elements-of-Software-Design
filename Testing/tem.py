numbers = [1, 2, 3, 4, 5]

print(list(map(lambda number: number ** 2 if number % 2 == 0 else number, numbers)))

