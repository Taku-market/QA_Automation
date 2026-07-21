import os

ENVIRONMENTS = {
    "staging": "https://jsonplaceholder.typicode.com",
    "production": "https://jsonplaceholder.typicode.com"
}

ENV = os.getenv("TEST_ENV", "staging")
BASE_URL = ENVIRONMENTS[ENV]