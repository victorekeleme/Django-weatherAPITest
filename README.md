# Django-weatherAPITest

## Setup
The first thing to do is to clone the repository

### git clone https://github.com/victorekeleme/Django-weatherAPITest.git

Create a virtual environment to install dependencies in and activate it:

### virtualenv env --no-site-packages
### source env/bin/activate

Then install the dependencies

### pip install -r requirements.txt

Once pip has finished downloading the dependencies:

### python manage.py runserver

### And navigate to http://127.0.0.1:8000


## Tests

The manual test cases are located at the base folder of the project

To run the automated scripts cd into the directory where manage.py is:

### python manage.py test functional_tests

This command runs all test scenerios from 1 to 5
when its done locate the results in the folder: weatherapitest/functional_tests/result/results.xlsx

### Note: You can only run the automation test cases when the server is not on.

### To end an on going server run use Ctrl + C 


