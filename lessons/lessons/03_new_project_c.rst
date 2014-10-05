
Ein Portfolio
--------------------------

* Seiten
 
   * Startseite mit Projektübersicht 
   * Projektdetailseite
   * Kontaktformular

* Design nach Bedarf
  (http://getbootstrap.com/)

----

Datenmodell für unsere Seite
----------------------------

.. comment:
   http://www.nomnoml.com/#view/#direction:%20right%0A#edgeMargin:10%0A#zoom:1.5%0A%0A%0A[Kategorie|%0A%20%20Name:%20CharField%0A|]%0A[Projekt|%0A%20%20Name:%20CharField%0A%20%20Beschreibung:%20TextField%0A|]%0A[Kategorie]o-[Projekt]%0A%0A[Kontaktanfrage|%0A%20%20Absender:%20EmailField%0A%20%20Text:%20TextField%0A|]
   
   #direction: right
   #edgeMargin:10
   #zoom:1.5
   
   
   [Kategorie|
     name: CharField
   |]
   [Projekt|
     name: CharField
     copy: TextField
   |]
   [Kategorie]o-[Projekt]
   
   [Kontaktanfrage|
     sender: EmailField
     copy: TextField
   |]

.. image:: ../_static/project_orm.png
    :width: 50%

----


virtualenv (venv)
-----------------

* Kapseln der Python Pakete in einer unabhängigen "Installation"
* Unterschiedliche Projekte können unterschiedliche Abhängigkeiten bekommen
* Volle Unterstützung von pip
* Keine root-Rechte für Installation von Paketen

----

venv einrichten
---------------

.. code-block:: console

   user@hostname:$ virtualenv venv
   New python executable in venv/bin/python
   Installing setuptools, pip...done.

   user@hostname:$ source venv/bin/activate

   (venv)user@hostname:$ deactivate 

   user@hostname:$

.. note::
   Man kann auch virtualenv wrapper verwenden. 
   Je nach Situation kann dieser Arbeit abnehmen. 
   
   http://virtualenvwrapper.readthedocs.org/en/latest/

----



django installieren
--------------------

.. code-block:: console

   $ pip install django==1.6.5
   $ pip install psycopg2
   $ pip freeze

.. warning::
	Für diesen Befehl und für alle weiteren Befehle muss man die venv aktiviert haben.


----

django installieren 2
--------------------------

.. code-block:: console

   $ python -c "import django; print(django.get_version())"
   1.6.5


----

Das django admin tool
---------------------

.. code-block:: console

   $ django-admin startproject portfolio


----

:class: slidecenter

Was wurde erstellt?
---------------------

.. note::
   Besonders wichtig sind:
   
     * manage.py
     * settings.py
     * urly.py
     * wsgi.py

----

settings.py
-----------


.. code-block:: python

   import os
   SETTINGS_DIR = os.path.dirname(__file__)
   PROJECT_PATH = os.path.abspath(
      os.path.join(SETTINGS_DIR, os.pardir))

.. note::
   Bitte immer ``os``-Funktionen nutzen wenn man mit Pfaden arbeitet.
----


runserver
---------

* Einfacher debugging Server
* NICHT(!) produktiv nutzen
* autoreload (fehlerhaft) 


----

runserver starten
------------------

.. code-block:: console

   $ python manage.py runserver 0.0.0.0:8000   
   Validating models...
   
   0 errors found
   September 15, 2014 - 17:49:54
   Django version 1.6.5, using settings 'portfolio.settings'
   Starting development server at http://0.0.0.0:8000/
   Quit the server with CONTROL-C.

----


It worked!
---------------------

.. image:: ../_static/screenshots/django-startproject.png
    :width: 100%

