from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from .validators import check_splcharacter
from .forms import SearchForm

# get person by name
def get_by_name(request, name: str) -> HttpResponse:
    person = Person.objects.get(name = name)
    return render(request, 'info.html', {'person': person})

# get person by number
def get_by_number(request, number: str) -> HttpResponse:
    person = Person.objects.get(phone_number = number)
    return render(request, 'info.html', {'person': person})

# get all persons
def get_all(request):
    persons = Person.objects.all()
    return render(request, 'all.html', {'persons': persons})

# search for a person by name or phone number (Daily-Challenge Day4)
def search_contact(request):
    search = SearchForm()
    context = {'searchform' : search}
    if request.method == 'POST':
        form_filled = SearchForm(request.POST)
        if form_filled.is_valid():
            if form_filled.cleaned_data['name']:
                name = form_filled.cleaned_data['name']
                return redirect('get_by_name', name=name) 

            if form_filled.cleaned_data['phone']:
                phone = form_filled.cleaned_data['phone']
                person = Person.objects.get(phone = phone)
                return redirect('get_by_name', name=context['person'].name)

    return render (request, 'search.html', context)
            
            


