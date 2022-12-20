/*
    Coe logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

    CSS from here:
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        color: '#022138',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '14px',
        '::placeholder': {
            color: 'rgba(2, 33, 56, 0.5)'
        }
    },
    invalid: {
        color: '#f02c2c',
        iconColor: '#f02c2c'
    }
}

var card = elements.create('card', {style: style});
card.mount('#card-element');