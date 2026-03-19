"""
URL configuration for storefront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
import debug_toolbar
from django.http import HttpResponse, JsonResponse

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

def home(request):
    return JsonResponse({
        "name": "Storefront API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "admin": {
                "base": "/admin/",
                "dashboard": "/admin/",
                "users": "/admin/auth/user/",
                "groups": "/admin/auth/group/",
                "models": {
                    "products": "/admin/store/product/",
                    "collections": "/admin/store/collection/",
                    "carts": "/admin/store/cart/",
                    "customers": "/admin/store/customer/",
                    "orders": "/admin/store/order/",
                }
            },
            "playground": {
                "base": "/playground/",
                "hello": "/playground/hello/",
            },
            "store": {
                "base": "/store/",
                "products": {
                    "list": "/store/products/",
                    "detail": "/store/products/{id}/",
                    "reviews": {
                        "list": "/store/products/{product_id}/reviews/",
                        "detail": "/store/products/{product_id}/reviews/{id}/"
                    }
                },
                "collections": {
                    "list": "/store/collections/",
                    "detail": "/store/collections/{id}/"
                },
                "carts": {
                    "list": "/store/carts/",
                    "detail": "/store/carts/{id}/",
                    "items": {
                        "list": "/store/carts/{cart_id}/items/",
                        "detail": "/store/carts/{cart_id}/items/{id}/"
                    }
                },
                "customers": {
                    "list": "/store/customers/",
                    "detail": "/store/customers/{id}/"
                },
                "orders": "/store/orders/",
            },
            "authentication": {
                "base": "/auth/",
                "users": "/auth/users/",
                "register": "/auth/users/",
                "login": "/auth/jwt/create/",
                "refresh": "/auth/jwt/refresh/",
                "verify": "/auth/jwt/verify/",
                "me": "/auth/users/me/",
                "password_reset": "/auth/users/reset_password/",
                "activation": "/auth/users/activation/",
            }
        },
        "documentation": "Coming soon",
    })

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls)),
]
