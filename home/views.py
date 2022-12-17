from django.shortcuts import render
from django.views.generic.edit import FormView
from home.forms import ContactForm


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
