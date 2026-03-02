from django.shortcuts import render
from .models import Category, Theme


def home1(request):
    categories = Category.objects.all()
    themes = Theme.objects.all()
    return render(request, 'home.html', {'categories': categories, 'themes': themes})


def categ(request, pk):
    categori = Category.objects.get(id=pk)
    themes010 = Theme.objects.filter(theme_category_id=categori)
    return render(request, 'category.html', {'categori': categori, 'themes010': themes010})

def theme2(request, pk):
    theme3 = Theme.objects.get(id=pk)
    return render(request, 'theme.html', {'theme3': theme3})
