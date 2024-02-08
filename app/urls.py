from django.urls import path
from . import views

urlpatterns = [
    path('kontakti', views.kontakti_view, name='kontakti'),
    path('', views.index, name='index'),
    path('testo', views.testo, name='testo'),
]
