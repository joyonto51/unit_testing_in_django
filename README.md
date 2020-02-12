# Unit Testing in Django
Please follow the instructions serially to setup this project.

## Create virtual environment
$`virtualenv venv --python=python3.6`

## Clone this repository
$`git clone https://github.com/joyonto51/unit_testing_in_django.git`

## Active the virtual environment
$`source venv/bin/activate`

## Go to the project directory
$`cd unit_testing_in_django`

## Install requirements
$`pip install -r requirements.txt`

## To migrate and run the project
$`python manage.py migrate & python manage.py runserver`

## Test the test cases
$ `python manage.py test`
#### To test a particular app
$`python manage.py test <app_name>`

## To run with coverage
$`coverage run manage.py run test`
#### Run with verbosity level-2 to see more details,
$`coverage run manage.py test -v 2`
##### For a particular app
$`coverage run manage.py test <app_name> -v 2`  
