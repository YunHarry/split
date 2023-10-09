from accountapp.views import hello_world, AccountCreateView, AccountLoginView, AccountLogoutView, AccountDetailView, \
    AccountUpdateView, AccountDeleteView
from django.urls import path

app_name = 'accountapp'

urlpatterns = [
    path("hello_world/", hello_world, name="hello_world"),
    path("create/", AccountCreateView.as_view(), name="create"),
    path("login/", AccountLoginView.as_view(), name="login"),
    path("logout/", AccountLogoutView.as_view(), name="logout"),

    path("detail/<int:pk>", AccountDetailView.as_view(), name="detail"),
    path("update/<int:pk>", AccountUpdateView.as_view(), name="update"),
    path("delete/<int:pk>>", AccountDeleteView.as_view(), name="delete"),
]