"""bloginfinity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import LoginView, LogoutView
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^login/$', LoginView.as_view(template_name = 'accounts/login.html')),
    url(r'^logout/$', LogoutView.as_view(template_name = 'accounts/logout.html')),
    url(r'^register/$', views.register, name="register"),
    url(r'^dashboard/profile/$', views.view_profile, name='view_profile'),
    url(r'^dashboard/profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^dashboard/newblog$', views.new_blog, name = 'new_blog'),
]
