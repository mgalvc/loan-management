from django.contrib import admin
from django.urls import path, include
from proposals.api import urlpatterns as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls))
]
