from django.conf import settings
from django.urls import reverse
from django.views.generic.base import RedirectView


class MainRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if settings.DEBUG or self.request.user.is_staff:
            url = reverse("admin:index")
        else:
            url = settings.MAIN_REDIRECT_URL

        return url
