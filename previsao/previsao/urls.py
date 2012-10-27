from django.conf.urls import patterns, include, url
from django.contrib import admin
import report
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'previsao.views.home', name='home'),
    url(r'^$', 'report.views.home' ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
