def dec_to_bin(cislo):
    try:
        dekadicke_cislo = int(cislo)
    except ValueError:
        raise ValueError("Vstup musí být platné dekadické číslo (str nebo int).")
    
    return bin(dekadicke_cislo)[2:]


def test_dec_to_bin_valid():
    assert dec_to_bin(0) == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin(7) == "111"
    assert dec_to_bin(5) == "101"
    assert dec_to_bin(100) == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin(128) == "10000000"
    assert dec_to_bin(167) == "10011101"
    assert dec_to_bin("0") == "0"
    assert dec_to_bin("167") == "10011101"
    assert dec_to_bin("128") == "10000000"
