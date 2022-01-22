import stripe

stripe.api_key = "sk_test_51KKgcdIZE0Muxk49q9EiryUY0HTWmKTchwHP7C24cn3c7epzs59OCYpI0lMJHUTfGb2cSfU5iqmzNxbutChQysWM00d7E33qTC"

session = stripe.checkout.Session.create(
    payment_method_types=["card"],
    line_items=[{
        "name": "Kavholm rental",
        "amount": 1000,
        "currency": "usd",
        "quantity": 1,
    }],
    payment_intent_data={
        "application_fee_amount": 123,
        "transfer_data": {
            "destination": "acct_1KKgfNROGsNq1D8b",  # acct_1KKgfNROGsNq1D8b
        },
    },
    mode="payment",
    success_url="https://example.com/success",
    cancel_url="https://example.com/failure",
)
