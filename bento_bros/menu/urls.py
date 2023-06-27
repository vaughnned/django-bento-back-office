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
from menu.views import appetizer_records, main_records, dessert_records, delete_record

app_name = "menu"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', appetizer_records, name="app_record"),
    path('main/', main_records, name="main_record"),
    path('dessert/', dessert_records, name="dessert_record"),
    path('app/delete_app/<int:appetizer_id>', delete_record, name="delete_app")
]
