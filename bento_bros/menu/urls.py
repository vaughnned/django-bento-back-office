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
from menu.views import appetizer_records, main_records, dessert_records, delete_app, delete_main, delete_dessert, update_app, update_main, update_dessert

app_name = "menu"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', appetizer_records, name="app_record"),
    path('main/', main_records, name="main_record"),
    path('dessert/', dessert_records, name="dessert_record"),
    path('delete_app/<int:appetizer_record_id>',
         delete_app, name="delete_app"),
    path('delete_main/<int:main_record_id>',
         delete_main, name="delete_main"),
    path('delete_dessert/<int:dessert_record_id>',
         delete_dessert, name="delete_dessert"),
    path('update_app/<int:appetizer_record_id>',
         update_app, name="update_app"),
    path('update_main/<int:main_record_id>',
         update_main, name="update_main"),
    path('update_dessert/<int:dessert_record_id>',
         update_dessert, name="update_dessert"),
]
