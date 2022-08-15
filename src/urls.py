from django.urls import path
from .views import (
    create_user,
    get_user,
)

urlpatterns = [
    path('users', create_user, name='create-user'),
    path('users/<int:id>', get_user, name='get-user'),
]
