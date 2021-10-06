Lesson 5
########

Download and extract the image files below.
   
:download:`img.zip <../_lesson_resources/lesson_05/img.zip>`


Decomposition
=============

1. What are the components of the `Gem Catching` game?
2. How does the player interact with the game?
3. Can we make this game with our existing knowledge?
4. What is missing?
5. What could we add to make the game more interesting?


Functions
=========

.. code_block:: python
    
    def create_gem(dt):
        window.create_sprite(Gem)


The ``Scheduler`` Class
=======================

.. code_block:: python

    from pycat.core import Scheduler

    Scheduler.update(create_gem, 1)


The ``Sprite``'s ``delete()`` method
=====================================

.. code_block:: python

    if self.is_touching_sprite(cat):
        self.delete()
        

Randomization
=============

.. code-block:: python

    from random import randint
    randint(1, 5)
