from unicodedata import name
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts.views import login_page, register_page, logout_page, guest_register_view
from django.views.generic import TemplateView
from carts.views import cart_home

from .views import (home_page, about_page, contact_page,
                    )

urlpatterns = [
	path('', home_page, name="home"),
	path('about/', about_page, name="about"),
	path('contact/', contact_page, name="contact"),
    path('cart/', cart_home, name='cart'),
    path('cart/', include("carts.urls", namespace="cart")),
    path('login/', login_page, name="login"), 
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name="register"),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('products/', include("products.urls", namespace="products")),
    path('search/', include("search.urls", namespace="search")),
	path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
