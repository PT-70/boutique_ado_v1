from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def__init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Hancle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received:{event["type"]}',
        status=200)