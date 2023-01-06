from django.shortcuts import render
import jason
# Create your views here.

with open ('./data.json', 'r')as f:
    data = json.load(f)

animals:list = data['animals']
families:list = data['families']

def show_family(request,id:int)-> HTTPResponse:
    family_selected = None

    for family in families:
        if family['id'] == id:
    return render(request, 'family.html', family_selected)

def show_animals(request,id:int)-> HTTPResponse:
    animal_selected = None

    for animal in animals:
        if family['id'] == id:
    return render(request, 'family.html', family_selected)

    def show_animals(request) ->HTTPResponse:
        return render(request, 'animals.html',)
