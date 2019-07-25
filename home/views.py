from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import reverse
from django.views.generic import View
from .models import Product,Category


class HomeView(View):
    template_name='home/home.html'
    def get(self,request):
        product=Product.objects.all()
        categories=[category.category for category in Category.objects.all()]
        return render(request,self.template_name,{'products':product,'categories':set(categories)})
