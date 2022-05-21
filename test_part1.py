import pytest
from part1 import first_exercise


@pytest.mark.parametrize(
    "array1, array2, expected",
    [
        ([-100, 0, 0], [1, 1, -100, 2], -100),
        ([1], (0, 1), 1),
        ([-70, 1], (2, 2), None),
        ((0,), (1, 2), None)
    ]
)
def test_first_exercise_result(array1, array2, expected):
    assert first_exercise(array1, array2) == expected


@pytest.mark.parametrize(
    "array1, array2",
    [
        ([-100, 0, 0], '12390'),
        (1, (-100, 0)),
        ({1: 2, 2: 3}, 'string'),
    ]
)
def test_first_exercise_exception(array1, array2):
    with pytest.raises(TypeError):
        first_exercise(array1, array2)
