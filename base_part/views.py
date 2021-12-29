from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import ClothesForm
from .models import Clothes


def index(request):
    clothes = Clothes.objects.all()
    context = {'clothes': clothes}
    return render(request, 'index.html', context)


def details(request, cloth_id):
    cloth = get_object_or_404(Clothes, uuid=cloth_id)
    context = {
        'cloth': cloth,
        'back': request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') else ''
    }
    return render(request, 'detail.html', context=context)


def create(request):
    if request.method == "POST":
        form = ClothesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'form': ClothesForm
    }
    return render(request, 'add_cloth.html', context)


def edit(request, cloth_id):
    try:
        cloth = Clothes.objects.get(uuid=cloth_id)
    except Clothes.DoesNotExist:
        raise Http404('CLOTH DOES NOT EXIST')

    if request.method == "POST":
        form = ClothesForm(request.POST, instance=cloth)
        if form.is_valid():
            form.save()
            return redirect('details', cloth_id)

    form = ClothesForm(instance=cloth)
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def delete(request,cloth_id):
    try:
        cloth = Clothes.objects.get(uuid=cloth_id)
        cloth.delete()
    except Clothes.DoesNotExist:
        raise Http404('The Resource, you requested does not exist!')

    return redirect('index')
