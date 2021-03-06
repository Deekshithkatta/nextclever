from  django.conf.urls import  url,include
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     path('admin/', admin.site.urls),
     url(r'^about/$', views.about),
     url(r'^accounts/', include('accounts.urls')),
     url(r'', include('articles.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
