from django.shortcuts import render, redirect
from .forms import CustomerForm

def create_account(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return render(request, 'accounts/success.html', {'account_number': customer.account_number})
    else:
        form = CustomerForm()
    return render(request, 'accounts/create_account.html', {'form': form})
