# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text: str) -> int:
    words = text.split()
    return len(words)
text = "hej jag heter nadia"
print(word_count(text))