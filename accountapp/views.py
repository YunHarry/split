from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, CustomUserCreationForm
from accountapp.models import Registration


# Create your views here.

def hello_world(request):
    #POST request
    if request.method == "POST":
        temp = request.POST.get('email')
        reg_all = Registration.objects.all()
        return render(request, "accountapp/hello_world.html",
                      context={"temp": temp,
                               "reg_all": reg_all})

    #GET request
    temp = "split"
    return render(request, "accountapp/hello_world.html",
                  context={"temp": temp})

class AccountCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/create.html"

class AccountLoginView(LoginView):
    template_name = "accountapp/login.html"

class AccountLogoutView(LogoutView):
    pass

class AccountDetailView(DetailView):
    model = User
    template_name = "accountapp/detail.html"
    context_object_name = "target_user"

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    template_name = "accountapp/update.html"
    context_object_name = "target_user"

    def get_success_url(self):
        return reverse("accountapp:detail", kwargs={"pk": self.kwargs["pk"]})

class AccountDeleteView(DeleteView):
    model = User
    template_name = "accountapp/delete.html"
    context_object_name = "target_user"
    success_url = reverse_lazy("accountapp:hello_world")