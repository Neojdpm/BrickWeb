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
# ===========================================================================
# Function Name: any_function($functionArguments)
# ===========================================================================
# Author:      Nombre y apellido del autor (Correo)
# Consultant:  [Nombre y apellido del Consultor Funcional (Correo)]
# Version:     1.0.0
# ===========================================================================
# Purpose:     Breve descripción. Debe reflejar lo que hace la 
#              función y si utiliza algún algoritmo o método conocido.
#
# ===========================================================================
# Input:       
#          @arguments: Nombre del argumento, debe ser mnemónico
#                     Tipo de variable del argumento
#                     Descripción del argumento
#          Tables:
#          Screen / View:
#          JsonCode:
# Output:
#          @returns   Retornos, nombre, debe ser mnemónico
#                     Tipo de variable de salida
#                     Descripción
#            Tables:
#          Service_JsonCode
# Control & Parameters:
#          Variables de control del programa = Parámetros de la función y Globales
#          Parámetros de operación y configuración
#          Operaciones permitidas en cada estado
# Error Return:
#          Indicar Código y Descripción de mensaje(s) de error
# Services:
#          Detectar a tiempo servicios necesarios 
#          ya disponibles o por desarrollar
#      
# Private Functions:
#          Indicar funciones privadas de ésta función y
#          contenidas en este archivo
# Comments: 
#      …..
#      …..
#      
# ===========================================================================
# History:
#  Version 1.0.1              2005-10-14
#     Author:      Pedro Perez (PPerez@yahoo.com)
#     Description; Removed unnecesary code and fixed some minor bugs
# 
#  Version 1.0.0              2005-10-09
#     Author:      Nombre del autor (CorreoAutor@idbcgroup.com)
#     Description: Initial Release. Creación
#
#
#  Acknowledgements  *******
#      Indicar si se desea reconocer la contribución y/o ayuda de
#      alguien  …
#      …..
# ===========================================================================
function Nombre de la función (Arg01, Arg02, Arg03 ….ErrCode) 
{
   Código de la función 
 
#      Commented code *** for debugging purposes only **  ELIMINAR ESTOS CASOS
 
   return Errcode;
}
# ====== End of function =======================
#
#***** helper functions *******************************************
#
#=================================================================*\
  # Name:    string_at($string, $start, $string_length, $list)

```

## Built With

* [Django](https://docs.djangoproject.com/en/1.10/) - The web framework used