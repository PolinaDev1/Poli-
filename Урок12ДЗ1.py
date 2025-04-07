string = input("Введіть рядок:")
numbers = ''.join(num for num in string if not num.isdigit())
print("Без чисел:", numbers)