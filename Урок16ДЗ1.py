temperatures = [0, 25, 100, -10]
def fahrenheit(temp):
    return (temp * 9 / 5) + 32
fahrenheit_temperatures = list(map(fahrenheit, temperatures))
even_fahrenheit_temperatures = list(filter(lambda x: x % 2 == 0, fahrenheit_temperatures))
print(even_fahrenheit_temperatures)
