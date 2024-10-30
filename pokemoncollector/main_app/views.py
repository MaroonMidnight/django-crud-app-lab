from django.shortcuts import render, redirect
from .models import Pokemon, Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.http import HttpResponse
# Create your views here.

from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request,'pokemon/index.html', {'pokemon': pokemon})

def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
    return redirect('pokemon-detail', pokemon_id=pokemon_id)

def pokemon_detail(request, pokemon_id):
    pokemon_from_db = Pokemon.objects.get(id=pokemon_id)
    items_pokemon_doesnt_have = Item.objects.exclude(id__in = pokemon_from_db.items.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'pokemon/detail.html', {'pokemon': pokemon_from_db, 'feeding_form': feeding_form, 'items': items_pokemon_doesnt_have})

class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name','type', 'description', 'evolution']
    
class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['name', 'description', 'evolution']
    
class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'
    
class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    
class ItemList(ListView):
    model = Item
    
class ItemDetail(DetailView):
    model = Item
    
class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'effect']
    
class ItemDelete(DeleteView):
    model = Item
    success_url = '/items/'
    
def associate_item(request, pokemon_id, item_id):
    Pokemon.objects.get(id=pokemon_id).items.add(item_id)
    return redirect('pokemon-detail', pokemon_id=pokemon_id)

def remove_item(request, pokemon_id, item_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    item = Item.objects.get(id=item_id)
    pokemon.items.remove(item)
    
    return redirect('pokemon-detail', pokemon_id=pokemon.id)