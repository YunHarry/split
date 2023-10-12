from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from profileapp.forms import ProfileForm
from profileapp.models import Profile


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profileapp/create.html'

    def get_success_url(self):
        return reverse('accountapp:detail',
                       kwargs={'pk':self.kwargs["pk"]})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)