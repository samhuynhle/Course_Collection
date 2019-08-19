from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^addcourse$', views.add_course),
    url(r'^courses/destroy/(?P<course_id>[0-9]+)$', views.display_delete),
    url(r'^destroy/(?P<course_id>[0-9]+)$', views.process_delete),
    url(r'^courses/comments/(?P<course_id>[0-9]+)$', views.comments),
    url(r'^comments/(?P<course_id>[0-9]+)$', views.process_comments),
    url(r'^', views.index),
    
]