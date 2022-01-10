from django.shortcuts import render, get_object_or_404, redirect
from .mixins import PaginationMixin, ContentMixin, FormMixin
from django.http import Http404
from .forms import ClothesForm
from .models import Clothes
from os import remove
from django.views import View


class IndexView(View, PaginationMixin, ContentMixin):
    obj_klass = Clothes
    objects = None
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        self.objects = self.obj_klass.objects.all()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        self.paginate(request)
        return super().render_to_response(request)


class DetailsView(View, ContentMixin):
    obj_klass = Clothes
    template_name = 'detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.obj_id = kwargs['cloth_id']
        return super().dispatch(request,*args,**kwargs)

    def get(self, request, *args,**kwargs):
        self.get_object_id(request)
        extra = {'back': request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') else ''}
        return self.render_to_response(request,**extra)


class CreateView(View, FormMixin):
    template = 'add_cloth.html'
    form_klass = ClothesForm
    redirect_to = 'index'
    type_func = 'create'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'add_cloth.html', {'form':ClothesForm})



class EditView(View,FormMixin):
    object_klass = Clothes
    object = None
    form_klass = ClothesForm
    obj_id = 'cloth_id'
    redirect_to = 'details'

    def dispatch(self, request, *args, **kwargs):
        try:
            print(kwargs)
            self.object = self.object_klass.objects.get(uuid=kwargs[self.obj_id])
            if request.method == 'POST':
                if not request.user == self.object.user:
                    raise Http404('Not Possible!')
        except self.object_klass.DoesNotExist:
            redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,*args,**kwargs):
        form = self.form_klass(instance=self.object)
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)


class DeleteView(View):
    object_klass = Clothes
    query_object = None

    def dispatch(self, request, *args, **kwargs):
        try:
            self.query_object = self.object_klass.objects.get(uuid=kwargs['cloth_id'])
        except self.object_klass.DoesNotExist:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, cloth_id):
        if request.user == self.query_object.user:
            remove(self.query_object.image.path)
            self.query_object.delete()
            return redirect('index')
        raise Http404('Failed to delete')
