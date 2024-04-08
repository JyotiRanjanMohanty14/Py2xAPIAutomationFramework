# create Token
# create Booking Id
# update Booking(Put)-by booking id, Token
# delete the booking

# Task-verify that created booking id when we are able to update it and delete it also

# create token
# create booking
# test_update() ->concept
# fixtures-> pass the data in pytest

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class TestCRUDBooking(object):

    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(),
                                headers=Util.common_headers_json(),
                                auth=None,
                                payload=payload_create_token(),
                                in_json=False
                                )
        verify_http_status_code(respone_data=response, expect_data=200)
        verify_json_key_for_not_null(response.json()["token"])
        return response.json()["token"]

    @pytest.fixture()
    def get_booking_id(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util.common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        # actual_status_code = response.status_code

    @allure.title("Test CRUD operation Update(PUT)")
    @allure.description(
        "Verify that full update with booking ID and Token is working")
    def test_update_booking_id_token(self):
        pass

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description(
        "Verify booking gets deleted with booking ID and Token")
    def test_delete_booking_id(self):
        pass
