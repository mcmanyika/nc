"""chamisa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from libs.views import *
from joins.views import logout

urlpatterns = [
    url(r'admin/', admin.site.urls),

    url(r'dash/', dash, name='dash'),
    url(r'shop/', include('shop.urls')),
    url(r'products/', include('products.urls')),
    url(r'cart/', include('cart.urls')),
    url(r'orders/', include('orders.urls')),
    url(r'blog/', include('blog.urls')),
    url(r'donate/', donate, name='donate'),
    url(r'libs/', include('libs.urls')),
    url(r'login/', include('joins.urls')),
    url(r'^', landing, name='landing'),

]
