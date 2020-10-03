from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from . import models

# Create your views here.
def home(request):
    blogs = models.Blog.objects.all()
    print(blogs)
    return render(request, "home.html", {"blogs": blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(models.Blog, pk=blog_id)

    return render(request, "detail.html", {"blog": blog_detail})


def new(request):
    return render(request, "new.html")


def create(request):
    blog = models.Blog()

    blog.title = request.GET["title"]
    blog.body = request.GET["body"]
    blog.pub_date = timezone.datetime.now()

    print(blog)

    blog.save()

    return redirect("/blog/" + str(blog.id))
