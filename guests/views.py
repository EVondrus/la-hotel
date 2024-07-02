from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

from .models import Profile
from .forms import ProfileForm

# Create your views here.

class Profiles(TemplateView):
    """ 
    Guest Profile view 
    Displays guest profile information
    """
    template_name = 'guests/profiles.html'
    
    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs['pk'])
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile)
        }

        return context

class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit Guest Profile """

    model = Profile
    form_class = ProfileForm

    def form_valid(self, form):
        form.save()  # Save the form
        # Add a success message
        messages.success(self.request, 'Your profile was successfully updated.')
        # Redirect to the profile view or success_url
        return redirect('guests:profile', pk=self.kwargs['pk'])

    def test_func(self):
        return self.request.user == self.get_object().user
    
