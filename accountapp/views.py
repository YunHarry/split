from django.http import HttpResponse
from django.shortcuts import render

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