Das erste Model
---------------

.. image:: ../_static/project_orm.png
    :width: 50%

----

Datenbank
-----------

* PostgreSQL
* MySQL
* SQLite
* Oracle
* (MSSQL)
* (NOSQL)


----

SQLite
------------

``portfolio/settings.py``

.. code-block:: python

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_PATH, 'portfolio.db'),
       }
   }

.. warning::
   Niemals SQLite produktiv nutzen

----

PostgreSQL
-----------

``portfolio/settings.py``

.. code-block:: python

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'db_name',
           'USER': 'db_user',
           'PASSWORD': 'db_user_password',
           'HOST': ''
       }
   }


----

Models
-------

* Beschreibung von Daten in Python-Objekten
* Wir bekommen "geschenkt":

  * auto Validierungen
  * auto Forms
  * auto Admin


----


Models
-------

``core/models.py``

.. code-block:: python

  class Kategorie(models.Model):
      name = models.CharField(max_length=128, unique=True, help_text="Der Name")
      def __unicode__(self):
          return self.name

  class Project(models.Model):
      category = models.ForeignKey("Kategorie", related_name="projects", null=True)
      name = models.CharField(max_length=128, unique=True)
      def __unicode__(self):
          return self.name




----

Model Feld Typen
-----------------

* CharField / TextField
* URLField
* IntegerField
* BooleanField
* ImageField
* DateField
* ForeignKey / OneToOneField / ManyToManyField
* ...

.. note::
   https://docs.djangoproject.com/en/1.8/ref/models/fields/

----

Datenbank erstellen
--------------------

.. code-block:: console

   $ python manage.py migrate

----

.. code-block:: console

   $ python manage.py makemigration core

----


.. code-block:: console

   $ python manage.py migrate

----



Shell debugging
----------------

.. code-block:: console

   $ python manage.py shell

----


Shell debugging 2
-------------------

.. code-block:: python

   >>> from core.models import Project

   >>> print Project.objects.all()
   []

   >>> p = Project(name="Test")

   >>> print Project.objects.all()
   []

   >>> p.save()

   >>> print Project.objects.all()
   [<Project: Test>]

   >>> quit()

.. note::
   * Daten lesen / schreiben:

     * all()
     * filter(...)
     * get(...)
     * order()
     * save()

   * Chaining bei QuerySets
   * Field Lookups
   * Genelle Informationen zum Query erstellen: https://docs.djangoproject.com/en/1.11/topics/db/queries/#field-lookups

----



:class: slidecenter

django Admin
----------------

.. note::
  Der Admin funktioniert über Introspection im Gegensatz zu zum Beispiel Ruby on Rails.

----


django Admin: aktivieren
------------------------

.. code-block:: python

   INSTALLED_APPS = (
       'django.contrib.admin', #hier
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'core',
   )

.. note::
   Bei neuen django Installationen ist der Admin schon aktiviert.

----


:class: slidecenter

django Admin Demo
------------------

.. note::

    /admin


----


Models am admin registrieren
------------------------------


``core/admin.py``

.. code-block:: python

   from django.contrib import admin
   from core.models import Project

   admin.site.register(Project)

----



Populate-Skript
-----------------

``populate.py``

.. code-block:: python

   import os
   
   def populate():
       Project.objects.get_or_create(name="myProject")
       #....

       for p in Project.objects.all():
           print p

   if __name__ == '__main__':
       print "Starting Population script..."
       os.environ.setdefault('DJANGO_SETTINGS_MODULE',
           'portfolio.settings')
       import django
       django.setup()
       from core.models import Project
       populate()

----


Der Adminuser im Template
--------------------------

``core/templates/index.html``

.. code-block:: html

   {% if user.is_authenticated %}
      nice to see you
   {% else %}
      who are you
   {% endif %}

----


:class: slidecenter

Admin Showcase
--------------

Was so geht ...
