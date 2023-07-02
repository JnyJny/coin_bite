from enum import Enum

class Coin(int, Enum):
    Penny = 1
    Nickel = 5
    Dime = 10
    Quarter = 25


Penny = Coin.Penny
Nickel = Coin.Nickel
Dime = Coin.Dime
Quarter = Coin.Quarter

def coins_on_the_table(n_pennies: int = 1001) -> list[Coin]:

    substitutions = {1: Penny, 2: Nickel, 3: Dime, 4: Quarter}
    coins = []
    for n in range(0, n_pennies):
        for pos, coin in substitutions.items():
            if (n + 1) % pos == 0:
                c = coin
        coins.append(c)
    return coins
