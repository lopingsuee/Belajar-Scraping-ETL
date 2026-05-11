from datetime import datetime

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://fashion-studio.dicoding.dev"


def fetch_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() #penerapan advanced

        return BeautifulSoup(response.text, "lxml")

    except requests.RequestException as error:
        print(f"Failed to fetch {url}: {error}")

        return None


def parse_product(card):
    try:
        title_element = card.find(
            "h3",
            class_="product-title"
        )

        price_element = card.find(
            "span",
            class_="price"
        )

        details = card.find_all("p")

        rating = details[0].text.strip() if len(details) > 0 else None
        colors = details[1].text.strip() if len(details) > 1 else None
        size = details[2].text.strip() if len(details) > 2 else None
        gender = details[3].text.strip() if len(details) > 3 else None

        return {
            "title": (
                title_element.text.strip()
                if title_element
                else None
            ),
            "price": (
                price_element.text.strip()
                if price_element
                else None
            ),
            "rating": rating,
            "colors": colors,
            "size": size,
            "gender": gender,
            "timestamp": datetime.now().isoformat(), #penerapan skilled
        }

    except AttributeError as error:
        print(f"Failed to parse product: {error}")

        return None


def scrape_page(page):
    try:
        url = (
            BASE_URL
            if page == 1
            else f"{BASE_URL}/page{page}"
        )

        soup = fetch_page(url)

        if soup is None:
            return []

        cards = soup.find_all(
            "div",
            class_="collection-card"
        )

        products = []

        for card in cards:
            product = parse_product(card)

            if product:
                products.append(product)

        return products

    except Exception as error:
        print(f"Failed to scrape page {page}: {error}")

        return []


def scrape_all_pages(start_page=1, end_page=50):
    try:
        all_products = []

        for page in range(start_page, end_page + 1):
            print(f"Scraping page {page}")

            products = scrape_page(page)

            all_products.extend(products)

        return all_products

    except Exception as error:
        print(f"Failed during scraping process: {error}")

        return []