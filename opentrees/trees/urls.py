from django.conf.urls import url

from .views import TreeCreate, TreeUpdate, TreeDelete, TreeDetail, TreeList

urlpatterns = [
    url(r'^$', TreeList.as_view(), name='index'),
    url(r'^add/$', TreeCreate.as_view(), name='tree_add'),
    url(r'^(?P<pk>[0-9]+)/$', TreeDetail.as_view(), name='tree_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', TreeUpdate.as_view(), name='tree_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', TreeDelete.as_view(), name='tree_delete'),
]
