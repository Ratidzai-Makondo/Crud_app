from .models import App
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


class IndexView(ListView):
    model = App
    template_name = 'app/index.html'
    context_object_name = 'index'


class SingleView(DetailView):
    model = App
    template_name = 'app/single.html'
    context_object_name = 'post'


class PostsView(ListView):
    model = App
    template_name = 'app/posts.html'
    context_object_name = 'post_list'


class AddView(CreateView):
    model = App
    template_name = 'app/add.html'
    fields = '__all__'
    success_url = reverse_lazy('app:posts')


class EditView(UpdateView):
    model = App
    template_name = 'app/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('app:posts')


class Delete(DeleteView):
    model = App
    template_name = 'app/confirm-delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('app:posts')
