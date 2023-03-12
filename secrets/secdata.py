import datetime
ALLOWED_HOSTS = [
    '*',
]

SECRET_KEY = 'super_seceret_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
AUTHORISATION_ON = False

AUTH_CODE_CLEAR_TIME = 1800 # in seconds
LOGIN_FRONTEND_EXPIRATION = 30 # in minutes

# mainUrl ='http://127.0.0.1:8000/'
mainUrl ='https://api-dev.webgtx.com/'
# mainUrl ='http://localhost:8084/'
# pictureUrl = 'http://127.0.0.1:8084/media/'
pictureUrl = 'https://api-dev.webgtx.com/media/'
url = mainUrl+'graphql/'


DATABASES = {
    #  'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'webgtx_dev',
    #     'USER': 'postgres',
    #     'PASSWORD': 'super_password',
    #     'HOST': 'webgtx-dev.ckozg832cfih.us-east-2.rds.amazonaws.com',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'webgtx',
        'USER': 'postgres',
        'HOST': '10.0.0.111',
    }
}

GRAPHQL_JWT = {
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
    ],
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": datetime.timedelta(minutes=LOGIN_FRONTEND_EXPIRATION),
}
