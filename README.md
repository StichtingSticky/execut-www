# exeuct_www

Very basic web app for the exec(ut) website. 

## Description

execut_www runs on Django (version 3.0.6 to be exa(ct), but given the simplicity, don't worry about it too much. This will work on any Django version >= 3). The Python version used is 3.7, but it will work on any Python version >= 3. 

## Installation

Clone the project, create a virtuelenv (by using Pipenv or Poetry or any tool you like), set up the environment variables, set up a database (or let Django create one for you in SQLite, but then you'll have to change your settings.py). Run Pipenv install to install all the dependencies. When you're all set, run migrations (`python manage.py migrate`), run `python manange.py runserver`, and there you are!

## Other remarks
* Business logic should be handled in the models. Views should be as clean as possible. You are welcome to disagree, but do realize you are dead wrong. I love fatty models.