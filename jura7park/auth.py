from social_core.backends.oauth import BaseOAuth2
from urllib.parse import urlencode
import jwt

class ChurrosAuthentik(BaseOAuth2):
    name = 'churros'
    AUTHORIZATION_URL = 'https://auth.inpt.fr/application/o/authorize/'
    ACCESS_TOKEN_URL = 'https://auth.inpt.fr/application/o/token/'
    USER_INFO_URL = 'https://auth.inpt.fr/application/o/userinfo/'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('openid:', 'openid'),
        ('profile', 'profile'),
        ('preferred_username','preferred_username')
    ]

    def get_user_details(self, response):
        access_token = response.get('access_token')
        id_token = response.get('id_token')
        user_info = jwt.decode(id_token, options={"verify_signature": False})
        print(user_info)
        return {
            'username': user_info.get('preferred_username'),
            'email': user_info.get('preferred_username'),
            "access_token" : access_token }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        print("USER DATA")
        return {}
