"""

    Àlex Modesto Mena
    ASIXc1B
    22 /02/2022
    Fes un programa (en el fitxer CheapestPrice) que donada la llista de preus (sense decimals) de tot de productes,
    retorni el preu del producte més baix

"""

preus = []


def demanarPreus(preus):
    llistapreus = input(" ").split(" ")
    for preu in llistapreus:
        if preu == "-1":
            break
        else:
            preus.append(int(preu))


def preuBaix(preus):
    mesBaix = int(preus[0])
    for preu in preus:
        if int(mesBaix) > int(preu):
            mesBaix = preu
    print(f"El producte més econòmic val: {mesBaix}€")


demanarPreus(preus)
preuBaix(preus)

