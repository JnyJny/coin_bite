from enum import Enum
from decimal import Decimal


Penny = "p"
Nickel = "n"
Dime = "d"
Quarter = "q"


class CoinInt(int, Enum):
    Penny = 1
    Nickel = 5
    Dime = 10
    Quarter = 25


Penny = CoinInt.Penny
Nickel = CoinInt.Nickel
Dime = CoinInt.Dime
Quarter = CoinInt.Quarter


Penny = Decimal(0.01)
Nickel = Decimal(0.05)
Dime = Decimal(0.1)
Quarter = Decimal(0.25)


class Coin:
    @classmethod
    def penny(cls) -> "Coin":
        return cls(0.01)

    @classmethod
    def nickel(cls) -> "Coin":
        return cls(0.05)

    @classmethod
    def dime(cls) -> "Coin":
        return cls(0.1)

    @classmethod
    def quarter(cls) -> "Coin":
        return cls(0.25)

    def __init__(self, value: float) -> None:
        self.value = value


Penny = Coin.penny()
Nickel = Coin.nickel()
Dime = Coin.dime()
Quarter = Coin.quarter()


def coins_on_the_table(n_pennies: int = 1001) -> list[Coin]:

    substitutions = {1: Penny, 2: Nickel, 3: Dime, 4: Quarter}
    coins = []
    for n in range(0, n_pennies):
        for pos, coin in substitutions.items():
            if (n + 1) % pos == 0:
                c = coin
        coins.append(c)
    return coins
