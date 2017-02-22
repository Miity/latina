from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from latina import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('pages.urls')),
    url(r'^blog/', include('blog.urls',  namespace='blog')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)