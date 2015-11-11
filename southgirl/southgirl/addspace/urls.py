from django.conf.urls import patterns, include, url
from southgirl.addspace import addspace

urlpatterns = patterns('',
    url(r'^$',addspace.addspace,name='addspace'),
    url(r'^addspace/',addspace.addspace,name='addspace'),
    url(r'^convert/',addspace.convert,name='convert'),
)