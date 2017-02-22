from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.blog, name='BlogList'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.blog, name='BlogListByCategory'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.post_detail, name='PostDetail'),

    url(r'^post/addcomment/(?P<id>[0-9]+)/$', views.addcomment),
    url(r'^(\d+)/$', views.blog)
]
