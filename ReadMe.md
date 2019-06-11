# O imóvel certo.com

Website for a challange, that simulates an online rental service.

## To run at development environment

Application built using Django 2.0.7 and you should have Python 3.7.0 to works correctly!

First, create a python virtualenv at oimovelcerto/

~/oimovelcerto$ python3 -m venv myvenv

Create a database file in the directory:

python manage.py migrate

Then run the dependencies (you can use pip):

pip install jinja2

pip install pillow

So start the web server by running

python manage.py runserver

Now you can enter 127.0.0.1:8000 and start to use it! Click on "Cadastre seu imóvel aqui" to submit yours properties so you can make a search by region typing your desired neighborhood on the filed "Faça uma busca por bairro".

I hope you enjoy it!
