from django.shortcuts import render

pokemon = [
    {'name': 'Sparky', 'species': 'Pikachu', 'type': 'Electric', 'description': 'Chonky boi go zapp'}
]

# Create your views here.

def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def poke_index (request):
    return render(request, 'pokemon/index.html', {
        'pokemons': pokemon
    })