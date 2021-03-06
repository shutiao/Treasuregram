from django.shortcuts import render
from .models import Treasure
from .forms import TreasureForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    # Here we need to get all of Treasure's objects
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, 'index.html', 
                    {'treasures': treasures, 'form': form})

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id = treasure_id)
    return render(request, 'detail.html', {'treasure': treasure})

# To process the submitted form,
# create an instance of form from the request
# and then retrieve the form data
#
def post_treasure(request):
    #Create the form and link it to the posted data
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username = username)
    # The QuerySet filter will look up all of the treasures that belong to this user
    treasures = Treasure.objects.filter(user=user)
    return render(request, 'profile.html',
    {
        'username': username,
        'treasures': treasures
    })