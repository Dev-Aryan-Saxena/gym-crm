from django.urls import path
from .views import customer_list, add_customer, edit_customer, delete_customer, register, customer_detail, dashboard
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', customer_list, name='home'),
    path('customers/', customer_list, name='customer_list'),
    path('add-customer/', add_customer, name='add_customer'),
    path('edit-customer/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('delete-customer/<int:customer_id>/', delete_customer, name='delete_customer'),
    path('customer/<int:pk>/', customer_detail, name='customer_detail'),
    
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='crm/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='crm/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='crm/password_change_done.html'), name='password_change_done'),
    

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='crm/password_reset.html'),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='crm/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='crm/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='crm/password_reset_done.html'),name='password_reset_complete'),

    path('dashboard/', dashboard, name='dashboard'),

]