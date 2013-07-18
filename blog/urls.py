from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', views.home, name='home'),
    url(r'^blog/$', views.home, name='blog'),
    url(r'^categorias/$', views.categorias, name='categorias'),
    url(r'^categoria/(\d)/$', views.categoria, name='categoria'),
    url(r'^post/$', views.postagem, name='postagem'),
)
