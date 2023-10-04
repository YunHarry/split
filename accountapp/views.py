from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    #POST request
    if request.method == "POST":
        temp = request.POST.get('email')
        return render(request, "accountapp/hello_world.html",
                      context={"temp": temp})

    #GET request
    temp = "split"
    return render(request, "accountapp/hello_world.html",
                  context={"temp": temp})