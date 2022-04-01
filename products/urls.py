from django.urls import path
from products.views import ProductListView, CategoryView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/<int:category_id>', CategoryView.as_view()),
]
