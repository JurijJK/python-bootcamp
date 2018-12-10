import json
from urllib.request import urlopen

miasto = input("Podaj miasto: ")


with urlopen(f"https://www.metaweather.com/api/location/search/?query={miasto}") as file:
    data = json.loads(file.read().decode("utf-8"))

print(data)
woeid = int(data[0]["woeid"])
print(woeid)

with urlopen(f"https://www.metaweather.com/api/location/{woeid}") as file:
    data = json.loads(file.read().decode("utf-8"))

print(data)

prognozy = data["consolidated_weather"]
for prognoza in prognozy:
    print(f"Dzień: {prognoza['applicable_date']}")
    print(f"Temperatura: {prognoza['the_temp']:.0f}")