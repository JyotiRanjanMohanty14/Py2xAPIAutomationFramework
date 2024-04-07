# APIConstants- Class which contain all the endpoints.
# Keep the URLs
# Concepts
# Static Method-which can be called by without the object directly by using class you can call it

class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com/"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking/"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # update,PUT,PATCH,DELETE-bookingId

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
