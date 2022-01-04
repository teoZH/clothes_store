from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .forms import ClothesForm
from .models import Clothes
from os import remove


def index(request):
    clothes = Clothes.objects.all()
    paginator = Paginator(clothes,4)
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    context = {'clothes': page_obj}
    return render(request, 'index.html', context)


def details(request, cloth_id):
    cloth = get_object_or_404(Clothes, uuid=cloth_id)
    context = {
        'cloth': cloth,
        'back': request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') else ''
    }
    return render(request, 'detail.html', context=context)


def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ClothesForm(request.POST,request.FILES)
            if form.is_valid():
                cloth = form.save(commit=False)
                cloth.user = request.user
                cloth.save()
    context = {
        'form': ClothesForm
    }
    return render(request, 'add_cloth.html', context)


def edit(request, cloth_id):
    try:
        cloth = Clothes.objects.get(uuid=cloth_id)
    except Clothes.DoesNotExist:
        raise Http404('CLOTH DOES NOT EXIST')
    if request.user == cloth.user:
        if request.method == "POST":
            form = ClothesForm(request.POST,request.FILES, instance=cloth)
            if form.is_valid():
                if request.FILES:
                    remove(cloth.image.path)
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
        if request.user == cloth.user:
            remove(cloth.image.path)
            cloth.delete()
    except Clothes.DoesNotExist:
        raise Http404('The Resource, you requested does not exist!')
    return redirect('index')
