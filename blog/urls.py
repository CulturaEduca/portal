from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(\d+)/$', 'blog.views.listagem', name='blog_post'),
    url(r'^/?$', 'blog.views.listagem', name='blog'),
    url(r'^(?P<slug>[-\w]+)/$', 'blog.views.post', name='post'),
)