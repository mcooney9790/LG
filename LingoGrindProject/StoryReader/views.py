from django.shortcuts import render
from .models import Story
# Create your views here.

def home(request):
    bunnysmoke = Story.objects.published().filter(title = 'The Bunny Who Smoked')
    mrfrogduck = Story.objects.published().filter(title = 'Mr. Frog and Mr. Duck')
    busybird = Story.objects.published().filter(title = 'The Busy Little Bird')
    squirrel = Story.objects.published().filter(title = 'The Political Squirrel and the Industrious Squirrel')
    iphoneinsect = Story.objects.published().filter(title = 'The iPhone Insects')
    return render(request, "home.html", {"bunnysmokes": bunnysmoke, "mrfrogducks": mrfrogduck, "busybirds": busybird, "squirrels": squirrel, "iphoneinsects":iphoneinsect})