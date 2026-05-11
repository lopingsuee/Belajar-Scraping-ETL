import pandas as pd


EXCHANGE_RATE = 16000


def clean_price(price):
    try:
        price = price.replace("$", "").strip()

        return float(price) * EXCHANGE_RATE

    except (AttributeError, ValueError):
        return None


def clean_rating(rating):
    try:
        rating = (
            rating
            .replace("Rating: ⭐", "")
            .replace("/ 5", "")
            .strip()
        )

        return float(rating)

    except (AttributeError, ValueError):
        return None


def clean_colors(colors):
    try:
        colors = colors.replace("Colors", "").strip()

        return int(colors)

    except (AttributeError, ValueError):
        return None


def clean_size(size):
    try:
        return size.replace("Size:", "").strip()

    except AttributeError:
        return None


def clean_gender(gender):
    try:
        return gender.replace("Gender:", "").strip()

    except AttributeError:
        return None


def transform_data(data):
    try:
        df = pd.DataFrame(data)

        df["price"] = df["price"].apply(clean_price)
        df["rating"] = df["rating"].apply(clean_rating)
        df["colors"] = df["colors"].apply(clean_colors)
        df["size"] = df["size"].apply(clean_size)
        df["gender"] = df["gender"].apply(clean_gender)

        df = df.dropna()

        df = df.drop_duplicates()

        df = df[df["title"] != "Unknown Product"]

        return df

    except Exception as error:
        print(f"Transformation failed: {error}")

        return pd.DataFrame()