from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mythical_creature/mythical_creature.html')

# Create your views here.
