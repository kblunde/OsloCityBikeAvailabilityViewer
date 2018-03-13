"# OsloCityBikeAvailabilityViewer" 
This application creates a simple web page showing the current availability of Oslo City Bikes.  
It requires Python 3.6 with Django framework to run.
### Build Instructions ###

Install anaconda python 3.6: https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe, https://www.anaconda.com/download/
Start the anaconda command line prompt
Install django: PIP install django


### Running the application
Clone this repository.
Modify oslocitybikeapiconfig.json and update "Client-Identifier":  with  your client spec.
In the anaconda command line prompt type python manage.py runserver in the root folder. This will start the local webserver.
View the webpage here: http://127.0.0.1:8000/OsloCityBikeAvailabilityViewer/
