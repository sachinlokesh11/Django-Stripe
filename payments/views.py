from django.views.generic.base import TemplateView
from django.shortcuts import render
import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Configure the Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


stripe.api_key = settings.STRIPE_SECRET_KEY  # new


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):  # new
    # if request.method == 'POST':
    #     charge = stripe.Charge.create(
    #         amount=500,
    #         currency='usd',
    #         description='A Django charge',
    #         source=request.POST['stripeToken']
    #     )
    try:
        charge = stripe.Charge.create(
            amount=500,
            currency="inr",
            description='A Django charge',
            source="tok_mastercard",
            metadata={'order_id': '6735'},
            idempotency_key='sSLwex2yaSVbiPyx'


        )

    except stripe.error.CardError as e:
        # Problem with the card
        return HttpResponse(e)

    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        return HttpResponse(e)
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe API
        return HttpResponse(e)

    except stripe.error.AuthenticationError as e:
        # Authentication Error: Authentication with Stripe API failed (maybe you changed API keys recently)
        return HttpResponse(e)

    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        return HttpResponse(e)

    except stripe.error.StripeError as e:
        # Stripe Error
        return HttpResponse(e)

    else:
        return render(request, 'charge.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers['Stripe-Signature']

    # Verify the signature
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        # Payment succeeded event
        payment_intent = event['data']['object']
        # Process the successful payment, update database, send confirmation email, etc.
        print("Payment succeeded for payment_intent:", payment_intent['id'])
    elif event['type'] == 'customer.subscription.deleted':
        # Subscription canceled event
        subscription = event['data']['object']
        # Handle subscription cancellation, update database, notify user, etc.
        print("Subscription canceled for subscription:", subscription['id'])
    # Add more event handlers as needed for other types of events

    # Return a success response
    return HttpResponse(status=200)
