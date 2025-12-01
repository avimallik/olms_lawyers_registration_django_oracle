from django.urls import path
from .views import insert_test_input

urlpatterns = [
    path('insert/', insert_test_input, name='insert_test_input'),
]