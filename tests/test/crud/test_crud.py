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
from src.helpers.api_requests_wrapper import *
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
        verify_json_key_for_not_null_token(response.json()["token"])
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
        return booking_id

        # actual_status_code = response.status_code

    @allure.title("Test CRUD operation Update(PUT)")
    @allure.description(
        "Verify that full update with booking ID and Token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_request(
            url=put_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        # print(response.json())
        # Verification here & more(after done remove delete request)
        verify_json_key_for_not_null(response.json()["firstname"])
        verify_response_key(response.json()["firstname"], expected_data="Amit")
        verify_response_key(response.json()["lastname"], expected_data="Brown")
        verify_json_key_for_not_null(response.json()["lastname"])
        verify_http_status_code(response_data=response, expect_data=200)

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description(
        "Verify booking gets deleted with booking ID and Token")
    def test_delete_booking_id(self,create_token,get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_request(
            url=delete_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        print(response.text)
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expect_data=201)

