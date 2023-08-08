from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Cat
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
    })


class CreateCat(CreateView):
    model = Cat
    fields = '__all__'


class UpdateCat(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']


class DeleteCat(DeleteView):
    model = Cat
    success_url = '/cats'


def add_feeding(request, pk):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    if(form.is_valid()):
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = pk
        new_feeding.save()
    return redirect('cats:detail', cat_id=pk)
