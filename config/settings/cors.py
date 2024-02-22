CORS_ALLOWED_ORIGINS = [
    "https://vbg-hotels.club",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
]
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CSRF_COOKIE_SECURE = False
