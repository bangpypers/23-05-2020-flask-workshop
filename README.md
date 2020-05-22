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

1. Quick Introduction to Decorators
2. Introduction to Flask
3. Adding Routes
4. Debugging Flask with VS Code
5. Flask Modularization
6. Adding a Database
7. Creating a Front End
8. Managing a Large Application


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

In v0.1.1, the way you run the app is a very simple operation.

```bash
# first, learn about decorators
python decorators.py
# then continue to the app.
python app.py
```

Open [this page](http://localhost:5000) on your browser.


## Reading the source code:

The easiest way to read the final application is from the `app.py` file. The
function `create_app` is your entrypoint into the application.

## Free Resources

1. [Flask Website](https://flask.palletsprojects.com/en/1.1.x/)
2. [Flask Mega-tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
3. [Explore Flask](http://exploreflask.com/en/latest/)
4. Git Tutorial [videos](https://git-scm.com/videos) [Pro-Git Book](https://git-scm.com/book/en/v2)
5. Automate the Boring Stuff
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
