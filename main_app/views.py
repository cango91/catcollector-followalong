from django.shortcuts import render, get_object_or_404
from .models import Cat

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cats_index(request):
    return render(request, 'cats/index.html', {
        'cats': Cat.objects.all(),
    })


def cats_detail(request, cat_id):
    cat = get_object_or_404(Cat, id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})
