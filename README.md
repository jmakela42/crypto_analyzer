# crypto_analyzer
Technical assignment for Vincit Rising Star program. Python application that analyzes historical cryptocurrency market data for a given date range. It is served as an API with few endpoints.

## Pre-requisites

Python >= 3.6 \
Docker >= 20.10

## Installation

### Virtual environment:

For development create and activate virtual environent:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements to venv:
```bash
pip install -r requirements.txt
```

Set env variables in .env:
```bash
FLASK_APP=main.py
FLASK_ENV=development/testing/production
```

Run the project:
```bash
flask run
```

### Docker:

Building the docker image:
```bash
docker build -t crypto_analyzer .
```

Running the image:
```bash
docker run -d -p 5000:5000 --name crypto_analyzer crypto_analyzer
```

## Usage

Head over to http://localhost:5000/ to see the API documentation. \
The app is also available online at: https://crpt-analyzer.herokuapp.com/

Please note that requests are limited to 50 calls/minute.

### Examples:

Longest downward trend that defaults to bitcoin and eur:
```
/api/downward_trend?from=2021-01-19&to=2021-05-20
```
Highest volume with another currency (jpy):
```
/api/highest_volume?vs_currency=jpy&from=2021-01-19&to=2021-05-20
```
Maximum profits with another coin (ethereum):
```
/api/max_profits?id=ethereum&vs_currency=usd&from=2021-01-19&to=2021-05-20
```
