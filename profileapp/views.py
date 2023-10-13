from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
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

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail',
                       kwargs={'pk':self.request.user.pk})