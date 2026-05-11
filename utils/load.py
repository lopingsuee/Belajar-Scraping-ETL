def save_to_csv(dataframe, filename="products.csv"):
    try:
        dataframe.to_csv(filename, index=False)

        print(f"Data saved to {filename}")

    except Exception as error:
        print(f"Failed to save CSV: {error}")