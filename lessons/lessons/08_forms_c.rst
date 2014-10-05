
Form: Checkliste
--------------------------

* forms.py erstellen
* ModelForm für Model erstellen
* Update-View erstellen (display, save, errors)
* urls.py updaten
* Template erstellen


----

forms.py und ModelsForm
------------------------

``core/forms.py``

.. code-block:: python

   from django import forms
   from cpre.models import Contact
   
   class ContactForm(forms.ModelForm):
       class Meta:
           model = Contact
           fields = ['name']


.. note::
   Man KANN jedes Feld einzeln definieren. Das machen wir aber nicht. 


----

Form: die View Dazu
---------------------

``core/views.py``

.. code-block:: python

  from core.forms import ContactForm
  def add_contact(request):
      context = RequestContext(request)
      if request.method == 'POST':
          form = ContactForm(request.POST)
          if form.is_valid():
              form.save(commit=True)
              return index(request)
          else:
              print form.errors
      else:
          form = ContactForm()
      return render_to_response('core/add_contact.html', {'form': form}, context)


----


Form: URL-Mapping
------------------

``core/urls.py``

.. code-block:: python

   url(r'^contact/$', views.add_contact, name='add_contact'), 
   
----

Form: Das Template
------------------

.. code-block:: html

    <form id="cform" method="post" action="/core/contact/">
        {% csrf_token %}
        {% for hidden in form.hidden_fields %}
            {{ hidden }}
        {% endfor %}
        {% for field in form.visible_fields %}
            {{ field.errors }}
            {{ field.help_text }}
            {{ field }}
        {% endfor %}
        <input type="submit" name="submit" value="Contact Me!" />
    </form>

.. note::
   CSRF: https://docs.djangoproject.com/en/1.6/ref/contrib/csrf/

----





:class: slidecenter

Form: Demo!
-----------


