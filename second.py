def cislo_text(cislo):
    cislo = int(cislo)
    
    jednotky = [
        "nula", "jedna", "dva", "tři", "čtyři",
        "pět", "šest", "sedm", "osm", "devět"
    ]
    
    desitky = [
        "", "deset", "dvacet", "třicet", "čtyřicet",
        "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"
    ]
    
    specialni = {
        11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct",
        15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
    }
    
    if cislo == 100:
        return "sto"
    elif cislo < 10:
        return jednotky[cislo]
    elif 10 < cislo < 20:
        return specialni[cislo]
    elif cislo % 10 == 0:
        return desitky[cislo // 10]
    else:
        return desitky[cislo // 10] + " " + jednotky[cislo % 10]


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
