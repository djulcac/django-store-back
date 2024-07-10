"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def get_version(request):
    return JsonResponse({
        'status': 'ok',
        'version': 'v0.1.0',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/v1/accounts/',
        include(
            ('django_accounts.accounts_sun.api.urls', 'accounts_sun_api'),
            namespace='accounts_sun_api'
        )
    ),
    path(
        '',
        include(
            ('homepage.urls', 'homepage'),
            namespace='homepage'
        )
    ),
    path(
        'api/v1/store/',
        include(
            ('store.api.urls', 'store_api'),
            namespace='store_api'
        )
    ),
    path('api/v1/healthcheck/', get_version, name='version'),
]
