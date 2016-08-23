from django.conf.urls import url, include,patterns
from userlogin import views


urlpatterns=patterns('',
    url(r'^$', views.post_comment,name='post_comment'),
    url(r'^add_like/$', views.add_like, name='add_like'),


)
