from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('product/<int:pk>/',views.ProductDetailView.as_view(),name="product_view"),
    path('cart/',views.CartView.as_view(),name="cart"),
    path('cart/<int:pk>/remove/',views.CartRemoveView.as_view(),name='cart_remove'),
    path('seller/',views.CreateSeller.as_view(),name='create-seller'),
    path('buyer/',views.CreateBuyer.as_view(),name='create-buyer'),
    path('newproduct/',views.ProductCreate.as_view(),name='create-product')
]
