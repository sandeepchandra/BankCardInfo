
from django.urls import path, include
from .views import CardAPIView


urlpatterns = [
    path('<str:id>/', CardAPIView.as_view(), name = "cardAPI")
]