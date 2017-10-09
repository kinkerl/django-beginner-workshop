
django
---------

* MVT-Webframework
* Python 2/3
* Aktuelle Version 1.11 LTS
* Pluggability
* Don't repeat yourself (DRY)
* Introspection

.. note::
   * Benannt nach Django Reinhardt, Gitarrist
   * Kommt aus der Zeitungswelt

----


Wo wird django genutzt?
-----------------------

* disqus
* Pinterest
* Instagram
* Mozilla
* NASA

----

Was beinhaltet django?
----------------------

* Webserver
* Middleware
* URL-Dispatcher
* Views
* Models: ORM-Mapper
* Form-Validator
* Admin-Interface
* Templates
* ...


----

(Stark vereinfachter) Requestablauf
------------------------------------



.. comment:
   http://www.nomnoml.com/#direction:%20right%0A#edgeMargin:%2010%0A#zoom:1.5%0A%0A[<start>st]->[runserver]%0A[runserver]->[Middlewares]%0A[Middlewares]->[URL-Dispatcher]%0A[URL-Dispatcher]->[View]%0A[View]--[Models]%0A[Models]-[<database>DB]%0A[View]->[Template-Engine]%0A[Template-Engine]--[Models]%0A[Template-Engine]->[Middlewares]%0A[Middlewares]->[runserver]%0A[runserver]->[<start>st]

   #direction: right
   #edgeMargin: 10
   #zoom:1.5

   [<start>st]->[runserver]
   [runserver]->[Middlewares]
   [Middlewares]->[URL-Dispatcher]
   [URL-Dispatcher]->[View]
   [View]--[Models]
   [Models]-[<database>DB]
   [View]-->[Middlewares]
   [View]-->[Template-Engine]
   [Template-Engine]--[Models]
   [Template-Engine]->[Middlewares]
   [Middlewares]->[runserver]
   [runserver]->[<start>st]

.. image:: ../_static/django_structure.png
    :width: 100%

.. note::
   Ein Request Object hat alle Informationen zu dem Request.
   Unter anderem Context-Variablen, Post/Get, URL, Languages.




----

Bei Fragen
--------------

* Google
* Offizielle Dokumentation: https://docs.djangoproject.com/
