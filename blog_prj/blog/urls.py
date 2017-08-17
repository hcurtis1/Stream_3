from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^top5posts/$', views.top_post),
    url(r'^top5posts/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
]
