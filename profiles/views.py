from django.shortcuts import render
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from django.shortcuts import get_object_or_404
from django.contrib import messages


def profile_view(request):
    """Render the user's profile"""
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
