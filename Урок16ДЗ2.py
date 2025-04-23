numbers = [ 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x ** 2, numbers))
even_squared_numbers = list(filter(lambda x: x % 2 == 0, squared_numbers))
print(even_squared_numbers)