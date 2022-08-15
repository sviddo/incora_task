from .models import User

def get_user_data(user: User):
    user_data = {}
    user_data['first_name'] = user.first_name
    user_data['last_name'] = user.last_name
    user_data['email'] = user.email
    user_data['phone'] = str(user.phone)

    return user_data


class CustomException(Exception):
    """custom exception class"""