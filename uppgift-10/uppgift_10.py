# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5 + 32)
    return fahrenheit

celsius_temperatur = 10
fahrenheit_temperatur = celsius_to_fahrenheit(celsius_temperatur)
print(f"{celsius_temperatur} celsius är ungefär {fahrenheit_temperatur} fahrenheit")