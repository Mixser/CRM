from django.core.urlresolvers import reverse

from django.shortcuts import render
from django.views.generic import View, UpdateView
from base.forms import EmployerUpdateForm
from base.mixins import LoginRequiredMixin
from base.models import Employer, Event


class HomeView(LoginRequiredMixin, View):
    template_name = 'base/home.html'

    def get(self, request):
        return render(request, self.template_name)


class ScheduleView(LoginRequiredMixin, View):
    template_name = 'base/schedule.html'

    def get(self, request):
        schedule = request.user.schedule

        events = schedule.events.all()

        return render(request, self.template_name, {'events': events})


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event

class EmployerUpdateView(LoginRequiredMixin, UpdateView):
    model = Employer
    form_class = EmployerUpdateForm
    fields = ['first_name', 'last_name', 'email']
    template_name = 'base/employer/edit_employer_form.html'

    def get_success_url(self):
        return reverse('home')
