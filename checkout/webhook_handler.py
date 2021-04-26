from django.http import HttpResponse

# From Boutique Ado project


class StripeWH_Handler:
    """
    Handles Stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)