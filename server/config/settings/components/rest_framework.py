"""Rest framework settings"""

DATE_INPUT_FORMATS = [
    ("%d-%m-%Y"),
    ("%d.%m.%Y"),
    ("%d/%m/%Y"),
    "iso-8601",
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication', )
}

CORS_ORIGIN_ALLOW_ALL = True
