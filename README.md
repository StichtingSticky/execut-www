# exeuct_www

Very basic web app for the exec(ut) website. 

## Description

execut_www runs on Django (version 3.0.6 to be exa(ct), but given the simplicity, don't worry about it too much. This will work on any Django version >= 3). The Python version used is 3.7, but it will work on any Python version >= 3. 

## Installation for development

Clone the project, create a virtuelenv (by using Pipenv or Poetry or any tool you like), set up the environment variables, set up a database (or let Django create one for you in SQLite, but then you'll have to change your settings.py). Run Pipenv install to install all the dependencies. When you're all set, run migrations (`python manage.py migrate`), run `python manange.py runserver`, and there you are!

## The .env variables required

DEBUG - should be 'False' while in production
DATABASE_URL - in the form postgresql://postgres:password@127.0.0.1:5432/execut_www
SECRET_KEY - can be any generated random secret, as long as it does not change
ALLOWED_HOSTS - all hosts on which this application should be available
AWS_ACCESS_KEY_ID - AWS access key ID
AWS_SECRET_ACCESS_KEY - AWS access key secret
AWS_BUCKET_NAME - AWS bucket name