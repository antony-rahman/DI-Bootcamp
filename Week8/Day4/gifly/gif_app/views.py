from django.shortcuts import render, redirect
from .models import Category, Gif
from .forms import CategoryForm, GifForm


def create_category(request):

    if request.method == 'POST':
        form_filled = CategoryForm(request.POST)
        if form_filled.is_valid():
            name = form_filled.cleaned_data['name']
            Category.objects.create(name = name)

    # method - GET 
    context = {'form': CategoryForm}
    return render(request, 'create_category.html', context)

def create_gif(request):

    if request.method == 'POST':
        form_filled = GifForm(request.POST)
        if form_filled.is_valid():

            title = form_filled.cleaned_data['title']
            url = form_filled.cleaned_data['url']
            uploader = form_filled.cleaned_data['uploader_name']
            categories = form_filled.cleaned_data['category']

            new_gif = Gif(title=title, url=url, uploader_name=uploader)
            new_gif.save()

            for cat in categories:
                new_gif.categories.add(cat)

            new_gif.save()


    context = {'form': GifForm}
    return render(request, 'create_gif.html', context)

def category_view(request, id):
    category = Category.objects.get(id=id)
    gifs = category.gifs.all()

    context = {'category': category, 'gifs': gifs}

    return render(request, 'category.html', context)

def homepage(request):
    context = {'gifs': Gif.objects.all(),
               'categories': Category.objects.all()}
    return render(request, 'homepage.html', context)