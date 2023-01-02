from django.shortcuts import render
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from checkout.models import Order
from django.shortcuts import get_object_or_404
from django.contrib import messages


def profile_view(request):
    """
    Render the user's profile view, order history and
    allow user to update their data.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your profile has been updated successfully')

    context = {
            'profile': profile,
            'form': form,
            'orders': orders,
            'on_profile_page': True,
        }
    return render(request, "profiles/user_profile.html", context)


def order_history(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/transact_success.html', context)
