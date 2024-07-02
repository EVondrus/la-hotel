from django.views.generic import TemplateView
from .models import Profile

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
            'profile': profile
        }
        return context
