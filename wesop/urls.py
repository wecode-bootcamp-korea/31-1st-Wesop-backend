from django.urls import path, include

urlpatterns = [
    path('users', include('users.urls')),
<<<<<<< HEAD
    path('products', include('products.urls'))
=======
    path("products",include('products.urls'))
>>>>>>> main
]
