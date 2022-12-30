from django.shortcuts import render
from django.views.generic import TemplateView


class UserProfile(TemplateView):
    template_name = 'profiles/user_profile.html'
