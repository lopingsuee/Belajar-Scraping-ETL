from utils.extract import scrape_all_pages
from utils.load import (
    save_to_csv,
    save_to_postgresql,
)
from utils.transform import transform_data


def main():
    products = scrape_all_pages()

    clean_data = transform_data(products)

    save_to_csv(clean_data)

    save_to_postgresql(clean_data)


if __name__ == "__main__":
    main()