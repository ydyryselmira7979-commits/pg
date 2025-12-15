def dec_to_bin(cislo):
    cislo = int(cislo)
    if cislo == 0:
        return "0"
    vysledek = ""
    while cislo > 0:
        vysledek = str(cislo % 2) + vysledek
        cislo //= 2
    return vysledek
