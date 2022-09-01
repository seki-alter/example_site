# TODO - check path and url dependencies and resolve correct url indexing

from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index, name='index'),

    # ex: /ex1/5/
    re_path(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),

    # ex: /ex1/5/results/
    re_path(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),

    # ex: /ex1/5/vote/
    re_path(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

]
