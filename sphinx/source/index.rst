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

2. Sprite Self Deletion:

.. code:: python

   class Gem(Sprite):
      def on_update(self):
         if touching_any_sprite():
            self.delete()

3. Add Custom Class Properties:

.. code:: python

   class Player(Sprite):
      def on_create(self):
         self.score = 0

4. Python Lists and ``random.choice``:

.. code:: python

   import random
   file_list = ["img/1.png", "img/2.png", "img/3.png"]
   random.choice(file_list)


Lesson 6
^^^^^^^^^
:download:`lesson_06_media.zip <_lesson_resources/lesson_06_media.zip>`

1. Use `Sprite`'s ``on_left_click``:

.. code:: python

   class Alien(Sprite):
      def on_left_click(self):
         self.is_moving_up = True

2. Use `tags`'s for collision:




.. toctree::
   :hidden:

   setup
   homework
   notes
   tutorials
   binder

