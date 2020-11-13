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

     pip install git+https://bitbucket.org/dwhite0/pycat.git -U

Lesson 9
^^^^^^^^
First update pycat in your Anaconda Terminal.

Download and unzip the following files.

:download:`lesson_09_media.zip <_lesson_resources/lesson_09_media.zip>`

1. Sound Effects and Audio Loops

   Pycat has two classes for playing sound files, ``Player`` and ``AudioLoop``.

   .. code:: python

      from pycat.core import Player, AudioLoop

      select_sprite_sound = Player('hit.wav')
      match_sprite_sound = Player('point.wav')
      audio_loop = AudioLoop('LoopLivi.wav', volume=0.2)
      audio_loop.play()

   `Scratch <https://scratch.mit.edu/projects/editor>`_ has a great collections of sound effects which you can download.


2. List Operations and Methods

   * The ``*`` operation

   .. code:: python

      img_list = 4 * ['1.png', '2.png', '3.png', '4.png']

   
   * The ``pop()`` method

   .. code:: python

      last_image = img_list.pop()

3. Random Shuffle

   .. code:: python

         import random

         img_list = 4 * ['1.png', '2.png', '3.png', '4.png']
         random.shuffle(img_list)
   


Lesson 8
^^^^^^^^

.. :download:`lesson_08_media.zip <_lesson_resources/lesson_08_media.zip>`

1. Review lists

   * list construction

   * ``append()``

   * ``len()``

   * accessing elements

   * ``clear()``

2. Pycat

   Keyword arguments for ``Window()`` and ``create_sprite()``

   .. code:: python

      window = Window(background_image="forest_04.png", draw_sprite_rects=True)


   .. code:: python

      window.create_sprite(Card, x=100, y=100, image='avatar_01.png')
      window.create_sprite(Card, x=100, y=200, image='avatar_01.png')
      window.create_sprite(Card, x=200, y=100, image='avatar_02.png')
      window.create_sprite(Card, x=200, y=200, image='avatar_02.png')


3. Python

   Use ``in`` and ``not in`` to check list membership.

   .. code:: python

      my_list = [1, 2, 3]
      x = 1
      if x in my_list:
         print(x, "is in", my_list)

      if x not in my list:
         print(x, "is not in", my_list)


Lesson 7
^^^^^^^^^
1. `Jupyter` review:

   * `Jupyter Notebook`, `VSCode`, and `Binder`

   * `Markdown`

   * Caution with code execution order

   * Restarting the kernel


2. Python list construction:

   * Empty list construction:

   .. code:: python

      my_list = []

   * Explicit construction:

   .. code:: python

      my_strings = ["red", "green", "blue"]
      my_ints = [23, 42, 57]
      my_floats = [1.41421, 2.71828, 3.14159]
      my_bools = [True, True, False]

3. The ``append()`` method:

   Adds elements to the end of the list.

   .. code:: python

      my_list = []
      my_list.append("red")
      my_list.append("blue")
      my_list.append("green")


4. Accessing list elements by index:

   Python, like most programming languages, uses `zero-based` indexing.

   .. code:: python

      my_list = ["red", "green", "blue"]
      first_color = my_list[0]

   We can use an index to `iterate` over a list.

   .. code:: python

      my_list = ["red", "green", "blue"]
      for i in range(3):
         print(my_list[i])


5. The ``len()`` function:

   Returns the number of objects in the list.

   .. code:: python

      my_list = ["red", "green", "blue"]
      size = len(my_list)

   The ``len()`` function allows us to iterate over lists with arbitrary length.

   .. code:: python
   
      my_list = ["red", "green", "blue", "cyan", "magenta", "yellow"]
         for i in range(len(my_list)):
            print(my_list[i])

6. The ``clear()`` function:

   Removes all elements in the list.

   .. code:: python

      my_list.clear()

7. Review homework





Lesson 6
^^^^^^^^^
:download:`lesson_06_media.zip <_lesson_resources/lesson_06_media.zip>`

1. Use `Sprite`'s ``on_left_click``:

.. code:: python

   class Alien(Sprite):
      def on_left_click(self):
         self.is_moving_up = True

2. Use `tags` for collision:

.. code:: python

   class Spaceship(Sprite):
      def on_create(self):
         self.add_tag('spaceship')

   class Alien(Sprite):
      def on_update(self, dt):
         if self.touching_any_sprite_with_tag('spaceship'):
            self.delete()

2. Display a `label` to show score:

.. code:: python

   score_label = Label('Aliens in ship: 0',x=550,y=600)
   window.add_label(score_label)
   score_label.text = 'Aliens in ship: '+str(space_ship.score)


Lesson 5
^^^^^^^^^

:download:`lesson_05_images.zip <_lesson_resources/lesson_05_images.zip>`

1. Use the `Scheduler`'s update function to repeatedly create sprites:

.. code:: python

   from pycat.core import Scheduler

   def create_gem(dt):
      window.create_sprite(Gem)

   Scheduler.update(create_gem, 1)

2. Sprite self deletion:

.. code:: python

   class Gem(Sprite):
      def on_update(self):
         if touching_any_sprite():
            self.delete()

3. Add custom class properties:

.. code:: python

   class Player(Sprite):
      def on_create(self):
         self.score = 0

4. Python lists and ``random.choice``:

.. code:: python

   import random
   file_list = ["img/1.png", "img/2.png", "img/3.png"]
   random.choice(file_list)


.. toctree::
   :hidden:

   setup
   homework
   notes
   tutorials
   binder

