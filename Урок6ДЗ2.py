string = input("Введіть рядок: ")
count = 0
if string:
    first_letter = string[0]
    count = string.count(first_letter)
    print(f"Літера '{first_letter}' зустрічається {count} разів ")