# Django Polls App

This repository contains the complete code for the [Django](https://www.djangoproject.com/) Project [tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/) `polls` app. 

The code is similar to what you would have after KU Polls Iteration 3, where each user gets one vote per poll, and he can change his vote.

## Installation

The application requires Python 3.8 or newer, Sqlite, Django 4.x, and `python-decouple`.

The migrations have all been run and data added to the database, should it should be ready to use.

1. (Optional) Create a virtual environment and start it.
2. (Optional) Install required Python packages if you don't have them: `pip install -r requirements.txt`


## Running the application

In a shell window, *optionally* using a virtual environment, enter:

```bash
 python manage.py runserver
```

And use a web browser to navigate to [http://localhost:8000/polls/](http://localhost:8000/polls/).

## USERS

There are 20 demo users available.     
demo1, demo2, ..., demo10 have submitted votes for the polls.    
demo11, ..., demo20 have not voted yet. So you have plenty of users for testing.

| User      | Role and Password |
|:----------|:------------------|
| demo1     | voter, password *Hackme1*  |
| demo2     | voter, password *Hackme2*  |
| demo**k**   | voter, password *Hackme****k***, **k** = 1, ..., 20 |
| admin     | admin user, pass `@isp2022`. You shouldn't need this. |
---

## Recreate The Database

You should **not** need to do this, but FYI the steps are as usual:

1. Delete the old database file.
2. Run migrations `python manage.py migrate`
3. Load table data from fixture files `python manage.py loaddata data/*.json`
