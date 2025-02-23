import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Laddar data från hela CSV-filen
df = pd.read_csv(r"C:\Users\nadia\Data Science\inlupp\exempel\bearbetad_data.csv")

# Ändrar "datum" till datetime-format och skapar en kolumn för antal dagar från startdatum
df["datum"] = pd.to_datetime(df["datum"], errors="coerce")
df["dagar_från_start"] = (df["datum"] - df["datum"].min()).dt.days

# Skapar kumulativ summa för att visa totalkostnader över tid
df["kumulativ_kostnad"] = df["belopp"].cumsum()

# Tar bort NaN-värden i kumulativ_kostnad
df = df.dropna(subset=["kumulativ_kostnad"])

X = df[["dagar_från_start"]]
y = df["kumulativ_kostnad"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skapar och tränar linjär regressionsmodell
model = LinearRegression()
model.fit(X_train, y_train)

# Förutsägelse för de kommande 100 dagarna
framtida_dagar = pd.DataFrame({"dagar_från_start": np.arange(df["dagar_från_start"].max() + 1, df["dagar_från_start"].max() + 101)})
framtida_kostnad = model.predict(framtida_dagar)

# Visualiserar kumulativ kostnad och förutsägelser för de kommande 100 dagarna
plt.figure(figsize=(10, 6))
plt.plot(df["dagar_från_start"], df["kumulativ_kostnad"], label="Kumulativ kostnad från leverantörsfakturorna", color="blue")
plt.plot(framtida_dagar["dagar_från_start"], framtida_kostnad, label="Förutspådd framtida kostnad", linestyle="--", color="green")
plt.xlabel("Dagar från start")
plt.ylabel("Kumulativ kostnad")
plt.title("Totalkostnad över tid")
plt.legend()
plt.grid(True)
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.ticklabel_format(style="plain", axis="y")
plt.show()
