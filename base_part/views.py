from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .forms import ClothesForm
from .models import Clothes
from os import remove
from django.views import View


class IndexView(View):
    obj_klass = Clothes
    objects = None
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        self.objects = self.obj_klass.objects.all()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        paginator = Paginator(self.objects, 4)
        page_number = request.GET.get('page')
        if not page_number:
            page_number = 1
        page_obj = paginator.get_page(page_number)
        context = {'clothes': page_obj}
        return render(request, self.template_name, context)


class DetailsView(View):
    obj_klass = Clothes
    query_object = None
    template_name = 'detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.query_object = get_object_or_404(self.obj_klass, uuid=kwargs['cloth_id'])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,cloth_id):
        context = {
            'cloth': self.query_object,
            'back': request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') else ''
        }
        return render(request, self.template_name, context=context)


class CreateView(View):
    form = ClothesForm
    context = {'form': form}

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'add_cloth.html', self.context)

    def post(self, request):
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            cloth = form.save(commit=False)
            cloth.user = request.user
            cloth.save()
            return redirect('index')
        return render(request, 'add_cloth.html', self.context)


class EditView(View):
    object_klass = Clothes
    query_object = None
    form_klass = ClothesForm

    def dispatch(self, request, *args, **kwargs):
        try:
            self.query_object = self.object_klass.objects.get(uuid=kwargs['cloth_id'])
            if request.method == 'POST':
                if not request.user == self.query_object.user:
                    raise Http404('Not Possible!')
        except self.object_klass.DoesNotExist:
            redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,cloth_id):
        form = self.form_klass(instance=self.query_object)
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)

    def post(self, request, cloth_id):
        form = self.form_klass(request.POST, request.FILES, instance=self.object_klass)
        if form.is_valid():
            if request.FILES:
                remove(self.object_klass.image.path)
            form.save()
            return redirect('details', cloth_id)
        return redirect('index')


class DeleteView(View):

    object_klass = Clothes
    query_object = None

    def dispatch(self, request, *args, **kwargs):
        try:
            self.query_object = self.object_klass.objects.get(uuid=kwargs['cloth_id'])
        except self.object_klass.DoesNotExist:
            return redirect('index')
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,cloth_id):
        if request.user == self.query_object.user:
            remove(self.query_object.image.path)
            self.query_object.delete()
            return redirect('index')
        raise Http404('Failed to delete')
