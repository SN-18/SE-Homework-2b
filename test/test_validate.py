from code.validate import Calculator
import pytest
val = Calculator()

@pytest.mark.parametrize('values, result', [
    ([0, 1, 2, 3], 6),
    ([-16, 9, 7, 3], 3),
    ([-1, -1, -1, False], -3)
])
def test_list_add(values, result):
    assert val.list_add(values) == result

@pytest.mark.parametrize('values, result', [
    ([0, 1, 2, 3], 3),
    ([-2, 9, 7, 3], 9),
    ([-1, -1, -1, False], 0)
])
def test_list_maximum(values, result):
    assert val.list_maximum(values) == result
