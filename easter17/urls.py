from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import egghunt.views

# Examples:
# url(r'^$', 'easter17.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', egghunt.views.index, name='index'),
    url(r'^db', egghunt.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
