from unicodedata import name
from django.urls import path
from .views import CategoryView, DetailCategory, ProductView, DetailProduct,FilterProductsByCategory,AddCartView,CartDeleteItem
urlpatterns = [
    path('categories', CategoryView.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    path('products', ProductView.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),
    path('category/<int:categ_id>/products',FilterProductsByCategory.as_view(),name='category_products'),
    #path('carts',CartViewSet.as_view(),name='carts'),
    path("cart/", AddCartView.as_view()),
    path("cart/<int:cartitem_id>", CartDeleteItem.as_view()),
    #path("cart-item/<int:pk>/", CartItemAPIView.as_view()),
]