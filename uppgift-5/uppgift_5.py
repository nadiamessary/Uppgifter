# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(numbers: list[int]) -> int:
    return [num for num in numbers if num % 2 == 0]
numbers = [1, 2, 3, 4, 5, 36, 66]
print(f"Udda tal är filtrerade och jämna tal är: ", filter_odd(numbers))