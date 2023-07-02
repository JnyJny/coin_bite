class Coin:
    def __init__(self, value: float) -> None:
        self.value = value

    @property
    def name(self) -> str:
        return self.__class__.__name__.title()

    def __repr__(self) -> str:
        return f"{self.name}(value={self.value!r})"

    def __str__(self) -> str:
        return self.name[0].lower()

    def __eq__(self, other) -> bool:
        try:
            return isinstance(self, other)
        except TypeError:
            pass

        return isinstance(self, type(other))

    def __hash__(self) -> int:
        return int(self.value)

    def __add__(self, other):
        if issubclass(other, Coin):
            return self.value + other.value
        return self.value + other

    def __radd__(self, other):
        return other + self.value


class Penny(Coin):
    def __init__(self) -> None:
        super().__init__(0.01)


class Nickel(Coin):
    def __init__(self) -> None:
        super().__init__(0.05)


class Dime(Coin):
    def __init__(self) -> None:
        super().__init__(0.10)


class Quarter(Coin):
    def __init__(self) -> None:
        super().__init__(0.25)


def coins_on_the_table(n_pennies: int = 1001) -> list[Penny | Nickel | Dime | Quarter]:

    substitutions = {1: Penny, 2: Nickel, 3: Dime, 4: Quarter}
    coins = []
    for n in range(0, n_pennies):
        for pos, coin in substitutions.items():
            if (n + 1) % pos == 0:
                c = coin()
        coins.append(c)
    return coins


if __name__ == "__main__":
    from collections import Counter

    coins = coins_on_the_table()

    c = Counter(coins)

    for key, value in c.items():
        print(key.name, value)

    print("total:", round(sum(coins), 2))
