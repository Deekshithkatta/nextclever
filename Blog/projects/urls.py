from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^project/$', views.projects, name="project")
]