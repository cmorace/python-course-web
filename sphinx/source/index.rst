Welcome to the Python Course Website!
=================================================

Hi there. This page includes some resources for our Python course. Check it out!

* `Setup <setup.rst>`_ has instructions for setting up a Python programming environment.
* `Homework <homework.rst>`_ posts the assigned homework.
* `Notes <notes.rst>`_ include details about Python and the topics we cover in class.
* `Tutorials <tutorials.rst>`_ include tutorials for the programming tools we use.
* `Binder <binder.rst>`_ has links to an online Python programming environment.

Pycat
------

.. note::
   Update pycat by running the following command in your terminal application (e.g. Anaconda Prompt)

   .. code:: bash

     pip install git+https://bitbucket.org/dwhite0/pycat.git


Lesson 5
^^^^^^^^^

:download:`lesson_05_images.zip <_lesson_resources/lesson_05_images.zip>`

1. Use the `Scheduler`'s update function to repeatedly create sprites:

.. code:: python

   from pycat import Scheduler

   def create_gem(dt):
      window.create_sprite(Gem)

   Scheduler.update(create_gem, 1)

2. Add properties on the fly:

.. code:: python

   class Player(Sprite):
      def on_create(self):
         self.score = 0 


Lesson 6
^^^^^^^^^
:download:`lesson_06_media.zip <_lesson_resources/lesson_06_media.zip>`


.. toctree::
   :hidden:

   setup
   homework
   notes
   tutorials
   binder

