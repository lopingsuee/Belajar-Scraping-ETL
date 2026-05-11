import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def save_to_csv(dataframe, filename="products.csv"):
    try:
        dataframe.to_csv(filename, index=False)

        print(f"Data saved to {filename}")

    except Exception as error:
        print(f"Failed to save CSV: {error}")


def save_to_postgresql(
    dataframe,
    table_name="fashion_products",
):
    try:
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_NAME")

        url = (
            f"postgresql://{user}:{password}"
            f"@{host}:{port}/{database}"
        )

        engine = create_engine(url)

        dataframe.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False,
        )

        print(
            f"Data saved to PostgreSQL table: {table_name}"
        )

    except Exception as error:
        print(f"Failed to save PostgreSQL: {error}")