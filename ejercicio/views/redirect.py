from django.http import JsonResponse
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.core.cache import cache

from ..models import Redirect

@require_http_methods(["GET"])
def redirect(request, key):
    data = get_from_cache(key)
    if data:
        return  JsonResponse(data, content_type="application/json")
    else:
        raise Http404

def get_from_cache(key):
    url = cache.get(key)
    if url:
        return { 'key': key, 'url': url}
    return None