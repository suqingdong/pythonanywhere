from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from .models import Post

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


app_name = 'blog'

urlpatterns = [
    # /blog/
    url(r'^$', ListView.as_view(model=Post), name='index'),

    # /blog/2/
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Post), name='detail'),

    # /blog/add/
    url(r'^add/$', CreateView.as_view(model=Post, fields="__all__"), name='add-blog'),

    # /blog/2/update/
    url(r'^(?P<pk>\d+)/update/$', UpdateView.as_view(model=Post,
                                                     fields="__all__"), name='update-blog'),

    # /blog/2/delete/
    url(r'^(?P<pk>\d+)/delete/$', DeleteView.as_view(model=Post,
                                                     success_url=reverse_lazy('blog:index')), name='delete-blog')

]
