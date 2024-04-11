"""
URL configuration for floreria project.

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
from plantas.views import ( 
                           CreateResitryPlantView, 
                           RetrievePlantsView, 
                           RetrievePlantsidView, 
                           UpdateRegitryPlant,
                           DeletePlantRegistryView,
                           DeleteallPlantRegistryView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # DELETE URLS
    path('create/plant', CreateResitryPlantView.as_view(), name= "Create Object Plant"),
    path('list', RetrievePlantsView.as_view(), name= "Lista de plantas"),
    path('list/<int:pk>/', RetrievePlantsidView.as_view(), name="Lista por id"), 
    path('update/<int:pk>/', UpdateRegitryPlant.as_view(), name="Update Registry by Id"),
    path('deleteall/', DeleteallPlantRegistryView.as_view(), name='delete_all_plants'),
    path('delete/<int:pk>/', DeletePlantRegistryView.as_view(), name='delete_specific_plant'),
] 



