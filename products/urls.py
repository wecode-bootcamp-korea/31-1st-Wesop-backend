from django.urls import path

from .views import ProductDetailView ,RecommendedView 

urlpatterns = [
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),
    path('/<int:product_id>' , ProductDetailView.as_view())
]
 