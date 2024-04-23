from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('djangoapp.urls')),
]

'''
from django.contrib import admin
from django.urls import path, include
from djangoapp.urls import urlpatterns as djangoapp_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclua as URLs do aplicativo 'djangoapp_urls'
    path('api/', include(djangoapp_urls)),
]
'''