# Constants-

# Add your constants here

# BASE_URL = "https://restful-booker.herokuapp.com"
#
#
# def base_url():
#     return "https://restful-booker.herokuapp.com"


'''
def base_usr() :
    return "https://restful-booker.herokuapp.com"

def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking/"

def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"

#update, PUT, PATCH, DELETE -booking id

def url_patch_put_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
'''


class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # Update, PUT, PATCH, DELETE -booking id
    def url_patch_put_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)