from django.http import HttpResponse


class StripeWH_Handler:
    """ Handles Stripe webhooks"""
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ handles a generic/unknown/unexpectedly webhook event"""
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_payment_succeeded(self, event):
        """ handles a successful webhook event"""
        intent = event.data.object
        print(f"successful attempt{intent}")
        return HttpResponse(
            content=f"webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ handles a failed webhook event"""
        intent = event.data.object
        print(f"failed attempt{intent}")
        return HttpResponse(
            content=f"Payment failed webhook received: {event['type']}",
            status=200)
