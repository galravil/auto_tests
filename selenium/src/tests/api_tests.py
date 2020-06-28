import pytest
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from ..utils.assertions import validate_schema
from ..data.urls import API_URL


def test_api():
    headers = {
        "Content-Type": "application/json"
    }
    r = requests.get(f'{API_URL}/api/articles?limit=10&offset=0', headers=headers)
    data = r.json()

    # in case of succesfull validation returns None, otherwise ValidationError
    assert validate_schema(data, 'articles.json') == None

    # with pytest.raises(ValidationError):
    #     validate(data, schema)
