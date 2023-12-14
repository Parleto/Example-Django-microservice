from django.http import JsonResponse
from django.urls import path
from django.utils.translation import (
    activate,
    get_language_from_request,
    gettext_lazy as _,
)


def index(request):
    data = dict(content='', errorList=[])

    # TODO: consider using middleware for this
    activate(get_language_from_request(request))

    if request.POST:
        data['errorList'].append(_('ERROR'))
    else:
        data['content'] = _('OK')

    return JsonResponse(data)


urlpatterns = [
    path('', index),
]
