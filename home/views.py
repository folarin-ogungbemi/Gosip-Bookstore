from django.shortcuts import render, reverse
from django.views.generic.edit import FormView
from home.forms import ContactForm
from django.http import HttpResponseRedirect


def index(request):
    """ A view to render the home page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to render the about page """
    return render(request, 'home/about.html')


def team(request):
    """ A view to render the team page """
    return render(request, 'home/team.html')


class ContactView(FormView):
    """
    Class renders Contact form view and
    allow users to send message
    """
    template_name = 'home/contact.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contact'))
