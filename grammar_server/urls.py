from django.urls import path

from .Scripts.comman import text

urlpatterns = [
    path('hello/', text.hello),
]