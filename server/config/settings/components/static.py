"""Static settings"""

from .paths import (
    PUBLIC_MEDIA_DIR,
    PUBLIC_STATIC_DIR,
    STATIC_DIR,
    WEBPACK_STATS_FILE,
)

STATIC_URL = "/static/"
STATIC_ROOT = PUBLIC_STATIC_DIR

STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_ROOT = PUBLIC_MEDIA_DIR
MEDIA_URL = "/media/"


WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "dist/",
        "STATS_FILE": WEBPACK_STATS_FILE,
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}

# TODO: настроить или удалить
# STATICFILES_STORAGE = (
#     "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
# )
