from django.shortcuts import render


def index(request):
    """ A view to render the home page """
    return render(request, 'home/index.html')


def about(request):
    """ A view to render the about page """
    return render(request, 'home/about.html')


def team(request):
    """ A view to render the team page """
    return render(request, 'home/team.html')
