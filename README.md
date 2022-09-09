# Travel-Agency-Site
## Django Based Website with authentication

The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/SoftCysec/Travel-Agency-Site.git
$ cd Travel-Agency-Site
```
Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip3 install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip3` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`

work your way through the `MVT-Model View Template` of the project to get to know how it works
