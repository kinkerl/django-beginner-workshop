Template Language
------------------

* Absichtlich:

  * Einfacher Syntax
  * !KEINE LOGIK!

* Wurde von vielen kopiert


----


Template Language
------------------

* Tags: ``{% if %}``, ``{% endif %}``, ``{% load static %}``
* Filter: ``{{project.name|lower|striptags|truncatewords:2 }}``
* Vererbung: ``{% extends "base.html" %}``, ``{% block content %}``


.. note::
   * Man kann sehr einfach eigene Tags/Filter schreiben https://docs.djangoproject.com/en/1.7/ref/templates/builtins/



----


Template-HTML
------------------

``core/templates/index.html``

.. code-block:: html

   <!DOCTYPE html>
   <html>
       <head>
           <title>Portfolio</title>
       </head>
       <body>
           <h1>Hi!</h1>
           {{ message }}
       </body>
   </html>

----



Template in der View verwenden
-------------------------------

``core/views.py``

.. code-block:: python

   from django.template import RequestContext
   from django.shortcuts import render_to_response

   def index(request):
       context = RequestContext(request)
       context_dict = {'message': "Ich komme aus dem context_dict"}
       return render_to_response('index.html', context_dict,    context)





----

Statische Medieninhalte
------------------------

``portfolio/settings.py``

.. code-block:: python

   STATIC_URL = '/static/'


.. note::
	 Statische Inhalte sind anders zu behandeln als Medieninhalte.

----

Im Template
------------

``core/templates/index.html``

.. code-block:: html


   {% load staticfiles %}

    <img src="{% static 'example.jpg' %}" alt="Picture" />

.. note::
         Das Bild dazu muss unter core/static/example.jpg liegen.

----

Assets einbinden
--------------------

.. code-block:: html

        <link rel="stylesheet" href="{% static 'css/base.css' %}" />
        <script src="{% static 'js/jquery.js' %}"></script>


----


Übung: "Über mich"-Seite
-------------------------

* Entwickele eine eigene "über mich"-Seite
* Url verlinkungen mit dem URL Tag:
  https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#url
