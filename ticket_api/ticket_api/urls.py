"""
URL configuration for ticket_api project.

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
from django.urls import path
from  tickets1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tic/list',views.no_rest_from_model),
    path('tic/rest', views.FBV_List),
    path('tic/dele/<int:pk>', views.FBV_pk),
    path('tic/CBV_List', views.CBV_List.as_view()),
    path('tic/CBV_pk/<int:pk>', views.CBV_pk.as_view()),
    path('tic/mixins_list', views.mixins_list.as_view()),
    path('tic/mixins_pk/<int:pk>', views.mixins_pk.as_view()),
    path('tic/generics_list', views.generics_list.as_view()),
    path('tic/generics_pk/<int:pk>', views.generics_pk.as_view()),
]
