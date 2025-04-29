from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .models import Customer
from .forms import CustomerForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, timedelta


# Create your views here.

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer_list.html',{'customers': customers})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer Added Successfully👍')
            return redirect('customer_list')
        
  
    else:
        form = CustomerForm()

    return render(request, 'crm/add_customer.html', {'form': form})

@login_required
def edit_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer Updated Successfully👌')
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'crm/edit_customer.html', {'form': form, 'customer': customer})


@login_required
def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'POST':
        customer.delete()
        messages.info(request, 'Customer Deleted🗑️')
        return redirect('customer_list')

    return render(request, 'crm/delete_customer.html', {'customer': customer})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Welcome Customer,Hope Our Services will Satsify Your Needs😊')
            return redirect('home')
        else:
            messages.error(request, 'Recheck the Form, Something might have gone wrong🤔')    
    else:
        form = RegisterForm()
        return render(request, 'crm/register.html', {'form': form})



class CustomLoginView(LoginView):
    def form_valid(self, form):
        messages.success(self.request, 'You are Logged In😎')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Check Your Credentials😊')
        return super().form_invalid(form)

    template_name='crm/login.html'


def logout_view(request):
    logout(request)
    return redirect('login')


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'crm/customer_detail.html',{'customer': customer})

@login_required
def dashboard(request):
    # Total customers
    total_customers = Customer.objects.count()

    # Active members (those whose membership is still valid)
    active_members = Customer.objects.filter(membership_end_date__gte=date.today()).count()

    # Expired memberships (those whose membership has expired)
    expired_memberships = Customer.objects.filter(membership_end_date__lt=date.today()).count()

    context = {
        'total_customers': total_customers,
        'active_members': active_members,
        'expired_memberships': expired_memberships,
    }

    return render(request, 'crm/dashboard.html', context)