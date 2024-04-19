from django.urls import path

from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'),
    path('stripe-webhook/', views.stripe_webhook, name='stripe_webhook'),
    path('', views.HomePageView.as_view(), name='home'),
]
