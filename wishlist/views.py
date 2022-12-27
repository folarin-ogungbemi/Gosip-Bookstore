from django.shortcuts import render


def wishlist_view(request):
    """ function renders wishlist view """
    # context = {
    #     'wishes': wishes,
    # }
    return render(request, 'wishlist/wish.html')
