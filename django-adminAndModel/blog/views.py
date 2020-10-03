from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    blogs = models.Blog.objects.all()
    print(blogs)
    return render(request, "home.html", {"blogs": blogs})