from collections import Counter
from typing import Any, Union

import pytest

from coins import Penny, Nickel, Dime, Quarter, coins_on_the_table

T_COINS = Union[type(Penny), type(Nickel), type(Dime), type(Quarter)]

T_COINLIST = list[T_COINS]


@pytest.fixture(scope="module")
def coins() -> T_COINLIST:
    return coins_on_the_table()


@pytest.fixture(scope="module")
def coin_value_map() -> dict[T_COINS, float]:
    return {Penny: 0.01, Nickel: 0.05, Dime: 0.1, Quarter: 0.25}


@pytest.mark.parametrize(
    "expected_coin,expected_count",
    [
        (Penny, 334),
        (Nickel, 167),
        (Dime, 250),
        (Quarter, 250),
    ],
)
def test_count_coin_on_table(
    expected_coin: T_COINS, expected_count: int, coins: T_COINLIST
) -> None:

    assert sum(coin == expected_coin for coin in coins) == expected_count


@pytest.mark.parametrize("expected", [99.19])
def test_total_dollar_amount(
    expected: float, coins: T_COINLIST, coin_value_map: dict[T_COINS, float]
) -> None:
    """Calculating the total dollar amount is predicated on the
    correctness of the counts, so it's not even really necessary
    unless we want the student implmentations of Penny, Nickel, Dime
    and Quarter to provide their values.
    """

    counts = Counter(coins)

    total = 0
    for coin, value in coin_value_map.items():
        total += counts[coin] * value

    assert total == expected
