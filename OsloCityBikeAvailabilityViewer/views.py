from django.shortcuts import render
from django.views.generic import TemplateView
import urllib
import sys
sys.path.append('OsloCityBikeAvailabilityViewer')
import services
from django.http import HttpResponse


class BikePage(TemplateView):
    def get(self, request):
        try:
            bike_availability = services.BikeAvailabilityReader()
        except FileNotFoundError:
            return HttpResponse('Could not find file oslocitybikeapiconfig.json! Please verify that it exists'
                                'in the root folder".')
        except KeyError:
            return HttpResponse('Invalid oslocitybikeapiconfig.json! Please verify that the following data is available'
                                'in json file  oslobysykkelurl and Client-Identifier.')
        except Exception as e:
            return HttpResponse("Error " + str(e))

        try:
            bike_availability.create_availability_data()
            context = {'availability_lists': bike_availability.bike_availability_info,
                       'last_updated': bike_availability.last_updated,
                       'refresh_rate': bike_availability.refresh_rate,
                       'status_string': bike_availability.status_string
                       }
            return render(request, 'OsloCityBikeAvailabilityViewer.html', context)
        except urllib.error.HTTPError as e:
            return HttpResponse("HTTPError :" + str(e.code) +" " + str(e.reason) +
                                ". Unable to connect to OsloBysykkel endpoint!")
        except urllib.error.URLError as e:
            return HttpResponse("URLError: " + str(e.reason) + ". Unable to connect to OsloBysykkel endpoint!")
        except Exception as e:
            return HttpResponse("Error " + str(e))

