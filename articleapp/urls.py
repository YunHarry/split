from django.urls import path

from articleapp.views import TempView

app_name = "articleapp"

urlpatterns = [
    path("temp/", TempView.as_view(), name="temp"),
]