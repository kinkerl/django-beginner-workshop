Template Language
------------------

* Absichtlich:

  * Einfacher Syntax
  * !KEINE LOGIK!

* Wurde von vielen kopiert



Template Language
------------------

* Tags: ``{% if %}``, ``{% endif %}``, ``{% load static %}``
* Filter: ``{{project.name|lower|striptags|truncatewords:2 }}``
* Vererbung: ``{% extends "base.html" %}``, ``{% block content %}``


.. note::
   * Die Logik dahinter ist nicht wie bei z.B. PHP-includes
   * Man kann sehr einfach eigene Tags/Filter schreiben https://docs.djangoproject.com/en/1.7/ref/templates/builtins/


----

Template auffindbar machen
---------------------------

``portfolio/settings.py``

.. code-block:: python

   TEMPLATE_DIRS = (
       # Always use forward slashes, even on Windows.   
       # Don't forget to use absolute paths, not relative paths.   
       os.path.join(BASE_DIR, 'templates'),
   )


----


Template-HTML
------------------

``templates/core/index.html``

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
       return render_to_response('core/index.html', context_dict,    context)





----

Statische Medieninhalte
------------------------

``portfolio/settings.py``

.. code-block:: python


   STATIC_PATH = os.path.join(PROJECT_PATH,'static')
   
   STATIC_URL = '/static/' # You may find this is already defined as    such.   
   
   STATICFILES_DIRS = (
       STATIC_PATH,
   )

.. note::
	 Statische Inhalte sind anders zu behandeln als Medieninhalte.

----

Im Template
------------

``templates/core/index.html``

.. code-block:: html


   {% load static %}
   
    <img src="{% static "mylogo.jpg" %}" alt="Picture" />


----

Assets einbinden
--------------------

.. code-block:: html

        <link rel="stylesheet" href="{% static "css/base.css" %}" /> <!-- CSS -->
        <script src="{% static "js/jquery.js" %}"></script> <!-- JavaScript -->

----

Medieninhalte
----------------

.. code-block:: python

   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') 


----



Ausliefern von Medieninhalten
-----------------------------

``urls.py``

.. code-block:: python

   from django.conf import settings
   
   if settings.DEBUG:
       urlpatterns += patterns(
           'django.views.static', (r'media/(?P<path>.*)', 'serve',
           {'document_root': settings.MEDIA_ROOT}), )


----


Übung: "Über mich"-Seite
-------------------------

.. note::
   https://docs.djangoproject.com/en/dev/ref/templates/builtins/#url
