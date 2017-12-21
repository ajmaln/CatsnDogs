from django.urls import path

from main import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('api/cats/<user>/<int:pk>', views.cat_list, name='cat_list'),
    path('api/dogs/<user>/<int:pk>', views.dog_list, name='dog_list'),
    path('api/cats/<user>', views.cat_list, name='cat_list'),
    path('api/dogs/<user>', views.dog_list, name='dog_list'),
]

