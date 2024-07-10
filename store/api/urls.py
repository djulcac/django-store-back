from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompaniesViewSet)
router.register(r'categories', views.CategoriesViewSet)
router.register(r'products', views.ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
