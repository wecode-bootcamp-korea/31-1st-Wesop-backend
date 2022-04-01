from django.urls import path

from .views import ProductDetailView
urlpatterns = [
    path('/detail/<str:products_name>' , ProductDetailView.as_view()),
    # path('/how/<str:products_name>' , HowToUseView.as_view()),
    # path('/recommend/<str:products_name>' , RecommendedView.as_view())
]
 