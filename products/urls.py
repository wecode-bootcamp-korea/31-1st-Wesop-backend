from  django.urls import path
from products.views import ProductListView, ProductDetailView, RecommendedView, CategoryListView, CategoryDetailView, ProductReviewView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/categories', CategoryListView.as_view()),
    path('/categories/<int:category_id>', CategoryDetailView.as_view()),
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),
    path('/<int:product_id>' , ProductDetailView.as_view()),
    path('/review' , ProductReviewView.as_view())
]