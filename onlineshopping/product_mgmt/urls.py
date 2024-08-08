from django.urls import path
from .views import*

urlpatterns = [
    path('items/', CreateItem.as_view()),
]
