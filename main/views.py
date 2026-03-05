from django.shortcuts import render, redirect
from .models import Category, Theme, Cart
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
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            login(request, user)
            return redirect('/')

        return render(request, self.template_name)


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


def add_favorite(request, pk):
    theme = Theme.objects.get(id=pk)

    # проверяем, есть ли уже в избранном
    if not Cart.objects.filter(user_id=request.user.id, user_product=theme).exists():
        Cart.objects.create(user_id=request.user.id, user_product=theme)

    return redirect('/theme2/' + str(pk))


def cart_page(request):
    user_cart = Cart.objects.filter(user_id=request.user.id)
    return render(request, 'cart.html', {'user_cart': user_cart})

def remove_favorite(request, pk):
    Cart.objects.filter(user_id=request.user.id, user_product_id=pk).delete()
    return redirect('/cart/')