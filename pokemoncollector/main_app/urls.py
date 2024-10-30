from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemon/', views.pokemon_index, name='pokemon-index'),
    path('pokemon/<int:pokemon_id>', views.pokemon_detail, name='pokemon-detail'),
    path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon-create'),
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemon-update'),
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemon-delete'),
    path('pokemon/<int:pokemon_id>/add-feeding/', views.add_feeding, name='add-feeding'),
    path('items/create/', views.ItemCreate.as_view(), name='item-create'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('items/', views.ItemList.as_view(), name='item-index'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
    path('pokemon/<int:pokemon_id>/associate-item/<int:item_id>/', views.associate_item, name='associate-item'),
    path('pokemon/<int:pokemon_id>/remove-item/<int:item_id>/', views.remove_item, name='remove-item'),

]