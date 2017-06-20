# BrickWeb
Brick Framework Repository (Web)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python 3.4.0 or higher

### Installing

Create a virtual env

```
$ sudo pip3 install virtualenv
...

$ virtualenv-3.3 agruppaenv
Using base prefix '/usr'
New python executable in myenv/bin/python3
Also creating executable in myenv/bin/python
Installing setuptools, pip...done.

$ source agruppaenv/bin/activate  # This is important!

```

Then install all the software contain in requirements.txt

```
$ pip3 install -r /path/to/requirements.txt
```

### Running

Make the migrations for the data base
```
$ python3 manage.py makemigrations
```

Migrate the data base
```
$ python3 manage.py migrate
```

Then run the server
```
$ python3 manage.py runserver
```
It will be running at your localhost

### Running Tests

Run test for each app
```
$ python3 manage.py test
```

## GitFlow

* Master
* Release  
* Develop 
  * Feature 1
  * Feature 2
    
## Coments Conventions

```
# Function description
#
# @date [dd/mm/yy]
#
# @author [Author's name]
#
# @param [Type] Name Description
#
# @returns [Type] Name Description
#
```

## Built With

* [Django](https://docs.djangoproject.com/en/1.10/) - The web framework used
