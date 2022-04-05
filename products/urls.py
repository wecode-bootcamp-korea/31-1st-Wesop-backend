from django.urls import path

from .views import ProductReview ,ProductDetailView ,RecommendedView 
urlpatterns = [
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),
    path('/<int:product_id>' , ProductDetailView.as_view()),
    path('/review' , ProductReview.as_view())
]

 
