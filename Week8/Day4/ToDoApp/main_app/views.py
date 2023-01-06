from django.shortcuts import render, redirect
from .forms import CategoryForm, TodoForm
from .models import Category, Todo
from datetime import date

def create_todo(request):

    context = {'form': TodoForm}

    if request.method == 'POST':
        form_filled = TodoForm(request.POST)
        if form_filled.is_valid():
            title = form_filled.cleaned_data['title']
            details = form_filled.cleaned_data['details']
            deadline_date = form_filled.cleaned_data['deadline_date']
            category = form_filled.cleaned_data['category']

            Todo.objects.create(title=title, details=details, 
            deadline_date=deadline_date, category=category)

    return render(request, 'add_todo.html', context)

def create_category(request):

    context = {'form': CategoryForm}

    if request.method == 'POST':
        form_filled = CategoryForm(request.POST)
        if form_filled.is_valid():
            name = form_filled.cleaned_data['name']
            image = form_filled.cleaned_data['image']
            Category.objects.create(name=name, image=image)

    return render(request, 'add_category.html', context)

def category(request, id):
    cat = Category.objects.get(id=id)
    todos = cat.todos.all()
    context = {'category':cat, 'todos': todos}

    return render(request, 'category.html', context)

def todo_done(request, id):

    if request.method == "POST":
        todo = Todo.objects.get(id=id)
        todo.has_been_done = True
        todo.date_completion = date.today()
        todo.save()
        category = todo.category

    return redirect(category.get_absolute_url())


def home(request):

    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'homepage.html', context)
