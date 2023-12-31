# from src.constants.api_constants import BASE_URL, APIConstants, base_url
import json
import os

import pytest
import self
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    def test_create_booking_jsonschema(self):
        # URL, Headers, Payload,

        payload = payload_create_booking()
        print(payload)
        # payload.update({"firstname: "milind","lastname:"trivedi})
        payload["firstname"] = "Jim"
        print(payload)

        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload, in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        response_json = response.json()

        #file = os.getcwd() + "/schema.json"
        #print(file)
        #schema = self.load_schema("file")
        #print(schema)

        schema = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "title": "Root Schema",
    "type": "object",
    "required": [
        "bookingid",
        "booking"
    ],
    "properties": {
        "bookingid": {
            "title": "The bookingid Schema",
            "type": "integer",
            "examples": [
                2377
            ]
        },
        "booking": {
            "title": "The booking Schema",
            "type": "object",
            "required": [
                "firstname",
                "lastname",
                "totalprice",
                "depositpaid",
                "bookingdates",
                "additionalneeds"
            ],
            "properties": {
                "firstname": {
                    "title": "The firstname Schema",
                    "type": "string",
                    "examples": [
                        "Jim"
                    ]
                },
                "lastname": {
                    "title": "The lastname Schema",
                    "type": "string",
                    "examples": [
                        "Breakfast"
                    ]
                },
                "totalprice": {
                    "title": "The totalprice Schema",
                    "type": "integer",
                    "examples": [
                        111
                    ]
                },
                "depositpaid": {
                    "title": "The depositpaid Schema",
                    "type": "boolean",
                    "examples": [
                        True
                    ]
                },
                "bookingdates": {
                    "title": "The bookingdates Schema",
                    "type": "object",
                    "required": [
                        "checkin",
                        "checkout"
                    ],
                    "properties": {
                        "checkin": {
                            "title": "The checkin Schema",
                            "type": "string",
                            "examples": [
                                "2018-01-01"
                            ]
                        },
                        "checkout": {
                            "title": "The checkout Schema",
                            "type": "string",
                            "examples": [
                                "2019-01-01"
                            ]
                        }
                    },
                    "examples": [{
                        "checkin": "2018-01-01",
                        "checkout": "2019-01-01"
                    }]
                },
                "additionalneeds": {
                    "title": "The additionalneeds Schema",
                    "type": "string",
                    "examples": [
                        "Breakfast"
                    ]
                }
            },
            "examples": [{
                "firstname": "Jim",
                "lastname": "Breakfast",
                "totalprice": 111,
                "depositpaid": True,
                "bookingdates": {
                    "checkin": "2018-01-01",
                    "checkout": "2019-01-01"
                },
                "additionalneeds": "Breakfast"
            }]
        }
    },
    "examples": [{
        "bookingid": 2377,
        "booking": {
            "firstname": "Jim",
            "lastname": "Breakfast",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    }]
}
        print(schema)
        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            print(e.message)

