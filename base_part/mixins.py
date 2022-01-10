from os import remove

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect


class ContentMixin:
    context = {}
    template_name = None
    query_object = None
    obj_klass = None
    obj_id = None

    def update_context(self, **kwargs):
        if kwargs is None:
            return self.context
        self.context.update(**kwargs)

    def get_object_id(self, request):
        self.query_object = get_object_or_404(self.obj_klass, uuid=self.obj_id)
        context = {
            'cloth': self.query_object,
        }
        self.update_context(**context)

    def render_to_response(self, request, **kwargs):
        self.update_context(**kwargs)
        return render(request, self.template_name, self.context)


class FormMixin:
    form_klass = None
    object_klass = None
    object = None
    redirect_to = None
    obj_id = None
    type_func = None

    def validation(self,request):
        form = self.form_klass(request.POST, request.FILES,instance=self.object)
        if form.is_valid():
            if self.obj_id and self.object:
                if request.FILES:
                    remove(self.object_klass.image.path)
                form.save()
            else:
                self.object = form.save(commit=False)
                self.object.user = request.user
                self.object.save()
            return True

    def post(self,request,*args,**kwargs):
        if self.validation(request):
            if self.obj_id:
                return redirect(self.redirect_to,self.object.uuid)
            return redirect(self.redirect_to)
        return redirect(self.type_func)







class PaginationMixin:
    number_objects = 4

    def paginate(self, request):
        paginator = Paginator(self.objects, self.number_objects)
        page_number = request.GET.get('page')
        if not page_number:
            page_number = 1
        page_obj = paginator.get_page(page_number)
        self.context.update({'clothes': page_obj})
