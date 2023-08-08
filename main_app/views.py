from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Cat

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cats_index(request):
    cats = get_list_or_404(Cat)
    return render(request, 'cats/index.html', {
        'cats': cats,
    })
    

def cats_detail(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

class CreateCat(CreateView):
    model = Cat
    fields= '__all__'
    
class UpdateCat(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']
    
class DeleteCat(DeleteView):
    model = Cat
    success_url = '/cats'