from django.conf.urls import patterns, include, url

from django.contrib import admin

from sdktest.views import default, chargingresponse, query, refund, chargingiframe, chargingredirect, chargingmaster, chargingminimal

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^chargingminimal/$', chargingminimal),
                       url(r'^chargingmaster/$', chargingmaster),
                       url(r'^chargingiframe/$', chargingiframe),
                       url(r'^chargingredirect/$', chargingredirect),
                       url(r'^query/$', query),
                       url(r'^refund/$', refund),
                       url(r'^chargingresponse', chargingresponse),
                       url(r'^$', default),
                       url(r'^index/$', default),
)
