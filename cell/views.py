from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import cellfForm
from .models import cellf


def index(request):

    if request.method == "POST":
        form = cellfForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'conformation.html')
    form = cellfForm()

    page = {
        "forms": form,
        "title": "cellf LIST",
    }
    return render(request, 'index.html', page)
