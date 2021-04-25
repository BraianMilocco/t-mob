from django.urls import path, include
# from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from .views import redirect

urlpatterns = [
    path('redirect/<key>/', redirect, name='redirect'),
]


