Models im Template
-------------------

* Liste

  * View erweitern
  * Template erweitern

* Detailseite

  * Neue View + URL-Mapping
  * Neues Template
  * Verlinkung von Liste


----


Models in Templates: View Liste
-------------------------------

``core/views.py``

.. code-block:: python

   from core.models import Project
   def index(request):
      #...
      project_list = Project.objects.all()
      context_dict = {'projects': project_list}
      #...
   
----

Template
---------------------------

``core/templates/index.html``

.. code-block:: html

   {% if projects %}
       <ul>
           {% for project in projects %}
              <li>{{ project.name }}</li>
           {% endfor %}
       </ul>
   {% else %}
       <strong>Keine Projekte</strong>
   {% endif %}



----

Model Detailseite: View Detail
------------------------------

``core/views.py``

.. code-block:: python

   from django.shortcuts import get_object_or_404
   from core.models import Project
   from django.template import RequestContext
   from django.shortcuts import render_to_response
      
   def project(request, project_id):
       context = RequestContext(request)
       project = get_object_or_404(Project, id=project_id)
       context_dict = {'project': project}
       return render_to_response('project.html', context_dict,    context)

.. note::
   Siehe auch get_list_or_404


----

Model Detailseite: URL-Mapping
-------------------------------

``core/urls.py``

.. code-block:: python

    url(r'^project/(?P<project_id>\d+)/$', views.project, name='project'),) 

.. note::
   Weitere Beispiele: 
   * (?P<project_name>\w+)
   * (?P<year>\d{4})
   * (?P<month>[a-z]{3})


----


Model Detailseite: Template
---------------------------

``core/templates/project.html``

.. code-block:: html

   <!DOCTYPE html>
   <html>
       <head>
           <title>Project</title>
       </head>   
       <body>
           <h1>{{ project.name }}</h1>
           <p>{{ project.copy }}</p>           
       </body>
   </html>

----


Model URLs Funktion am Model
-----------------------------

``core/models.py``

.. code-block:: python

   def get_absolute_url(self):
       from django.core.urlresolvers import reverse
       return reverse('core.views.project', args=[str(self.id)])

.. note::
   Um Objekte zu referenzieren, ist es sehr hilfreich, die Objekte um Funktionen zu erweitern wie ``get_absolute_url``.  


----

Verlinkung im Template
----------------------


.. code-block:: html

   <a href="{{ project.get_absolute_url }}">{{ project.name }}</a>

----


Asset Management
----------------

Wir bauen einen einfachen Bildupload 

----

Asset Management 1
------------------

Neues Attribut hinzufügen

``core/models.py``

.. code-block:: python

    image = models.ImageField(upload_to='project')
       
----

Asset Management 2
------------------

Settings Überprüfen

``portfolio/settings.py``

.. code-block:: python

   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   
   
Asset Management 3
------------------

Template Context Processor setzen für Media damit {{MEDIA_URL}} auch im Template zur Verfügung steht.

``portfolio/settings.py``

.. code-block:: python

   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   ...
                   'django.template.context_processors.media',
                   ...
               ],
           },
       },
   ]   
   
   
   

----
   
Asset Management 4
------------------

``portfolio/urls.py``

.. code-block:: python

   from django.conf.urls.static import static
   from django.conf import settings

   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
   
----   


Asset Management 5
------------------

Auf der Detailseite das Bild hinzufügen

``core/templates/project.html``

.. code-block:: html


    <img src="{{ MEDIA_URL }}{{ project.image }}">
       
       
   
----

Übung: Projekt-Kategorien
-------------------------

Kategorieliste mit Projekten darstellen