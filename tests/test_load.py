from unittest.mock import patch

import pandas as pd

from utils.load import (
    save_to_csv,
    save_to_postgresql,
)


def test_save_to_csv(tmp_path):
    dataframe = pd.DataFrame(
        {
            "title": ["T-shirt"],
            "price": [100000],
        }
    )

    file_path = tmp_path / "products.csv"

    save_to_csv(dataframe, file_path)

    assert file_path.exists()


@patch("utils.load.create_engine")
def test_save_to_postgresql(mock_engine):
    dataframe = pd.DataFrame(
        {
            "title": ["T-shirt"],
            "price": [100000],
        }
    )

    save_to_postgresql(dataframe)

    mock_engine.assert_called_once()