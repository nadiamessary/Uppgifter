# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(text):
    dictionary = {}
    for ch in text:
        if ch in dictionary:
            dictionary[ch] += 1
        else:
            dictionary[ch] = 1
    return dictionary

string = "hejhahahabajs"
result = count_letters(string)
print(result)