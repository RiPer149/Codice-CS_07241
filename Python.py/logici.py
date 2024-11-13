if(1 < 3): print("Vero")
if(1 > 3): 
    print("non stampa")   #questo perchè è falso
else:
    print("Vero")

    if(1 <= 1): print("Vero")
    if(1 >= 1): print("Vero")
    if(2 != "Uno"): print("Vero")
    if(1 == 1): print("Vero")
    if(type(1) is int): print("Vero Vero")
    if(type("Ciao") is not int): print("Non è un intero")

    lista = [1, 2, 3, "Pippo"]
    if("Pippo" in lista): print("Pippo è in lista")
    if("Paolo" not in lista): print("Paolo non è in lista")
    if(not 1 > 1): print("Nego la maggioranza")
    if((1 > 1) or (2 == 2)): print("La seconda è vera")
    if((1 == 1) and ("Pippo" == "Pippo")): print("Sono entrambe vere")

    if(1 == "1"): print("Falso")   # non verrà scritta perchè una stringa non viene convertita in intero

