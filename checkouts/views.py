from django.shortcuts import render
from checkouts.process import generate_client_token, transact, find_transaction
# from checkouts.process import *
from django.shortcuts import render, redirect
import braintree
# Create your views here.



TRANSACTION_SUCCESS_STATUSES = [
    braintree.Transaction.Status.Authorized,
    braintree.Transaction.Status.Authorizing,
    braintree.Transaction.Status.Settled,
    braintree.Transaction.Status.SettlementConfirmed,
    braintree.Transaction.Status.SettlementPending,
    braintree.Transaction.Status.Settling,
    braintree.Transaction.Status.SubmittedForSettlement
]


def new_checkout(request):
    client_token = generate_client_token()
    return render(request, 'checkouts/new.html', {"client_token":client_token})