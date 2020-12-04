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


Lesson 12
^^^^^^^^^

1. A new way to iterate over lists

   :download:`lesson_12.ipynb <_lesson_resources/lesson_12.ipynb>`

2. Particle Systems
   
   Starter Code:

   .. code:: python

      from pycat.core import Sprite, Window
      import random


      class Particle(Sprite):

          def on_create(self):
              self.goto_random_position()
              self.rotation = random.randint(0, 360)
              self.scale = 5


      window = Window()
      for _ in range(100):
          window.create_sprite(Particle)

      window.run()

   Your job is to add a bounce effect.

3. Changing particle properties

   Use tags to get a list of particles from the window

   .. code:: python

      class Particle(Sprite):

          def on_create(self):
              self.add_tag('particle')


      class ColorButton(Sprite):

          def on_left_click(self):
              for particle in window.get_sprites_with_tag('particle'):
                  particle.color = self.color

   Now create two of more buttons with different colors to modify the particles' color.

4. Timed Explosions

   Keep track of time to set off an explosion.

   .. code:: python

      class TimedExplosionParticle(Sprite):
          def on_create(self):
              self.timer = 0

          def on_update(self, dt):
              self.timer += dt

   Create two buttons for creating and exploding particles.

5. Fireworks

   Create particles when clicking the mouse.

   .. code:: python

      from pycat.base.event import MouseEvent

      def my_mouse_press(mouse: MouseEvent):
          for _ in range(8):
              p = window.create_sprite(Particle)
              p.position = mouse.position
              p.rotation = random.randint(70, 110)
              p.speed = 5+random.random()*2


      window.run(on_mouse_press=my_mouse_press)

   Add a timer to your your particle class and set off the fireworks.


Lesson 11
^^^^^^^^^

Learning objectives:

- List indexing (reinforce)
- Parallel lists
- Refactoring code to avoid duplication
- ``global`` keyword


:download:`lesson_11_media.zip <_lesson_resources/lesson_11_media.zip>`


1. Slideshow

   .. code:: python

      images = [
         'squirrel.jpg',
         'bird.jpg',
         'sheep.jpg',
         'cow.jpg',
         'seal.jpg',
         'cat.jpg',
         'hedgehog.jpg',
         'meerkat.jpg',
      ]

      image_number = 0
      window = Window(width=1000)
      window.background_image = images[image_number]


      class NextButton(Sprite):

         def on_left_click(self):
            global image_number

2. Slideshow with Labels

   .. code:: python

      texts = [
         'Red squirrel',
         'Pheasant',
         'Sheep',
         'Cow',
         'Seal',
         'Cat',
         'Hedgehog',
         'Meerkat',
      ]

      text_label = Label('', 100, 50)
      text_label.text = texts[image_number]
      window.add_label(text_label)

3. Refactoring Duplicate Code

4. Track and Print Out Liked/Disliked Pictures


Create Your Programming Website
""""""""""""""""""""""""""""""""

Sign up for a github account at `Github <https://github.com/>`_. Choose your username wisely. Your website will be named ``www.<your_username>.github.io``

Follow the instructions `here <https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/creating-a-github-pages-site?>`_ to set up your website.

1. Name your repository ``<your_username>.github.io``
2. Add a file ``index.md``
3. Go to settings and enable github pages for your main branch

Lesson 10
^^^^^^^^^

:download:`lesson_10.ipynb <_lesson_resources/lesson_10.ipynb>`



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
      no_match_sprite_sound = Player('laugh.wav')
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

