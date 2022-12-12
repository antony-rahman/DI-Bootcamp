from django.shortcuts import render
from django.http import HttpResponse # pass view information into the browser
from .models import Gif_model, Category_model
from .forms import CategoryForm, GifForm

# Create your views here.

def create_category(request):
    if request.method == 'POST':
        form_filled = CategoryForm(request.POST)
        # print(form_filled.data['name'])
        if  form_filled.is_valid():
            name = form_filled.cleaned_data['name']
            Category_model.objects.create(name = name)
    
    context = {'form': CategoryForm}
    return render(request, 'create_category.html', context)

def add_gif(request):
    if request.method == 'POST':
        form_filled = GifForm(request.POST)
        if  form_filled.is_valid():
            # print(form_filled.data['categories'])
            categories = form_filled.cleaned_data['categories']
            title = form_filled.cleaned_data['title']
            url = form_filled.cleaned_data['url']
            uploader_name = form_filled.cleaned_data['uploader_name']
            gif = Gif_model.objects.create(uploader_name = uploader_name, url = url, title = title)
            
            for category in categories:

                gif.categories.add(category)

            gif.save()
    
    context = {'form': GifForm}
    return render(request, 'add_gif.html', context)


def category_view(request, id):
    category = Category_model.objects.get(id=id)
    gifs = category.gifs.all()

    context = {'category': category, 'gifs': gifs}

    return render(request, 'category.html', context)

def homepage(request):
    context = {'gifs': Gif_model.objects.all(),
               'categories': Category_model.objects.all()}
    return render(request, 'homepage.html', context)