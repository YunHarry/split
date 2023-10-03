from accountapp.views import hello_world
from django.urls import path

appname = 'accountapp'

urlpatterns = [
    path("hello_world/", hello_world),
]