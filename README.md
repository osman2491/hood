# Hood

# Auother

Osman Mohamed Ali

# Discription

This is an application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

# User stories
The user should be able to:

 1. Sign in with the application to start using.
 2. Set up a profile about me and a general location and my neighborhood name.
 3. Find a list of different businesses in my neighborhood.
 4. Find Contact Information for the health department and Police authorities near my neighborhood.
 5. Create Posts that will be visible to everyone in my neighborhood.
 6. Change My neighborhood when I decide to move out.
 7. Only view details of a single neighborhood.

# Prerequisites

 Python3.6

# Installation

### To install, follow the following instructions;

    $ git clone 
    $ cd Hood
    $ source virtual/bin/activate
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver

# How to Prepare enviroment variables

Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it

    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'

# Technology used

1. Python3.6
2. Django 1.11
3. Heroku
4. Bootstrap


# License
This project is licensed under the MIT Open Source license, (c)