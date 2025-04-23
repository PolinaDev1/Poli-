names = ["Vika", "Ivan", "John", "Polina", "Olga", "Ivan"]
unique_names = list(filter(lambda x: names.count(x) == 1, names))
full_names = list(map(lambda name: f"{name} Smith", unique_names))
print(full_names)