from django.urls import path
from .views import (
    create_user,
    login,
    SingleUser,
)

urlpatterns = [
    path('users', create_user, name='create-user'),
    path('login', login, name='login'),
    path('users/<int:id>', SingleUser.as_view(), name='single-user'),
]
