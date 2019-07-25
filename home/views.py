from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import reverse
from django.views.generic import View
from .models import Product


class HomeView(View):
    template_name='home/product_detail.html'
    def get(self,request):
        return render(request,self.template_name)
