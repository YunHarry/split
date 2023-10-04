from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
    form_class = UserCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "accountapp/create.html"