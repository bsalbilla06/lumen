import pytest

from lumen import compact_number


@pytest.mark.parametrize(
    "value, expected",
    [
        (None, "0"),
        (0, "0"),
        (499, "499"),
        (999_999, "999,999"),
        (1_000_000, "1.0 million"),
        (5_224_879, "5.2 million"),
        (16_058_634_931, "16.1 billion"),
        (2_500_000_000_000, "2.5 trillion"),
    ],
)
def test_compact_number(value, expected):
    assert compact_number(value) == expected
