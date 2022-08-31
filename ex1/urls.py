# TODO - check path and url dependencies and resolve correct url indexing

from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]

