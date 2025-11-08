def je_tah_mozny(figurka, cilova, obsazene):
    typ, (r, s) = figurka["typ"], figurka["pozice"]
    r2, s2 = cilova
    dr, ds = r2 - r, s2 - s

    if not (1 <= r2 <= 8 and 1 <= s2 <= 8) or cilova in obsazene:
        return False

    if typ == "pěšec":
        return s == s2 and ((dr == 1 and (r+1, s) not in obsazene)
                            or (r == 2 and dr == 2 and all((x, s) not in obsazene for x in (3, 4))))

    if typ == "jezdec":
        return (abs(dr), abs(ds)) in [(1, 2), (2, 1)]

    if typ in ("věž", "střelec", "dáma"):
        if typ in ("věž", "dáma") and (r == r2 or s == s2):
            rng = range(s + (s2 > s) - (s2 < s), s2, 1 if s2 > s else -1) if r == r2 else \
                  range(r + (r2 > r) - (r2 < r), r2, 1 if r2 > r else -1)
            return all(((r, x) not in obsazene for x in rng)) if r == r2 else \
                   all(((x, s) not in obsazene for x in rng))
        if typ in ("střelec", "dáma") and abs(dr) == abs(ds):
            kr, ks = (1 if dr > 0 else -1), (1 if ds > 0 else -1)
            return all((r+i*kr, s+i*ks) not in obsazene for i in range(1, abs(dr)))
        return False

    if typ == "král":
        return max(abs(dr), abs(ds)) == 1

    return False
