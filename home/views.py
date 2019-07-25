from django.shortcuts import render,redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product,Category,Quantity,Seller,Buyer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


class HomeView(View):
    template_name='home/home.html'
    def get(self,request):
        products=Product.objects.all()
        categories=[category.category for category in Category.objects.all()]
        return render(request,self.template_name,{'products':products,'categories':set(categories)})

class ProductDetailView(View):
    template_name='home/product_detail.html'
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        categories=[category.category for category in Category.objects.all()]
        if request.user.is_authenticated:
            cart_products = [qty.product for qty in request.user.buyer.cart_set.first().qty.all()]
        else:
            cart_products =[]    
        return render(request,self.template_name,{'product':product,'in_cart':product in cart_products,'categories':set(categories)})

class CartView(LoginRequiredMixin,View):
    template_name = 'home/cart.html'
    def get(self, request):
        categories=[category.category for category in Category.objects.all()]
        return render(request,self.template_name,{'products':request.user.buyer.cart_set.first().qty.all(),'categories':set(categories)})
    def post(self,request):
        qty = Quantity()
        qty.qty = request.POST.get("qty")
        qty.product = Product.objects.get(pk=int(request.POST.get("pk")))
        qty.save()
        request.user.buyer.cart_set.first().qty.add(qty)
        return render(request,self.template_name,{'products':request.user.buyer.cart_set.first().qty.all()})

class CartRemoveView(View):
    template_name = 'home/cart.html'
    def get(self, request, pk):
        product = get_object_or_404(Product,pk=pk)
        for qty in request.user.buyer.cart_set.first().qty.all():
            if qty.product.pk == product.pk:
                qty.delete()
        return render(request,self.template_name,{'products':request.user.buyer.cart_set.first().qty.all()})
class CreateSeller(View):
    template_name='home/create_seller.html'
    def get(self,request):
        if not request.user.is_authenticated:
            return HttpResponse("Not Found")
            

        if request.user.is_authenticated and Seller.objects.filter(user=request.user).exists() or Buyer.objects.filter(user=request.user):
            return HttpResponse(status=500)
        return render(request,self.template_name)  
    def post(self,request):
        if request.user.is_authenticated and Seller.objects.filter(user=request.user).exists():
            return HttpResponse(status=500)
        else:
            if not request.user.is_authenticated:
                return HttpResponse(status=500)
            seller=Seller()
            seller.user=request.user
            seller.phone_number=request.POST.get('phone_num')
            seller.address=request.POST.get('address')
            seller.save()
            return redirect('home')
        return render(request,self.template_name)   
class CreateBuyer(View):
    template_name='home/create_buyer.html'
    def get(self,request):
        if not request.user.is_authenticated:
            return HttpResponse("Not Found")
            

        if request.user.is_authenticated and Buyer.objects.filter(user=request.user).exists() or Seller.objects.filter(user=request.user):
            return HttpResponse(status=500)
        return render(request,self.template_name)  
    def post(self,request):
        if request.user.is_authenticated and Buyer.objects.filter(user=request.user).exists():
            return HttpResponse(status=500)
        else:
            if not request.user.is_authenticated:
                return HttpResponse(status=500)
            seller=Seller()
            seller.user=request.user
            seller.phone_number=request.POST.get('phone_num')
            seller.address=request.POST.get('address')
            seller.save()
            return redirect('home')
        return render(request,self.template_name)           

class ProductCreate(View):
    template_name="home/create_product.html"
    def get(self,request):
        if not request.user.is_authenticated :
            return HttpResponse("Not Found")
        if request.user.is_authenticated and not Seller.objects.filter(user=request.user).exists():
            return HttpResponse("Not Found")
        return render(request,self.template_name)    

    def post(self,request):
        if not request.user.is_authenticated :
            return HttpResponse("Not Found")
        if request.user.is_authenticated and not Seller.objects.filter(user=request.user).exists():
            return HttpResponse("Not Found")
        else :
            product=Product()
            product.name =request.POST.get('name')
            product.price=request.POST.get('price')
            product.description=request.POST.get('description')
            product.img=request.FILES.get('image')
            product.stock=True
            product.rating =0
            product.seller=request.user.seller
            product.save()
            category=Category()
            category.category=request.POST.get('category').title()
            category.product=product
            category.save()
            return redirect('product_view',pk=product.pk)
        return render(request,self.template_name)



        