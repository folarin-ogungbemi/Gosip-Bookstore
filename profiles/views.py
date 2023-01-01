from django.shortcuts import render
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from django.shortcuts import get_object_or_404


def profile_view(request):
    """Render the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
            'profile': profile,
            'form': form,
            'orders': orders
        }
    return render(request, "profiles/user_profile.html", context)
