from django.shortcuts import render, redirect
from .models import Category, Theme
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import RegForm
from django.views import View



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


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = RegForm
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')


            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()
            login(request, user)
            return redirect('/')

def search(request):
    if request.method == 'POST':
        searched_product = request.POST.get('search_product')
        product = Theme.objects.filter(name_theme__iregex=searched_product)
        context = {}
        if product:
            context.update(user_pr=searched_product, products=product)
        else:
            context.update(user_pr=searched_product, products='')
        return render(request, 'result.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


