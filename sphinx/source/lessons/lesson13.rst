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
            result.append(randint(a, b))
        return result

Foreach Loops
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


Particle Effects
==================

``class Particle(Sprite)``
----------------------------

- random direction
- random speed
- deletes if touching edge

Use a for loop to create many particles

Extensions:

- bouncing off edge
- fades out over time
- find an fire/explosion
