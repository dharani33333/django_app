from django.shortcuts import render
# from django.http import HttpResponse
from .models import Tasks

# Create your views here.
# def homepage(request):
#     return HttpResponse("<h1>Welcome to my homepage!</h1>")

def homepage(request):
    all_task=Tasks.objects.all()
    print(all_task)
    return render(request,"homepage.html",context={"tasks":all_task})
