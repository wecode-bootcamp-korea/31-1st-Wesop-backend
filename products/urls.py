from django.urls import path

from .views import ProductReview ,ProductDetailView ,RecommendedView ,ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),
    path('/<int:product_id>' , ProductDetailView.as_view()),
    path('/review' , ProductReview.as_view())
]
