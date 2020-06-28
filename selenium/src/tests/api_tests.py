import pytest
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from ..data.urls import API_URL

schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "multiple articles",
    "type": "object",
    "properties": {
        "articles": {
            "type": "array",
            "properties": {
                "author": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string"
                        },
                        "bio": {
                            "type": "string"
                        },
                        "image": {
                            "type": "string"
                        },
                        "following": {
                            "type": "boolean"
                        }
                    }
                },
                "slug": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "body": {
                    "type": "string"
                },
                "tagList": {
                    "type": "array"
                },
                "createdAt": {
                    "type": "string"
                },
                "updatedAt": {
                    "type": "string"
                },
                "favorited": {
                    "type": "boolean"
                },
                "favoritesCount": {
                    "type": "number"
                }
            }
        },
        "articlesCount": {
            "type": "number"
        }
    }
}



def test_api():

    headers = {
        "Content-Type": "application/json"
    }
    r = requests.get(f'{API_URL}/api/articles?limit=10&offset=0', headers=headers)
    data = r.json()

    assert validate(data, schema) == None

    # with pytest.raises(ValidationError):
    #     validate(data, schema)
