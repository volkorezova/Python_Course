import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

# Logging to the file and to the console
logger = logging.getLogger("cars_tests")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log")
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# loging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )
    assert response.status_code == 200, "Authentication failed"
    token = response.json()["access_token"]
    session.headers.update({
        "Authorization": f"Bearer {token}"
    })
    return session


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 4),
    ("brand", 6),
    ("price", 10),
    ("year", 2),
])

class TestCarsAPI:
    # get cars
    def test_get_cars(self, auth_session, sort_by, limit):
        params = {
            "sort_by": sort_by,
            "limit": limit
        }

        response = auth_session.get(f"{BASE_URL}/cars", params=params)

        logger.info(f"Request params: {params}")
        logger.info(f"Status: {response.status_code}")

        # assert on status code
        assert response.status_code == 200

        data = response.json()
        logger.info(f"Response: {data}")

        # assert for structure of car object
        for car in data:
            assert "brand" in car
            assert "year" in car
            assert "engine_volume" in car
            assert "price" in car

        # sorting check
        if sort_by in ["price", "year", "engine_volume", "brand"]:
            values = [car[sort_by] for car in data]
            assert values == sorted(values)