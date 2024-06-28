from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm


# Create your views here.
class AddBooking(LoginRequiredMixin, CreateView):
    """ Add booking view """
    template_name = 'booking/add_booking.html'
    model = Booking
    form_class = BookingForm
    success_url = '/booking/booking_list/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBooking, self).form_valid(form)
