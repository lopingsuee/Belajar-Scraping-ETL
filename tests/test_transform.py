import pandas as pd

from utils.transform import (
    clean_colors,
    clean_gender,
    clean_price,
    clean_rating,
    clean_size,
    transform_data,
)


def test_clean_price():
    result = clean_price("$10.00")

    assert result == 160000.0


def test_clean_price_invalid():
    result = clean_price(None)

    assert result is None


def test_clean_rating():
    result = clean_rating(
        "Rating: ⭐ 4.5 / 5"
    )

    assert result == 4.5


def test_clean_rating_invalid():
    result = clean_rating(None)

    assert result is None


def test_clean_colors():
    result = clean_colors("3 Colors")

    assert result == 3


def test_clean_colors_invalid():
    result = clean_colors(None)

    assert result is None


def test_clean_size():
    result = clean_size("Size: XL")

    assert result == "XL"


def test_clean_size_invalid():
    result = clean_size(None)

    assert result is None


def test_clean_gender():
    result = clean_gender("Gender: Men")

    assert result == "Men"


def test_clean_gender_invalid():
    result = clean_gender(None)

    assert result is None


def test_transform_data():
    sample_data = [
        {
            "title": "T-shirt 1",
            "price": "$10.00",
            "rating": "Rating: ⭐ 4.5 / 5",
            "colors": "3 Colors",
            "size": "Size: M",
            "gender": "Gender: Men",
            "timestamp": "2025-01-01",
        }
    ]

    result = transform_data(sample_data)

    assert isinstance(
        result,
        pd.DataFrame
    )

    assert result.iloc[0]["title"] == "T-shirt 1"

    assert result.iloc[0]["price"] == 160000.0

    assert result.iloc[0]["rating"] == 4.5