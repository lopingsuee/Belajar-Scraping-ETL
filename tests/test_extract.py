from bs4 import BeautifulSoup

from utils.extract import (
    fetch_page,
    parse_product,
    scrape_page,
)


def test_fetch_page():
    result = fetch_page(
        "https://fashion-studio.dicoding.dev"
    )

    assert result is not None


def test_fetch_page_invalid():
    result = fetch_page(
        "https://invalid-url-test.com"
    )

    assert result is None


def test_parse_product():
    html = """
    <div class="collection-card">
        <h3 class="product-title">T-shirt 1</h3>
        <span class="price">$10.00</span>

        <p>Rating: ⭐ 4.5 / 5</p>
        <p>3 Colors</p>
        <p>Size: M</p>
        <p>Gender: Men</p>
    </div>
    """

    soup = BeautifulSoup(html, "lxml")

    card = soup.find(
        "div",
        class_="collection-card"
    )

    result = parse_product(card)

    assert result["title"] == "T-shirt 1"

    assert result["price"] == "$10.00"

    assert result["rating"] == "Rating: ⭐ 4.5 / 5"


def test_parse_product_invalid():
    html = """
    <div class="collection-card"></div>
    """

    soup = BeautifulSoup(html, "lxml")

    card = soup.find(
        "div",
        class_="collection-card"
    )

    result = parse_product(card)

    assert result["title"] is None


def test_scrape_page():
    result = scrape_page(1)

    assert isinstance(result, list)

    assert len(result) > 0