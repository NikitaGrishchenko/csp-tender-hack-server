import typing

from django.http import HttpRequest
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import BaseHasAPIKey


class HasApiKeyOrIsAdmin(BaseHasAPIKey):
    model = APIKey

    def has_permission(self, request: HttpRequest, view: typing.Any) -> bool:
        assert self.model is not None, (
            "%s must define `.model` with the API key model to use"
            % self.__class__.__name__
        )
        key = self.get_key(request)
        if not key:
            if bool(request.user and request.user.is_staff):
                return True
            return False
        return self.model.objects.is_valid(key)
