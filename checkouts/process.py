from django.conf import settings
import os
import braintree

 
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        # environment=settings.BT_ENVIRONMENT,
        # merchant_id=settings.BT_MERCHANT_ID,
        # public_key=settings.BT_PUBLIC_KEY,
        # private_key=settings.BT_PRIVATE_KEY,
        environment='sandbox',
        merchant_id='snz94bz69xrtysfw',
        public_key='9h8v24t83g2dyh4x',
        private_key='9981ac0e29e5d113a063a993592ac463'
    )
)

def generate_client_token():
    return gateway.client_token.generate()

def transact(options):
    return gateway.transaction.sale(options)

def find_transaction(id):
    return gateway.transaction.find(id)
