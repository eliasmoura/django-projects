from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog import views
from models import Postagem
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),
    url(r'^admin/$', include(admin.site.urls), name='admin'),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<numpag>[0-9]+)/$', views.home, name='numhome'),
    url(r'^arquivo/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', 
        views.arquivo, name='arquivo'),
    url(r'^categorias/$', views.categorias, name='categorias'),
    url(r'^categorias/([a-z]+)?[/]?$', views.categorias, name='vcategorias'),
    url(r'^categoria/(?P<slug>[\w_-]+)/$', views.categoria, name='categoria'),
    #rl(r'^categoria/([a-z+#-_0-9]+)?[/]?$', views.categoria, name='categoria'),
    url(r'^post/(?P<slug>[\w_-]+)/$', views.postagem, name='postagem'),
)
