from django.db import models
import utils
import urllib.request, json
from datetime import datetime, timedelta
class BikeList():
    config = json.load(open('oslocitybikeapiconfig.json'))
    pub_date = models.DateTimeField('date published')
    url = config['availability_url']
    req = urllib.request.Request(url)
    identifier = config['Client-Identifier']
    req.add_header("Client-Identifier",identifier)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    availabilityData = json.loads(data)
    timeobject = datetime.strptime(availabilityData['updated_at'], "%Y-%m-%dT%H:%M:%S+00:00")
    timeobject = timeobject + timedelta(hours=utils.findUTCOffest())
    lastUpdated = timeobject.strftime("%Y-%m-%d %H:%M   %A %B %S")
    refreshRate = availabilityData['refresh_rate'] * 1000
    url = config['stations_url']
    req = urllib.request.Request(url)
    identifier = "c71f0302a513ec0ff38145704f59e2ae"
    req.add_header("Client-Identifier",identifier)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    stationData = json.loads(data)
    stationInfo = {}
    for station in stationData['stations']:
        stationInfo[station['id']] = {}
        stationInfo[station['id']]['title'] = station['title']
        #print(stationInfo)
    counter = 0
    for station in availabilityData['stations']:
        id = station['id']
        #print(str(id) + "\n")
        if id not in stationInfo.keys():
            counter += 1
         #   print("Station id " + str(id) + " has unknown location")
        else:
            stationInfo[id]['bikes'] = station['availability']['bikes']
            stationInfo[id]['locks'] = station['availability']['locks']

    def updateBike(self):
        url = 'https://oslobysykkel.no/api/v1/stations/availability'
        req = urllib.request.Request(url)
        identifier = "c71f0302a513ec0ff38145704f59e2ae"
        req.add_header("Client-Identifier", identifier)
        resp = urllib.request.urlopen(req)
        data = resp.read()
        availabilityData = json.loads(data)
        timeobject = datetime.strptime(availabilityData['updated_at'], "%Y-%m-%dT%H:%M:%S+00:00")
        timeobject = timeobject + timedelta(hours=utils.findUTCOffest())
        self.lastUpdated = timeobject.strftime("%Y-%m-%d %H:%M   %A %B %S")
        self.refreshRate = availabilityData['refresh_rate'] * 1000
        url = 'https://oslobysykkel.no/api/v1/stations'
        req = urllib.request.Request(url)
        identifier = "c71f0302a513ec0ff38145704f59e2ae"
        req.add_header("Client-Identifier", identifier)
        resp = urllib.request.urlopen(req)
        data = resp.read()
        stationData = json.loads(data)
        stationInfo = {}
        for station in stationData['stations']:
            stationInfo[station['id']] = {}
            stationInfo[station['id']]['title'] = station['title']
            # print(stationInfo)
        counter = 0
        for station in availabilityData['stations']:
            id = station['id']
            # print(str(id) + "\n")
            if id not in stationInfo.keys():
                counter += 1
            #   print("Station id " + str(id) + " has unknown location")
            else:
                stationInfo[id]['bikes'] = station['availability']['bikes']
                stationInfo[id]['locks'] = station['availability']['locks']
        stationInfo['lastUpdated'] = self.lastUpdated
        self.stationInfo = stationInfo
        return self

    #def refresh(self):
     #   """ Reload an object from the database """
      #  self.updateBike()
       # return self.__class__._default_manager.get(pk=self.pk)

#print(str(counter) + " has unknown location, total " + str(len(availabilityData['stations'])))
#updated_at = availabilityData['updated_at']

#for station, value in stationInfo.items():
#    print(value)
#url = 'https://oslobysykkel.no/api/v1/stations/availability'
#req = urllib.request.Request(url)
#identifier = "c71f0302a513ec0ff38145704f59e2ae"
#req.add_header("Client-Identifier", identifier)
#while True:
    #resp = urllib.request.urlopen(req)
    #data = resp.read()
    #availabilityData = json.loads(data)
    #timeobject = datetime.strptime(availabilityData['updated_at'], "%Y-%m-%dT%H:%M:%S+00:00")
    #print(utcOffset_h)
    #timeobject = timeobject + timedelta(hours=utcOffset_h)
    #print(timeobject.strftime("%Y-%m-%d %H:%M   %A %B %S"))
    #time.sleep(availabilityData['refresh_rate'])