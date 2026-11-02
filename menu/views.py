from django.shortcuts import render

# Create your views here.
from django.shortcuts  import render, redirect
from .models import Dish, Review
from .forms import ReviewForm

def menu_list(request):
    dishes = Dish.objects.all()
    reviews = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = ReviewForm()

    return render(request, 'menu/index.html', {
        'dishes': dishes,
        'reviews': reviews,
        'form': form
    })
