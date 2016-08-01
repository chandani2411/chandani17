from django.conf.urls import url, include,patterns
from userlogin import views


urlpatterns=patterns('',
    url(r'^$', views.post_comment,name='post_comment'),


)
