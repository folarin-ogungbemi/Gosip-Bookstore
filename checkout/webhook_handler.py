"""
Listen for signals when a payment is created or completed.
webhook will be sent to the specified URL address-url/checkout/wh/

The init method is called everytime an instance of the class is created.
The event handler indicates whether event was received. We create a response
for successful and failed attempts
"""

from django.http import HttpResponse

# To send confirmation email
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from django.shortcuts import get_object_or_404

# import models from loacal App
from checkout.models import Order, OrderSet
from books.models import Books
from profiles.models import UserProfile

# To work with stripe
import json
import time
import stripe


class StripeWH_Handler:
    """
    Handles Stripe webhooks
    """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):
        """
        Handles a generic/unknown/unexpectedly webhook event.
        """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles a successful webhook event
        """
        # store payment intent from the event
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount/100, 2)

        # clean data in the shipping details by
        # replacing empty strings with none to match null in db
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None
        
        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.user_phone_number = shipping_details.phone,
                profile.user_address_line_1 = shipping_details.address.line1,
                profile.user_address_line_2 = shipping_details.address.line2,
                profile.user_zip = shipping_details.address.postal_code,
                profile.user_city = shipping_details.address.city,
                profile.user_state = shipping_details.address.state,
                profile.user_country = shipping_details.address.country,
                profile.save()
                print(profile)

        # check existence of order
        order_exist = False
        # take care of same order being added twice to db if there is
        # a delay in view.
        # we delay order creation as opposed to immediate creation.
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    phone_number__iexact=shipping_details.phone,
                    email__iexact=billing_details.email,
                    address_line_1__iexact=shipping_details.address.line1,
                    address_line_2__iexact=shipping_details.address.line2,
                    zip__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    state__iexact=shipping_details.address.state,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                    )
                order_exist = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exist:
            # send email to user
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'webhook received: {event["type"]} | SUCCESS: verified order already in db',
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    phone_number=shipping_details.phone,
                    email=billing_details.email,
                    address_line_1=shipping_details.address.line1,
                    address_line_2=shipping_details.address.line2,
                    zip=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    state=shipping_details.address.state,
                    country=shipping_details.address.country,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,)

                # load cart from payment intent
                print(f'cart')
                for slug, qty in json.loads(cart).items():
                    book = Books.objects.get(slug=slug)
                    if isinstance(qty, int):
                        order_set = OrderSet(
                            order=order,
                            book=book,
                            quantity=qty,)
                        order_set.save()
                        Order.objects.filter(
                                order_id=str(order)).update(concluded=True)
            except Exception as error:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f"webhook received: {event['type']} | ERROR: {error}",
                    status=500)
        # send email to user if order was created by the webhook handler
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f"webhook received: {event['type']} | SUCCESS: Created order in webhook",
            status=200)

    def handle_payment_intent_failed(self, event):
        """ handles a failed webhook event"""
        return HttpResponse(
            content=f"webhook received: {event['type']}",
            status=200)