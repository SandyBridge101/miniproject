from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:id>/', views.ProductView.as_view(), name='product-view'),
    path('category/', views.CategoryListView.as_view(), name='category-create'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-list'),
    path('cart/', views.CartListView.as_view(), name='cart-list'),
    path('cart/create/', views.CartCreateView.as_view(), name='cart-create'),
    path('cart/update/<int:pk>/', views.CartUpdateView.as_view(), name='cart-update'),
    path('cart/delete/<int:id>/', views.CartDeleteView.as_view(), name='cart-delete'),
    path('region/', views.RegionListView.as_view(), name='region-list'),
    path('region/create/', views.RegionCreateView.as_view(), name='region-create'),
    path('home/', views.index, name='home'),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("product/<int:id>/", views.product, name="product"),
    path("cart/<int:id>/", views.cart, name="cart"),
    
#    path('pay/<str:username>/<int:orderID>/<str:method>/<str:pin>/', views. paymentView, name='payment'),

] 