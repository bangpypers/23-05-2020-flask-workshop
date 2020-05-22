# Flask Workshop

This workshop is a basic introduction to Flask, a popular webframework for
Python. Flask allows you to build Web applications in a simple way. An alternate
is Django, which follows a batteries-included approach. Flask follows the
opposite approach.

Flask can be used to build many things, from complex web applications to IoT
projects such as the trainer's [Speaking Bookshelf](https://youtu.be/aEYftBZz6ag).

## About the Instructor

Vinay Keerthi is a self-taught programmer who has been meddling with, and
breaking computers since he was 14. His first computer was an Atari 600XL,
which he used to program in BASIC. His programming interests include Python,
MicroPython and Rust. He is currently writing a book on MicroPython which
will be published by Apress around December 2020.

## Agenda

1. Basics
    1. Decorators and Getting Started
    2. Add HTML to the content of the home page.
    3. Move HTML to a template page.
    4. Add a second page.
    5. Modularize both pages.
2. Routes
    1. GET and queries
    2. Using Postman
    3. POST
    4. PUT
    5. DELETE
3. Debugging with VS Code.
    1. Adding a `launch.json` file
4. Adding a Database
    1. flask-sqlalchemy
    2. db.Model example table
    3. Adding a second table.
5. Flask shell
    1. Using flask-shell to debug.
    2. Adding values to the database.
    3. Quering values
    4. Removing values from the database.
6. Front-End
    1. Adding Bootstrap CSS.
    2. Adding a simple template.
    3. A simple form.
7. Flask Modularization
    1. moving files.
    2. loading database later.
    3. logging
8. Creating an Application
    1. Home page
    2. Designing the API with Stoplight Studio
    3. Adding tables.
    4. Adding API routes
    5. Adding helper command to `flask` CLI to load data.
    6. Movie display page.
    7. Adding javascript for `onClick`
    8. Adding a \user\selected page to display all the selections
    9. Logging to a file
    10. Running with gunicorn (linux and mac only)
    11. Writing tests with pytest-flask
    12. Dockerfile!


## Installation

Make sure you install Python 3.6 or greater. Use Anaconda or Miniconda if you
don't know how.


Then follow these steps.

```bash
# Windows users, make sure you have git installed.
git clone https://github.com/bangpypers/23-05-2020-flask-workshop.git
cd 23-05-2020-flask-workshop
python -m venv env
source env/bin/activate # use just env\bin\activate.bat for Windows
pip install -r requirements.txt
```

This is enough to get you setup for the workshop.


## Using the Tags

This repository will always have a `master` branch that is latest with the
final state of the application. However, that will be daunting for anyone to
read through. So, please make continuous use of the tags that I have put together
to rewind to older states of the application.

### Listing all Tags

To list all tags: `git tag -l -n9`


### Rewinding the App

To rewind the app to a specific tag, use the following command:

```bash
git checkout v0.1
```

You can feel free to make changes or play around with the application.

### Fast-forwarding the App

Just checkout a later commit:

```bash
git checkout v0.9
```

The decimal portion of the application version will correspond to the agenda.


## Running the App

In v0.2.x, the way you run the app is a very simple operation.

```bash
python app.py
# OR
FLASK_APP=app.py FLASK_DEBUG=1 flask run
```

Open [this page](http://localhost:5000) on your browser.

To check out the search URL, try this [page](http://localhost:5000/search?query=pink+socks).

### Trying httpie to test the API

You can use the `http` command to test the API.

```bash
http http://localhost:5000/json-example
```
Note: Ensure you have installed httpie using:

```bash
pip install -r requirements.txt
```


The output I get is:
```
HTTP/1.0 200 OK
Content-Length: 96
Content-Type: application/json
Date: Fri, 22 May 2020 17:26:39 GMT
Server: Werkzeug/1.0.1 Python/3.8.3

{
    "animal": "Cat",
    "name": "John Doe",
    "place": "Amsterdam",
    "thing": "Volleyball"
}
```

## Using Postman to Test the API

Sometimes it is easier to use a GUI to
check your API. Postman is one such app for this.

![Postman Image](screenshots/00_postman.png)


## Reading the source code:

The easiest way to read the final application is from the `app.py` file. The
function `create_app` is your entrypoint into the application.


## About Routes

This section explains a bit about routes and queries.

### Routes

When you visit a URL you are probably used to seeing the `https://www.google.com/` portion of the website. Everything following the first `/` after the `.com` (this could be `.org` or `.in` or anything else) is the *route* for the page.

For your site, when you visit `http://localhost/`, the default *route* is the
*index*. This is `/`. We added a `/about` route, mapping a page to it.

If you noticed in the first example, we *don't* need to return **html**
content for a request. We can return anything, really.

### Types of Routes

#### GET

The default type of request is *GET*. This can be interpreted literally.
*Get* what I asked for.

`http://localhost/` means *get the index route of http://localhost*.

`http://localhost/about` means *get the about route of http://localhost*.


### Data in routes

Routes sometimes have meaningful data in them. A good analogy is to think
of a route as a postal address.

In API terms:

```
charlie
road #42
ChocolateFactory
```

could become:

```/ChocolateFactory/road/42/charlie```

Note that this does not follow any sort of standard on how APIs *should*
look, but this is quite feasible.


## About Queries

A query is the *second* easiest way to pass data to a route. You have used
queries millions of times without realizing it. Google uses a query to
lead you to the search results: `https://www.google.com/search?q=how+do+I+use+google`.
the `?q=...` portion is just a query where the API gets the values after `?`
as an accessible string.


## Free Resources

1. [Flask Website](https://flask.palletsprojects.com/en/1.1.x/)
2. [Flask Mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
3. [Explore Flask](http://exploreflask.com/en/latest/)
4. Git Tutorial [videos](https://git-scm.com/videos) [Pro-Git Book](https://git-scm.com/book/en/v2)
5. [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
6. [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
7. [SQL Tutorial on Postgres Documentation](https://www.postgresql.org/docs/10/tutorial.html)
8. [Postman](https://www.postman.com/)
9. [StopLight API Design Tool](https://stoplight.io/)
10. [httpie Commandline tool](https://httpie.org/)
11. [Real Python Decorators Tutorial](https://realpython.com/primer-on-python-decorators/)
12. [Real Python Virtualenv Primer](https://realpython.com/python-virtual-environments-a-primer/)

## Contacting the Author

Vinay goes by @stonecharioteer everywhere. [Twitter](https://twitter.com/stonecharioteer) is an easy way to reach
him, or reddit, if you are brave enough.
