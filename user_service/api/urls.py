from django.urls import path
from api.views import CreateUser

urlpatterns = [
    path('create-user/', CreateUser.as_view())
]
