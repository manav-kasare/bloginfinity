from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from .models import Post


urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by('-created_on')[:25],
        template_name = 'dashboard/dashboard.html')),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'dashboard/post.html')),
]


