from django.conf.urls import url

from .views import TreeCreate, TreeUpdate, TreeDelete, TreeDetail, TreeList

urlpatterns = [
    url(r'^$', TreeList.as_view(), name='index'),
    url(r'^add/$', TreeCreate.as_view(), name='tree_add'),
    url(r'^(?P<slug>[-\w]+)/$', TreeDetail.as_view(), name='tree_detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', TreeUpdate.as_view(), name='tree_update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', TreeDelete.as_view(), name='tree_delete'),
]
