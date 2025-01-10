# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password: str) -> str:
    val = True
    if len(password) < 8:
        print("lösenordet måste vara minst 8 tecken långt")
        val = False
    if not any(char.isdigit() for char in password):
        print("lösenordet måste innehålla minst en siffra")
        val = False
    return val

print(validate_password("hejhej"))
print(validate_password("hejsan123"))