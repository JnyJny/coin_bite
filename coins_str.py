Penny = "p"
Nickel = "n"
Dime = "d"
Quarter = "q"


def coins_on_the_table(n_pennies: int = 1001) -> list:

    substitutions = {1: Penny, 2: Nickel, 3: Dime, 4: Quarter}
    coins = []
    for n in range(0, n_pennies):
        for pos, coin in substitutions.items():
            if (n + 1) % pos == 0:
                c = coin
        coins.append(c)
    return coins
