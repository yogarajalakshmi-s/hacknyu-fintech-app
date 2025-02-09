from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PaymentForm
from .models import Payment
from django.contrib.auth.decorators import login_required
import random
import string


@login_required
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            card_number = form.cleaned_data['card_number']
            card_expiry = form.cleaned_data['card_expiry']
            card_cvc = form.cleaned_data['card_cvc']

            if len(card_number) == 16 and len(card_expiry) == 5 and len(card_cvc) == 3:
                transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                status =  random.choice(['success', 'failed'])

                payment = Payment(
                    user=request.user,
                    amount=amount,
                    payment_method='Credit Card',
                    status=status,
                    transaction_id=transaction_id
                )
                payment.save()

                messages.success(request, f"Payment of {amount} was successful. Transaction ID: {transaction_id}")
                return redirect('expenses')
            else:
                messages.error(request, "Invalid card details. Please check your card information.")
    else:
        form = PaymentForm()

    return render(request, 'payments/make_payment.html', {'form': form})

@login_required
def view_expenses(request):
    payments = Payment.objects.filter(user=request.user).order_by('-date')
    return render(request, 'payments/expenses.html', {'payments': payments})
