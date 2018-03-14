import utils
import urllib
import json
from datetime import datetime, timedelta


class BikeLocksAvailability:
    def __init__(self, bikes_input, locks_input):
        self.bikes = bikes_input
        self.locks = locks_input


class BikeAvailabilityReader:
    def __init__(self):
        """The configuration file  is read in the constructor"""
        config = json.load(open('oslocitybikeapiconfig.json'))
        self.__url = config['oslobysykkelurl']
        self.__identifier = config['Client-Identifier']
        self.status_string = ""
        self.refresh_rate = 100000
        self.last_updated = ""
        self.bike_availability_info = {}

    def read_and_set_status(self):
        status_data = self.read_endpoint("/status")
        if status_data['status']['all_stations_closed']:
            self.status_string = "All stations are now closed."
        else:
            self.status_string = "All stations are now open."

    def read_endpoint(self, endpoint):
        req = urllib.request.Request(self.__url + endpoint)
        identifier = self.__identifier
        req.add_header("Client-Identifier", identifier)
        resp = urllib.request.urlopen(req)
        data = resp.read()
        json_data = json.loads(data)
        return json_data

    def create_availability_data(self):
        self.read_and_set_status()
        availability_data = self.read_availability()
        stations_data = self.read_endpoint("/stations")
        station_info = {}
        for station in stations_data['stations']:
            station_info[station['id']] = station['title'] + ", " + station['subtitle']
        for station in availability_data['stations']:
            station_id = station['id']
            if station_id in station_info.keys():# we skip stations that has no location
                lock_bike_info = BikeLocksAvailability(station['availability']['bikes'], station['availability']['locks'])
                self.bike_availability_info[station_info[station['id']]] = lock_bike_info
        self.bike_availability_info = dict(sorted(self.bike_availability_info.items()))

    def read_availability(self):
        availability_data = self.read_endpoint("/stations/availability")
        try:
            updated_at = datetime.strptime(availability_data['updated_at'], "%Y-%m-%dT%H:%M:%S+00:00")  #GMT=0 is assumed
            updated_at = updated_at + timedelta(hours=utils.findUTCOffest())
            self.last_updated = updated_at.strftime("%A %B %d %Y %H:%M:%S")
        except Exception as e:
            self.last_updated = "Unable to determine when the page was last updated!" + str(e)
        self.refresh_rate = availability_data['refresh_rate'] * 1000
        return availability_data

