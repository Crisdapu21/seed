from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    # Base see urls
    url(r'^', include('apps.website.urls')),
    url(r'^users/', include('apps.users.urls')),
    
    #  project urls
    #url(r'^$', include('apps.custom_app.urls')),

    # Default Admin urls
    url(r'^admin/', admin.site.urls),
]
