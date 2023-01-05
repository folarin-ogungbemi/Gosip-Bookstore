from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect


def wishlist_view(request):
    """ function renders wishlist view """
    return render(request, 'wishlist/wish.html')


def like_book(request, slug):
    """ Add wish item to wishlist"""

    # check if likes dict exist else create
    wishlist = request.session.get('wishlist', {})
    # redirects to the current page
    redirect_url = request.POST.get('redirect_url')

    if slug not in list(wishlist.keys()):
        wishlist[slug] = slug
    elif slug in list(wishlist.keys()):
        wishlist.pop(slug)
    request.session['wishlist'] = wishlist
    return redirect(redirect_url)


def remove_book(request, slug):
    """ Returning a liked item from the wishlist """
    try:
        wishlist = request.session.get('wishlist', {})
        wishlist.pop(slug)

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as error:
        return HttpResponse(status=500)
