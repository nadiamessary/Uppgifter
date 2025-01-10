# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(text):
    return text == text[::-1]

text = "aha"
palindrom = is_palindrome(text)
if palindrom:
    print("Det är ett palindrom")
else:
    print("Det är inte ett palindrom")