from helper import spi_constant


def get_user(user):
    if user == "admin":
        return spi_constant.USER_ADMIN['user']
    elif user == "otrouser":
        return spi_constant.USER_REEMPLAZO['user']

def get_pass(user):
    if user == "admin":
        return spi_constant.USER_ADMIN['password']
    elif user == "otrouser":
        return spi_constant.USER_REEMPLAZO['password']