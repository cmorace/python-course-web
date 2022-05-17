****************
Lesson 13
****************

Review Homework
==================

Returning a list from a function
-----------------------------------

.. code-block:: python

    from random import randint

    def get_random_list(low, high, length):
        result = []
        for _ in range(length):
            result.append(randint(low, hight))
        return result

-------------------------------

For Each Loops
======================================

Last lesson we iterated over a list using an index variable.

.. code-block:: python

    some_list = [1, 4, 5, 7, 2, 56, 8]
    for i in range(len(some_list)):
        element = some_list[i]
        print(element)

A simpler way to do the same thing:

.. code-block:: python

    for element in some_list:
        print(element)

.. admonition:: Exercise:

    Rewrite the ``is_in_list(any_list, x)`` function from last week using a for each loop.

    Extension: rewrite functions from the last homework to use for each loops

-------------------------------

Particle Effects
==================

.. admonition:: Exercise:

    Create a ``Particle(Sprite)`` class.
    A particle should:

    - have a random starting direction
    - a random speed
    - deletes itself if touching edge

    Create 100 particles using a for loop

    Extensions:

    - bouncing off edge
    - fades out over time
    - find an image so particles look more like fire/explosion

.. admonition:: Exercise:

    Create a Button to change the color of all of the particles.
    Use a for each loop and ``window.get_all_sprites_with_tag('particle')``
    to get the list of particles

    Extensions:

    - Add multiple buttons to change the particles different colors.
      Can you use a single ``Button`` class?
    - Add a button to change the image and scale of the particles.


.. admonition:: Exercise:

    Create a Button to create new particles.

    Extensions:

    - Create a button to delete all particles
    - Create a button to delete particles in the order they were created.


.. admonition:: Exercise:

    Create an fireworks animation when the user clicks on the window or presses a key.
    The animation should have an explosion animation where particles shoot out radially
    from the point of explosion.
