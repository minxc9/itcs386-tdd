# test_shipping.py

import pytest
from shipping import shipping_fee


@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),   # Rule 2: Within the first weight range
    (1.0, 40),   # Rule 2: BUG - exactly 1 kg
    (1.5, 60),   # Rule 3: More than 1 kg
    (5.0, 60),   # Rule 3: Exactly 5 kg
    (5.2, 70),   # Rule 4: BUG - started extra kg
    (6.0, 70),   # Rule 4: One full extra kg
    (6.1, 80),   # Rule 4: BUG - fractional extra kg
])
def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected


def test_zero_weight_is_rejected():
    # Rule 1 BUG: weight must be greater than zero
    with pytest.raises(ValueError):
        shipping_fee(0)


def test_negative_weight_is_rejected():
    # Rule 1: negative weight is invalid
    with pytest.raises(ValueError):
        shipping_fee(-1)
