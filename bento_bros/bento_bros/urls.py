"""
URL configuration for bento_bros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from menu.views import home_page, item, appetizer_item, seed, main_item, dessert_item

app_name = "menu"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('item/<int:index>', item),
    path('seed/', seed),
    path('appetizer_item/<int:appetizer_item_id>',
         appetizer_item, name="appetizer_item"),
    path('main_item/<int:main_item_id>',
         main_item, name="main_item"),
    path('dessert_item/<int:dessert_item_id>',
         dessert_item, name="dessert_item"),
]
