# class or functions(keep as like class or functions)

class Util(object):
    @staticmethod
    def common_headers_json():
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    @staticmethod
    def common_headers_xml():
        headers = {
            "Content-Type": "application/xml"
        }
        return headers

    def common_header_put_patch_delete_basic_auth(basic_auth_value):
        headers = {
            "Content-Type": "application/xml",
            "Authorization": "BasicAuth" + str(basic_auth_value),
        }
        return headers

    def common_header_put_delete_patch_cookie(self, token):
        headers = {
            "Content-Type": "application/xml",
            "Cookie": "token=" + str(token),
        }
        return headers

    # for future keep all common utilities
    def read_csv_file(self):
        pass

    def read_env_file(self):
        pass

    def read_database(self):
        pass

# util = Util().common_headers_json() create object then call
