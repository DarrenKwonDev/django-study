from django.shortcuts import render
from . import models

# Create your views here.
def portfolio(request):
    portfolios = models.Portfolio.objects
    return render(request, "portfolio.html", {"portfolios": portfolios})