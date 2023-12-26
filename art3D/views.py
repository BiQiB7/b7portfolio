from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'art3D/art3D.html')