# -*- coding: utf-8 -*-
"""first.py
Функция sudy_nebo_lichy(cislo) проверяет, чётное или нечётное число,
и печатает сообщение на чешском: "Číslo X je sudé" / "Číslo X je liché".
"""

def sudy_nebo_lichy(cislo):
    """Принимает одно целое число 'cislo' и выводит, sudé (чётное) или liché (нечётное)."""
    try:
        n = int(cislo)
    except Exception:
        print(f"Zadaná hodnota '{cislo}' není celé číslo.")
        return

    if n % 2 == 0:
        print(f"Číslo {n} je sudé")
    else:
        print(f"Číslo {n} je liché")

if __name__ == "__main__":
    # Тестовые вызовы, как в задании
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)
