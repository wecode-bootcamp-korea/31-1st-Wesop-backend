from django.urls import path

from .views import ProductReview
urlpatterns = [
    path('/review' , ProductReview.as_view())
]