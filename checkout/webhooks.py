from django.conf import settings
from django.http import HttpResponse
import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler
import stripe


@require_POST
@csrf_exempt
def my_webhook_view(request):
    """Listens for webhooks from Stripe """
    payload = request.body
    event = None

    # setup
    wh_secret = settings.STRIPE_WEBHOOK_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Handle the event

    print('success')
    return HttpResponse(status=200)
