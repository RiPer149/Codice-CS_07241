def saluta(nome):
    saluto = f"Ciao, {nome}!"
    return saluto

def somma(a, b):
    return a + b

def saluta_antonio():
    return "Saluta Antonio"

messaggio=saluta("Alice")
print(messaggio)
print(somma(3, 5))
print(saluta_antonio())

def mia_funzione():
    numero = 7
    print(numero)

mia_funzione()
#print numero non è più accessibile

globale = 20
def stampa_1():
    print(globale)
def stampa_2():
    print(globale)

stampa_1()
stampa_2()

def saluta(nome, messaggio):
    print(f"{messaggio}, {nome}!")

saluta(messaggio = "Ciao", nome = "Alice")
saluta(messaggio="Hey")

def sottrazione(x, y):
    return x - y
print(sottrazione(3,4))
print(sottrazione(y=3, x=4))