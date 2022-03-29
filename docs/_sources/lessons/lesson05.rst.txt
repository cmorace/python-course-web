Lesson 5
########

Download and extract the image files below.
   
:download:`img.zip <../_lesson_resources/lesson_05/img.zip>`


Decomposition
=============

1. What are the components of the "Gem Catching" game?
2. How does the player interact with the game?
3. Can we make this game with our existing knowledge?
4. What is missing?
5. What could we add to make the game more interesting?


Functions
=========

A function defines a procedure that we "call" to execute at a different
location in our program. In Python, functions start with the ``def`` keyword
to signify the definition of a new function, followed by the function name,
the function arguments, and the code that we want the function to execute.

For example:

.. code-block:: python
    
    def create_gem():
        window.create_sprite(Gem)


The ``Scheduler`` Class
=======================
Pycat includes a ``Scheduler`` class to call a function repeatedly at a fixed time interval. For example, if we want to execute our ``create_gem`` function every second, we can write:

.. code-block:: python

    from pycat.core import Scheduler

    Scheduler.update(create_gem, 1)


The ``Sprite``'s ``delete()`` method
=====================================

To delete a sprite from the window, use the ``delete()`` method.

.. code-block:: python

    if self.is_touching_sprite(cat):
        self.delete()
        

Randomization
=============

You can use the ``random`` module to generate random numbers.

.. code-block:: python

    from random import randint
    randint(1, 5)


The Sprite class also has a method to set a sprite's position to a random x-y location in the window. 

.. code-block:: python

    def on_create(self):
        self.goto_random_position()
