from django.shortcuts import render
from django.views.generic import TemplateView
import sys, os
sys.path.append('OsloCityBikeAvailabilityViewer')
import services
# Create your views here.
from django.http import HttpResponse
import time

class BikePage(TemplateView):
    def get(self,request):
        bikelists = services.BikeList()
        bikelists.updateBike()
        print(bikelists.lastUpdated)
        context = {'timer': str(time.time()),
                   'bikelists': bikelists.stationInfo.items(),
                   'lastUpdated': bikelists.lastUpdated,
                   'refresh_rate': bikelists.refreshRate,
                   'data': bikelists.updateBike()
                   # 'updated': bikelists.updateBike()

                   }
        # output = str(time.time())
        # print(bikelists.lastUpdated)
        return render(request, 'OsloCityBikeAvailabilityViewer.html', context)
        #return render(request,''bysykkelapitest/books.html',books_list)