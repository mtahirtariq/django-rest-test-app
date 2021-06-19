from django.urls import path

from . import views

app_name = 'api'


urlpatterns = [
    path('create_customer/', views.CreateCustomerView.as_view(), name='create_customer'),
]
