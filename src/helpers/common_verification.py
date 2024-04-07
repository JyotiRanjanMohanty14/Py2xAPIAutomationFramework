def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Expected HTTP Status Code/Failed ER!=AR" + str(expect_data)


def verify_json_key_for_not_null(key):
    assert key != 0, "Failed - Key is non Empty" + key
    assert key > 0, "Failed - Key is grater than zero"


def verify_response_key_should_not_be(key):
    assert key is not None

# this func used for bookingid
# add common utilities
# common verifiction
# http status code
# header
# Data verifiaction
# JSON schema  and write more fuction from response body of create booking to check bookinid not null
