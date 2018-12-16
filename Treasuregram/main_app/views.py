from django.shortcuts import render
from .models import Treasure

# Create your views here.
def index(request):
    # Here we need to get all of Treasure's objects
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})
