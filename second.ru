def cislo_text(cislo):
    cislo = int(cislo)

    if cislo == 0:
        return "nula"
    elif cislo == 1:
        return "jedna"
    elif cislo == 15:
        return "patnáct"
    elif cislo == 25:
        return "dvacet pět"
    elif cislo == 100:
        return "sto"
    else:
        return "zatím neumím toto číslo"


print(cislo_text("0"))
print(cislo_text("1"))
print(cislo_text("15"))
print(cislo_text("25"))
print(cislo_text("100"))
