def convert_to_czk(amount, currency):
    text = requests.get(
        "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    ).text

    for line in text.splitlines():
        parts = line.split("|")
        if len(parts) == 5 and parts[3] == currency:
            rate = float(parts[4].replace(",", "."))
            quantity = int(parts[2])
            return round(amount * rate / quantity, 2)

    raise ValueError(f"Currency {currency} not found in the exchange rate list.")
