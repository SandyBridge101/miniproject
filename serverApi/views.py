from django.shortcuts import render
from .models import *
from .serializers import *

from django.http import HttpResponse,JsonResponse
from django.db.models import Q


# Create your views here.
from rest_framework import generics, permissions
from django.views.generic import TemplateView, ListView

# Create your views here.

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    http_method_names = ['get']


class RegionCreateView(generics.CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    http_method_names = ['get']



class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']



class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class CartUpdateView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['put']

class CartDeleteView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    http_method_names = ['delete']

class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_names = ['get']

class SearchResultsView(ListView):
    model = Product
    template_name = "search.html"
    

    def get_queryset(self): # new
        categories=[]
        regions=[]
        product = self.request.GET.get("product")
        price = self.request.GET.get("price")

        print('Check box results',categories,regions )
        query=Q()
        if price!='':
            query|=Q(price=price)
        

        if product:
            query|=Q(name__icontains=product)

        for r in Region.objects.all():
            #regions.append(self.request.GET.get(r.name))
            region=self.request.GET.get(r.name)
            if region:
                query|=Q(region_id=int(region))

        for c in Category.objects.all():
            #categories.append(self.request.GET.get(c.name))
            category=self.request.GET.get(c.name)
            if category:
                query|=Q(category_id=int(category))

        

        return Product.objects.filter(
            query
        )

def index(request):
    data=Product.objects.all()
    categories=Category.objects.all()
    regions=Region.objects.all()
    context = {
        'title': 'Custodia',
        'heading': 'Welcome to Home page!',
        'content': 'This is some content for Home page.',
        'data':data,
        'categories':categories,
        'regions':regions,
    }
    return render(request, 'index.html', context)

def product(request,id):
    product=Product.objects.all()[id-1]
    category=Category.objects.all()[product.category_id.id-1]
    region=Region.objects.all()[product.region_id.id-1]
    context = {
        'title': 'Custodia',
        'heading': 'Welcome to Home page!',
        'content': 'This is some content for Home page.',
        'id':id,
        'product':product,
        'category':category,
        'region':region,
    }
    return render(request, 'product.html', context)


def cart(request,id):
    cart=Cart.objects.all()[1]
    cart_items=cart.product_id.all()
    cart.product_id.add(Product.objects.all()[id-1])
    cart.save()

    cart=Cart.objects.all()[1]

    quantity=Product.objects.all()[id-1].stock_quantity
    Product.objects.get(id=id).stock_quantity=5
    Product.objects.get(id=id).save()
    cart_items=cart.product_id.all()
     
    context = {
        'title': 'Custodia',
        'heading': 'Welcome to Home page!',
        'content': 'This is some content for Home page.',
        'cart':cart,
        'items':cart_items,
    }
    return render(request, 'cart.html', context)
