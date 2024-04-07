#help to keep payload ex from body
import faker
from faker import Faker
import json

def payload_create_booking():
    payload= {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
         "checkin": "2024-03-11",
         "checkout": "2024-03-13"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_booking_dynamic():
    payload= {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
         "checkin": "2024-03-11",
         "checkout": "2024-03-13"
        },
        "additionalneeds": faker.random_elements(elements=("Breakfast","Parking","wifi","Extra Bed"))
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

# def payload_create_booking_data_excel():
#     payload= {
#         "firstname": read_from_excel["first_name"],
#         "lastname": faker.last_name(),
#         "totalprice": faker.random_int(min=100, max=1000),
#         "depositpaid": faker.boolean(),
#         "bookingdates": {
#          "checkin": "2024-03-11",
#          "checkout": "2024-03-13"
#         },
#         "additionalneeds": faker.random_elements(elements=("Breakfast","Parking","wifi","Extra Bed"))
