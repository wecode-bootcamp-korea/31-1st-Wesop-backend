from  django.urls import path
from products.views import ProductListView, ProductDetailView, RecommendedView, CategoryListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/categories', CategoryListView.as_view()),
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),
    path('/<int:product_id>' , ProductDetailView.as_view())
]