from django.urls import path

from .views import  RecommendedView
urlpatterns = [   
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),
]
 