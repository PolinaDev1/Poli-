surname = 'Коплик'
letter = max(set(surname), key=surname.count)
print(f"Найчастіша літера: '{letter}'")