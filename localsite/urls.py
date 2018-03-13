from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('OsloCityBikeAvailabilityViewer/', include('OsloCityBikeAvailabilityViewer.urls')),
    #not needed yet
    #path('admin/', admin.site.urls),
]