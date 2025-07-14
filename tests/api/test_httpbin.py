import json
import os

import pytest
import requests


def load_test_cases():
    case_path = os.path.join(
        os.path.dirname(__file__), "cases_test_api_httpbin.json"
    )
    with open(case_path, "r") as f:
        return json.load(f)


@pytest.mark.parametrize("test_case", load_test_cases())
def test_httpbin(test_case):
    endpoint = test_case["endpoint"]
    expected_status_code = test_case["expected_status_code"]
    url = f"https://httpbin.org{endpoint}"
    response = requests.get(url)
    print(f"Testing {url} with expected status code {expected_status_code}")
    assert response.status_code == expected_status_code, (
        f"Expected {expected_status_code}, got {response.status_code}"
    )
