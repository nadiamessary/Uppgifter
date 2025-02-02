import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates 
from matplotlib.ticker import ScalarFormatter

# Leverantörsfakturor från Digg
df = pd.read_csv("2024-Q3 Digg Leverantörsfakturor.csv", delimiter=";")
print(df.head())

# Hantera saknade värden
df = df.dropna()

# Visar datatyper
print("\nDatatyper i csv-filen:")
print(df.dtypes)

# Konverterar datum till datetime
df["datum"] = pd.to_datetime(df["datum"])

# Konverterar belopp till numeriska värden för att göra beräkningar
df["belopp"] = pd.to_numeric(df["belopp"], errors="coerce")

# Visar konverterade datatyper
print("\nDatatyper efter konvertering:")
print(df.dtypes)

# Filtrering som visar fakturor som överstiger 100 000 SEK
faktura_100k = df[df["belopp"] > 100000]
print("\nFakturor som överstiger 100 000 SEK:")
print(faktura_100k)

# Filtrering som visar köp gjorda i SEK
df_valuta_sek = df[df["valuta"] == "SEK"]
print("\nKöp är gjorda i SEK:")
print(df_valuta_sek)

# Filtrering som visar köp gjorda i annan valuta än SEK
df_valuta_annan = df[df["valuta"] != "SEK"]
print("\nKöp som inte är gjorda i SEK:")
print(df_valuta_annan)

# Konvertera NOK till SEK
vaxlingskurs_nok_till_sek = 0.98
def filter_valuta(df, valuta):
    return df[df["valuta"] == valuta].copy()
df_sek = filter_valuta(df, "SEK")
df_nok = filter_valuta(df, "NOK")
df_nok.loc[:, "belopp_sek"] = df_nok["belopp"] * vaxlingskurs_nok_till_sek
df_sek.loc[:, "belopp_sek"] = df_sek["belopp"]
df_konverterad = pd.concat([df_sek, df_nok], ignore_index=True)
print(df_konverterad.head())

# Summering av antal köp från varje leverantör och totalsumma
df_summering = df.groupby("leverantor").agg(antal_kop=("leverantor", "size"), totalsumma=("belopp", "sum")).reset_index()
print("\nSummering av antal köp från varje levrantör och totalsumma:")
print(df_summering)

df["ar_manad"] = df["datum"].dt.to_period("M")
df_monthly = df.groupby("ar_manad").agg(total_belopp=("belopp", "sum")).reset_index()
df_monthly["ar_manad"] = df_monthly["ar_manad"].dt.to_timestamp()

# Linjediagram
plt.figure("Linjediagram")
plt.plot(df_monthly["ar_manad"], df_monthly["total_belopp"], marker="o")
plt.title("Totalbelopp över tid")
plt.xlabel("Månad")
plt.ylabel("Totalbelopp")
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.gcf().autofmt_xdate()
ax.yaxis.set_major_formatter(ScalarFormatter())
plt.ticklabel_format(style="plain", axis="y")

# Stapeldiagram
plt.figure("Stapeldiagram")
plt.bar(df_summering["leverantor"], df_summering["antal_kop"])
plt.title("Antal köp från varje leverantör")
plt.xlabel("Leverantör")
plt.ylabel("Antal köp")
plt.xticks(rotation=90)

# Scatter plot
plt.figure("Scatter plot")
plt.scatter(df_summering["antal_kop"], df_summering["totalsumma"])
plt.title("Antal köp och totalsumma")
plt.xlabel("Antal köp")
plt.ylabel("Totalsumma")
plt.ticklabel_format(style="plain", axis="y")

plt.show()

df.to_excel("bearbetad_data.xlsx", index=False)