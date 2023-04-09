from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .models import Movie
from .forms import MovieForm

# Create your views here.
@require_safe
def index(request):
    
    moives = Movie.objects.all()
    
    context = {
        'movies' : moives
    }
    
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm()
    context = {
        'form':form
    }
    return render(request, 'movies/create.html',context)


@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    context = {
        'movie': movie
    }
    
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET','POST'])
def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context ={
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)


@require_POST
def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect('movies:index')