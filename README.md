"# OsloCityBikeAvailabilityViewer" 
This application creates a simple web page showing the current availability of Oslo City Bikes, using this API https://developer.oslobysykkel.no/api.  
It requires Python 3.6 with Django framework to run.
### Build Instructions ###

Install anaconda python 3.6: https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe, https://www.anaconda.com/download/ .
Install django, start the Anaconda command line prompt
```cmd
 PIP install django
```


### Running the application
Clone this repository.
Modify oslocitybikeapiconfig.json and update "Client-Identifier":  with  your client spec.

In the anaconda command line prompt type 
```cmd
python manage.py runserver 
```
in the root folder. This will start the local webserver.
View the webpage here: http://127.0.0.1:8000/OsloCityBikeAvailabilityViewer/

### About the code
#### OsloCityBikeAvailabilityViewer/services.py
This file contains the main functionality for reading the BySykkel API and handles the logic needed for creating the list.

#### OsloCityBikeAvailabilityViewer/views.py
Contains the top level entry point to displaying the webpage. All error handling is handled here.

#### OsloCityBikeAvailabilityViewer/templates/OsloCityBikeAvailabilityViewer.html
This is the template page for the HTML output.

#### exampleofoutput.png
png file showing how the output will look like in Chrome.

#### oslocitybikeapiconfig.json
Config file to be updated with your client identifier.


