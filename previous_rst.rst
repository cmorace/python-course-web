.. Most of the homework will be distributed as Jupyter notebooks which you can download below. You can preview the homework by clicking on the links under `Preview`_.

.. Downloads
.. ----------

.. To complete the assignments you should have Anaconda installed. If you have not installed Anaconda yet, see the `Anaconda installation instructions <setup.rst>`_. 

.. You can complete the assignments by downloading the `.ipynb` file and opening the file with VS Code or the Jupyter Notebook web application. The `Jupyter tutorial <_notebooks/tutorials/jupyter_tutorial.ipynb>`_ has information about using jupyter notebooks if you are unfamiliar.

..
   .. note::

..    You must be using a desktop computer to download the homework files.


.. .. |hw1_binder| image:: images/launch_binder.svg
..    :target: https://mybinder.org/v2/gh/cmorace/python-course-web/gh-pages?filepath=sphinx%2Fsource%2F_notebooks%2Fhomework%2Fhw01.ipynb


.. .. |hw2_binder| image:: images/launch_binder.svg
..    :target: https://mybinder.org/v2/gh/cmorace/python-course-web/gh-pages?filepath=sphinx%2Fsource%2F_notebooks%2Fhomework%2Fhw02.ipynb

.. .. |hw3_binder| image:: images/launch_binder.svg
..    :target: https://mybinder.org/v2/gh/cmorace/python-course-web/gh-pages?filepath=sphinx%2Fsource%2F_notebooks%2Fhomework%2Fhw03.ipynb

.. .. |hw4_binder| image:: images/launch_binder.svg
..    :target: https://mybinder.org/v2/gh/cmorace/python-course-web/gh-pages?filepath=sphinx%2Fsource%2F_notebooks%2Fhomework%2Fhw04.ipynb

.. .. |hw5_binder| image:: images/launch_binder.svg
..    :target: https://mybinder.org/v2/gh/cmorace/python-course-web/gh-pages?filepath=sphinx%2Fsource%2F_notebooks%2Fhomework%2Fhw05.ipynb

..
   .. list-table::
      
..    :header-rows: 3

..    * - Homework
..      - Binder
..      - Solution
..    * - :download:`hw01.ipynb <_notebooks/homework/hw01.ipynb>`
..      - |hw1_binder|
..      - :download:`hw01_solution.ipynb <_notebooks/homework/hw01_solution.ipynb>`
..    * - :download:`hw02.ipynb <_notebooks/homework/hw02.ipynb>`
..      - |hw2_binder|
..      - :download:`hw02_solution.ipynb <_notebooks/homework/hw02_solution.ipynb>`
..    * - :download:`hw03.ipynb <_notebooks/homework/hw03.ipynb>`
..      - |hw3_binder|
..      - :download:`hw03_solution.ipynb <_notebooks/homework/hw03_solution.ipynb>`
..    * - :download:`hw04.ipynb <_notebooks/homework/hw04.ipynb>`
..      - |hw4_binder|
..      - :download:`hw04_solution.ipynb <_notebooks/homework/hw04_solution.ipynb>`
..    * - :download:`hw05.ipynb <_notebooks/homework/hw05.ipynb>`
..      - |hw5_binder|
..      - 

.. Preview
.. -------------

.. The links below will bring you to a preview of the homework assignments. You will not be able to execute the Python code; these are static web pages meant for previewing assignments and solutions.

.. 
 .. toctree::
   :hidden:
..    :maxdepth: 1

..    _notebooks/homework/hw01
..    _notebooks/homework/hw01_solution
..    _notebooks/homework/hw02
..    _notebooks/homework/hw02_solution
..    _notebooks/homework/hw03
..    _notebooks/homework/hw03_solution
..    _notebooks/homework/hw04
..    _notebooks/homework/hw04_solution
..    _notebooks/homework/hw05

...............................................



.. Lesson 14
.. ^^^^^^^^^
.. Lesson Objectives:

.. - Webpage setup
.. - Final project planning, decomposition, and implementation

.. 1. Webpage setup

.. - Download the zip file :download:`markdown-pages <_lesson_resources/markdown-pages.zip>`
.. - Create a new folder in your VS Code workspace
.. - Move the downloaded files into the new folder
.. - Open ``index.md`` in the VS Code editor
.. - Press ``shift + control + v`` to see a preview
.. - Add the files to your github repository

.. 2. Write a rough overview for your final project (see template webpage) 
   
.. 3. Draw a decomposition/ UML class diagram (see template webpage)

..    - Take a picture of the diagram and add it to your webpage

.. 4. Draw/find some appropriate sprites and sound effects

..    - `Scratch <https://scratch.mit.edu/projects/editor>`_ has a good collection.

..    - Add images of each sprite to your webpage and give a brief description of its role in the project

.. 5. Preview your webpage in VS Code and update your repository

.. 6. Begin implementation




.. Lesson 13
.. ^^^^^^^^^

.. First, please update pycat with Anaconda prompt.

.. What's new?
..    - new mouse event handler for the Sprite class: ``on_left_click_anywhere(self)``
..    - ``self.point_toward_mouse_cursor()`` will set a sprite's rotation/direction
..    - a ``Color`` class with named colors, e.g. ``Color.AMBER``.

.. Final project template and decomposition

.. 1. Implementing the Player class

..    .. code:: python

..     from pycat.core import Color, KeyCode, Sprite, Window

..     window = Window()


..     class Player(Sprite):

..         def on_create(self):
..             self.color = Color.AMBER
..             self.scale = 30
..             self.speed = 10

..         def on_update(self, dt):
..             if window.get_key(KeyCode.W):
..                 self.y += self.speed
..             # fill in code for keys A, S, D


..     player = window.create_sprite(Player)
..     window.run()

..    Extensions:

..    - set your player's initial position
..    - add a key to make your player teleport
..    - add a method to reset your player's position
..    - add properties to store your player's hp, strength, defense, magic, etc.


.. 2. Shooting Bullets with ``on_left_click_anywhere()``
   
..    We will fire bullets whenever the mouse is clicked.
..    Add the following method to your Player class.
   
..    .. code:: python

..       def on_left_click_anywhere(self):            
..           window.create_sprite(Bullet)

..    Now implement your ``Bullet`` class.

..    - What is the bullet size i.e. ``self.scale``?
..    - What is the bullet color i.e. ``self.color``?
..    - What is the bullet starting position i.e ``self.position``?
..    - Add a new property for bullet speed i.e. ``self.speed``
..    - To set the rotation to shoot towards the mouse cursor, use ``self.point_toward_mouse_cursor()``.
..    - Make each bullet move foward to the mouse cursor with ``self.move_forward(self.speed)`` and call ``self.delete()`` if ``self.touching_window_edge()``

..    Extensions:

..    - Give your player a maximum number of bullets they can fire
..    - Add a power property to your ``Bullet`` class
..    - Add a ``PowerUp`` class that the player can collect to increase power

.. 3. Add an ``Enemy`` class and generate some enemies.

..    We will need a little help. Import the ``Scheduler`` class and the ``random`` module.

..    .. code:: python
      
..       from pycat.core import Color, KeyCode, Scheduler, Sprite, Window
..       import random

..    In the ``Enemy`` class:
   
..    - Start each enemy at a random starting position i.e. ``self.goto_random_position()``
..    - Start each enemy with a random rotation, i.e. ``self.rotation = random.randint(0, 360)``
..    - Add a speed property and move each enemy forward
..    - Delete an enemy when they touch the window's edge

..    Spawn the enemies using the ``Scheduler.update()`` method.

..    .. code:: python

..       def spawn_enemy():
..           window.create_sprite(Enemy)


..       Scheduler.update(spawn_enemy, delay=1)

..    Remember that this code must be outside any class (in the global scope).


..    Extension:

..    - only spawn enemies if they are farther than some distance from the player. You can use the method ``self.distance_to(player.position)``
..    - only spawn enemies on the window edge. How can you keep them from being immediately deleted?

.. 4. Have the player's bullets kill enemies

..    - ``self.add_tag('bullet')`` in our ``Bullet`` class
..    - ``self.delete()`` if ``self.touching_any_sprite_with_tag('bullet')`` in our ``Enemy`` class.

..    Extensions: 
   
..    - add hp to your ``Enemy`` class so that they die after multiple hits
..    - if an enemny touches the player, reduce the player's hp, change color, and/or opacity, etc.
..    - keep track of the total number of enemies killed
..    - add a label that displays the total number of enemies killed

.. 5. Make your enemies shoot bullets at the player

..    Create an ``EnemyBullet`` class with properties:

..    - ``self.color``
..    - ``self.scale``
..    - ``self.speed``

..    The enemy bullets should ``self.move_forward(self.speed)`` and be deleted if:
    
..    - ``self.touching_window_edge()`` or,
..    - ``self.touching_sprite(player)``

..    We want each of our enemies to fire bullets at the player every 2 seconds.
    
..    - add a ``self.time`` to the ``Enemy`` class
..    - update ``self.time += dt`` in ``on_update(self, dt)``
..    - if ``self.time > 2`` then create a bullet and remember to set ``self.time = 0``
   
..    Each bullet's position should start at the enemy shooting it and ``point_toward_sprite(player)``.

..    Extensions:

..    - delete the enemy bullets when they touch the player
..    - reduce the player's hp if they get hit by a enemy bullet
..    - add a label to display the player's hp


.. Lesson 12
.. ^^^^^^^^^

.. 1. A new way to iterate over lists

..    :download:`lesson_12.ipynb <_lesson_resources/lesson_12.ipynb>`

.. 2. Particle Systems
   
..    Starter Code:

..    .. code:: python

..       from pycat.core import Sprite, Window
..       import random


..       class Particle(Sprite):

..           def on_create(self):
..               self.goto_random_position()
..               self.rotation = random.randint(0, 360)
..               self.scale = 5


..       window = Window()
..       for _ in range(100):
..           window.create_sprite(Particle)

..       window.run()

..    Your job is to add a bounce effect.

.. 3. Changing particle properties

..    Use tags to get a list of particles from the window

..    .. code:: python

..       class Particle(Sprite):

..           def on_create(self):
..               self.add_tag('particle')


..       class ColorButton(Sprite):

..           def on_left_click(self):
..               for particle in window.get_sprites_with_tag('particle'):
..                   particle.color = self.color

..    Now create two of more buttons with different colors to modify the particles' color.

.. 4. Timed Explosions

..    Keep track of time to set off an explosion.

..    .. code:: python

..       class TimedExplosionParticle(Sprite):
..           def on_create(self):
..               self.timer = 0

..           def on_update(self, dt):
..               self.timer += dt

..    Create two buttons for creating and exploding particles.

.. 5. Fireworks

..    Create particles when clicking the mouse.

..    .. code:: python

..       from pycat.base.event import MouseEvent

..       def my_mouse_press(mouse: MouseEvent):
..           for _ in range(8):
..               p = window.create_sprite(Particle)
..               p.position = mouse.position
..               p.rotation = random.randint(70, 110)
..               p.speed = 5+random.random()*2


..       window.run(on_mouse_press=my_mouse_press)

..    Add a timer to your your particle class and set off the fireworks.


.. Lesson 11
.. ^^^^^^^^^

.. Learning objectives:

.. - List indexing (reinforce)
.. - Parallel lists
.. - Refactoring code to avoid duplication
.. - ``global`` keyword


.. :download:`lesson_11_media.zip <_lesson_resources/lesson_11_media.zip>`


.. 1. Slideshow

..    .. code:: python

..       images = [
..          'squirrel.jpg',
..          'bird.jpg',
..          'sheep.jpg',
..          'cow.jpg',
..          'seal.jpg',
..          'cat.jpg',
..          'hedgehog.jpg',
..          'meerkat.jpg',
..       ]

..       image_number = 0
..       window = Window(width=1000)
..       window.background_image = images[image_number]


..       class NextButton(Sprite):

..          def on_left_click(self):
..             global image_number

.. 2. Slideshow with Labels

..    .. code:: python

..       texts = [
..          'Red squirrel',
..          'Pheasant',
..          'Sheep',
..          'Cow',
..          'Seal',
..          'Cat',
..          'Hedgehog',
..          'Meerkat',
..       ]

..       text_label = Label('', 100, 50)
..       text_label.text = texts[image_number]
..       window.add_label(text_label)

.. 3. Refactoring Duplicate Code

.. 4. Track and Print Out Liked/Disliked Pictures


.. Create Your Programming Website
.. """"""""""""""""""""""""""""""""

.. Sign up for a github account at `Github <https://github.com/>`_. Choose your username wisely. Your website will be named ``www.<your_username>.github.io``

.. Follow the instructions `here <https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/creating-a-github-pages-site?>`_ to set up your website.

.. 1. Name your repository ``<your_username>.github.io``
.. 2. Add a file ``index.md``
.. 3. Go to settings and enable github pages for your main branch

.. Lesson 10
.. ^^^^^^^^^

.. :download:`lesson_10.ipynb <_lesson_resources/lesson_10.ipynb>`



.. Lesson 9
.. ^^^^^^^^
.. First update pycat in your Anaconda Terminal.

.. Download and unzip the following files.

.. :download:`lesson_09_media.zip <_lesson_resources/lesson_09_media.zip>`

.. 1. Sound Effects and Audio Loops

..    Pycat has two classes for playing sound files, ``Player`` and ``AudioLoop``.

..    .. code:: python

..       from pycat.core import Player, AudioLoop

..       select_sprite_sound = Player('hit.wav')
..       match_sprite_sound = Player('point.wav')
..       no_match_sprite_sound = Player('laugh.wav')
..       audio_loop = AudioLoop('LoopLivi.wav', volume=0.2)
..       audio_loop.play()

..    `Scratch <https://scratch.mit.edu/projects/editor>`_ has a great collections of sound effects which you can download.


.. 2. List Operations and Methods

..    * The ``*`` operation

..    .. code:: python

..       img_list = 4 * ['1.png', '2.png', '3.png', '4.png']

   
..    * The ``pop()`` method

..    .. code:: python

..       last_image = img_list.pop()

.. 3. Random Shuffle

..    .. code:: python

..          import random

..          img_list = 4 * ['1.png', '2.png', '3.png', '4.png']
..          random.shuffle(img_list)
   


.. Lesson 8
.. ^^^^^^^^

.. .. :download:`lesson_08_media.zip <_lesson_resources/lesson_08_media.zip>`

.. 1. Review lists

..    * list construction

..    * ``append()``

..    * ``len()``

..    * accessing elements

..    * ``clear()``

.. 2. Pycat

..    Keyword arguments for ``Window()`` and ``create_sprite()``

..    .. code:: python

..       window = Window(background_image="forest_04.png", draw_sprite_rects=True)


..    .. code:: python

..       window.create_sprite(Card, x=100, y=100, image='avatar_01.png')
..       window.create_sprite(Card, x=100, y=200, image='avatar_01.png')
..       window.create_sprite(Card, x=200, y=100, image='avatar_02.png')
..       window.create_sprite(Card, x=200, y=200, image='avatar_02.png')


.. 3. Python

..    Use ``in`` and ``not in`` to check list membership.

..    .. code:: python

..       my_list = [1, 2, 3]
..       x = 1
..       if x in my_list:
..          print(x, "is in", my_list)

..       if x not in my list:
..          print(x, "is not in", my_list)


.. Lesson 7
.. ^^^^^^^^^
.. 1. Jupyter review:

..    * Jupyter Notebook, VSCode, and Binder

..    * Markdown

..    * Caution with code execution order

..    * Restarting the kernel


.. 2. Python list construction:

..    * Empty list construction:

..    .. code:: python

..       my_list = []

..    * Explicit construction:

..    .. code:: python

..       my_strings = ["red", "green", "blue"]
..       my_ints = [23, 42, 57]
..       my_floats = [1.41421, 2.71828, 3.14159]
..       my_bools = [True, True, False]

.. 3. The ``append()`` method:

..    Adds elements to the end of the list.

..    .. code:: python

..       my_list = []
..       my_list.append("red")
..       my_list.append("blue")
..       my_list.append("green")


.. 4. Accessing list elements by index:

..    Python, like most programming languages, uses "zero-based" indexing.

..    .. code:: python

..       my_list = ["red", "green", "blue"]
..       first_color = my_list[0]

..    We can use an index to "iterate" over a list.

..    .. code:: python

..       my_list = ["red", "green", "blue"]
..       for i in range(3):
..          print(my_list[i])


.. 5. The ``len()`` function:

..    Returns the number of objects in the list.

..    .. code:: python

..       my_list = ["red", "green", "blue"]
..       size = len(my_list)

..    The ``len()`` function allows us to iterate over lists with arbitrary length.

..    .. code:: python
   
..       my_list = ["red", "green", "blue", "cyan", "magenta", "yellow"]
..          for i in range(len(my_list)):
..             print(my_list[i])

.. 6. The ``clear()`` function:

..    Removes all elements in the list.

..    .. code:: python

..       my_list.clear()

.. 7. Review homework





.. Lesson 6
.. ^^^^^^^^^
.. :download:`lesson_06_media.zip <_lesson_resources/lesson_06_media.zip>`

.. 1. Use ``Sprite``'s ``on_left_click``:

.. .. code:: python

..    class Alien(Sprite):
..       def on_left_click(self):
..          self.is_moving_up = True

.. 2. Use "tags" for collision:

.. .. code:: python

..    class Spaceship(Sprite):
..       def on_create(self):
..          self.add_tag('spaceship')

..    class Alien(Sprite):
..       def on_update(self, dt):
..          if self.touching_any_sprite_with_tag('spaceship'):
..             self.delete()

.. 2. Display a ``Label`` to show score:

.. .. code:: python

..    score_label = Label('Aliens in ship: 0',x=550,y=600)
..    window.add_label(score_label)
..    score_label.text = 'Aliens in ship: '+str(space_ship.score)


.. Lesson 5
.. ^^^^^^^^^

.. :download:`lesson_05_images.zip <_lesson_resources/lesson_05_images.zip>`

.. 1. Use the ``Scheduler``'s update function to repeatedly create sprites:

.. .. code:: python

..    from pycat.core import Scheduler

..    def create_gem(dt):
..       window.create_sprite(Gem)

..    Scheduler.update(create_gem, 1)

.. 2. Sprite self deletion:

.. .. code:: python

..    class Gem(Sprite):
..       def on_update(self):
..          if touching_any_sprite():
..             self.delete()

.. 3. Add custom class properties:

.. .. code:: python

..    class Player(Sprite):
..       def on_create(self):
..          self.score = 0

.. 4. Python lists and ``random.choice``:

.. .. code:: python

..    import random
..    file_list = ["img/1.png", "img/2.png", "img/3.png"]
..    random.choice(file_list)

.................................................



.. 1. Optional Software
.. --------------------

.. Pycat-tools
.. ^^^^^^^^^^^^^
.. Download pycat-tools `here <https://bitbucket.org/dwhite0/pycat/raw/master/utils/pycat-vscode-extension/pycat-tools/pycat-tools-0.0.1.vsix>`_. In VS Code's extensions view, click on the "Views and More Actions" button and then Install from VSIX...

.. .. image:: images/install_vsix.png
..    :scale: 80 %
..    :align: center
      
.. Select the ``pycat-tools.vsix`` file you just downloaded.
