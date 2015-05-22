from django.conf.urls import include, url
from django.contrib import admin

from website import urls as website_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(website_urls))
]
