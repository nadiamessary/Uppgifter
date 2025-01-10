# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

def multiplication_table(n: int, limit: int):
    return [n * i for i in range(1, limit + 1)]
n = 4
limit = 8
print(multiplication_table(n, limit))