# Fashion Studio ETL Pipeline

ETL pipeline project for scraping, transforming, and storing product data from https://fashion-studio.dicoding.dev.

## Project Structure

```bash
submission/
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── utils/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── .env.example
├── .gitignore
├── main.py
├── products.csv
├── pytest.ini
├── requirements.txt
└── README.md
````

## Installation

Clone repository:

```bash
git clone <repository-url>
cd submission
```

Create virtual environment:

```bash
conda create -n etl python=3.12
conda activate etl
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

Install PostgreSQL:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Start PostgreSQL service:

```bash
sudo service postgresql start
```

Open PostgreSQL:

```bash
sudo -u postgres psql
```

Create database:

```sql
CREATE DATABASE fashion_db;
```

Set password:

```sql
ALTER USER postgres PASSWORD 'postgres';
```

Exit PostgreSQL:

```sql
\q
```

## Environment Variables

Create `.env` file:

```env
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
```

## Run ETL Pipeline

```bash
python main.py
```

Output:

* `products.csv`
* PostgreSQL table `fashion_products`

## Run Unit Test

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=utils
```
