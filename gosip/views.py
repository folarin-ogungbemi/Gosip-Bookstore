# django error-page documentation
# https://docs.djangoproject.com/en/3.2/ref/exceptions/#resolver404
# https://docs.djangoproject.com/en/3.2/topics/http/views/#customizing-error-views
from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)
