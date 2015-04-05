from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View


from base.mixins import LoginRequiredMixin


from landing.forms import SignInForm


class LandingView(View):
    template_name = 'landing/landing.html'

    def get(self, request):
        return render(request, self.template_name)


class SignInView(View):
    form_class = SignInForm
    template_name = 'landing/signin.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect(reverse('home'))
        return render(request, self.template_name, {'form': form})


class SignOutView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated():
            logout(request)
        return HttpResponseRedirect(reverse('landing'))

