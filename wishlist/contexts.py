from django.shortcuts import get_object_or_404
from books.models import Books


def wish_list(request):
    books_liked = []
    like_count = 0

    wishlist = request.session.get('wishlist', {})

    for slug, val in wishlist.items():
        book = get_object_or_404(Books, slug=slug)
        books_liked.append({
            'book': book,
            'slug': slug})
        like_count = len(books_liked)
    return {
        'books_liked': books_liked,
        'like_count': like_count,
    }
