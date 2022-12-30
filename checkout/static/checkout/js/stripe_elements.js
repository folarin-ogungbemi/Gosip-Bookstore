/*
    Coe logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

    stripe Elements Docs:
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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
};

var card = elements.create('card', {style: style});
card.mount('#card-element');


// Handle realtime validation errors on the card element
card.addEventListener('change', function (event){
    var erDiv = document.getElementById('card-errors');
    if (event.error){
        var html = 
                `<span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>`
        ;
        $(erDiv).html(html);
    } else {
        erDiv.textContent = '';
    }
});


// Handle form submit
var form = document.getElementById('complete-order');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#transact').attr('disabled', true);
    $('#complete-order').fadeToggle(100);
    $('#loader').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'))
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    }
    var url = '/checkout/cache_checkout_data/';
    $.post(url, postData).done(function(){
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.address_line_1.value),
                        line2: $.trim(form.address_line_2.value),
                        postal_code: $.trim(form.zip.value),
                        city: $.trim(form.city.value),
                        state: $.trim(form.state.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.address_line_1.value),
                    line2: $.trim(form.address_line_2.value),
                    postal_code: $.trim(form.zip.value),
                    city: $.trim(form.city.value),
                    state: $.trim(form.state.value),
                    country: $.trim(form.country.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var erDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(erDiv).html(html);
                $('#complete-order').fadeToggle(100);
                $('#loader').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#transact').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function(){
        // just reload the page, the error will be in django messages
        location.reload();
    })
});