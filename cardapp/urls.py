from django.urls import path, include
from .views import provideCardDetails


urlpatterns = [
    path('', provideCardDetails, name = "cardlink")
]