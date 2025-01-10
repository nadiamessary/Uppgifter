# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

n = 10
fib_n = fibonacci(n)
print(f"De första {n} Fibonnaci-talen är {fib_n}")