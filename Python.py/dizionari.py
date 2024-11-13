dizionario = {"nome": "Greta", "cognome": "Levi", "eta": 23}
print(dizionario)
print(dizionario["nome"])
print(dizionario["cognome"])
print(dizionario["eta"])

dizionario["eta"] = 24
print(dizionario)

del dizionario["eta"]
print(dizionario)

dizionario["eta"] = 24
print(dizionario)

dizionario.pop("eta")
print(dizionario)

print(dizionario.values())
print(dizionario.keys())