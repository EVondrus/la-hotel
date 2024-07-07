from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from allauth.account.views import SignupView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth import logout

from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404

from .models import Profile
from .forms import ProfileForm
from .forms import CustomSignupForm


# Create your views here.
class CustomSignup(SignupView):
    """ Custom Signup view """
    template_name = 'allauth/account/signup.html'
    form_class = CustomSignupForm
    success_url = reverse_lazy('account_login')

    def form_valid(self, form):
        """Handle successful form submission."""
        messages.success(
            self.request, 'Your account has been created. You can now log in.'
        )
        return super().form_valid(form)


    def form_invalid(self, form):
        """Handle invalid form submission."""
        messages.error(
            self.request,
            'There was an error with your submission. Please try again.'
        )
        return super().form_invalid(form)



class Profiles(TemplateView):
    """  
    Displays guest profile information
    """
    template_name = 'guests/profiles.html'
    
    def get_context_data(self, **kwargs):
        """Get the guest profile information."""
        user_id = self.kwargs.get('pk')
        profile = get_object_or_404(Profile, user=user_id)
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
        """Handle successful form submission."""
        self.success_url = f'/profiles/profile/{self.kwargs["pk"]}/'
        messages.success(self.request, 'Your profile was successfully updated.')
        return super().form_valid(form)

    def test_func(self):
        """Ensure user can only edit their own profile."""
        return self.request.user == self.get_object().user


class DeleteProfile(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Deletes the user's profile and related bookings
    and logs them out of the system.
    """
    model = Profile
    template_name = 'allauth/account/delete_profile.html'
    success_url = reverse_lazy('home') 

    def test_func(self):
        """Ensure user can only delete their own profile."""
        return self.request.user == self.get_object().user


    def form_valid(self, form):
        """Handle successful deletion."""
        messages.success(self.request, 'Your account has been permanently \
        deleted, including all related bookings. Welcome back anytime!')

        # Delete the user's account and related bookings
        self.request.user.delete()

        # Log out the user
        logout(self.request)

        # Redirect to the home page 
        return HttpResponseRedirect(reverse('home'))