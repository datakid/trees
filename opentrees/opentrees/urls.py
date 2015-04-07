from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'opentrees.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^trees/', include('trees.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
