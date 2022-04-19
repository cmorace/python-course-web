Lesson 9
=================

Individual Project and Presentation
--------------------------------------

Over the next two weeks, you will design and implement an individual project.
You will demo and present your project at the end of next week's class.

.. admonition:: Requirement

    You must have at least one sprite with an *animation cycle*.

    .. image:: images/animation_cycle.gif
        :align: center
        :width: 30 %

An animation cycle repeats different behaviors (i.e. animations).
There are many ways we could implement this. It will be up to you
to choose an appropriate method for your project.

-------------



The ``Sprite``'s ``on_update`` Method
-------------------------------------------

The ``Sprite`` class has an ``on_update`` method,
which takes the *arguments* ``self`` and ``dt``.

.. code-block:: python

    class MyAwesomeSprite(Sprite):
        def on_update(self, dt):
            # does some awesome stuff

.. admonition:: Questions

    #. What is the ``type`` of the argument ``dt``?
    #. What is the approximate value?
    #. What does the value of ``dt`` represent?
    #. What are some use-cases for ``dt``?
    #. How does a ``Sprite``'s ``on_update`` method get called?


--------------------------------


``Scheduler`` Methods
-------------------------------------------

The ``Scheduler.update()`` Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Scheduler.update(func: Callable, interval: float)`` is a *static* method that
repeatedly calls a function at fixed time intervals.

1. A ``Callable`` object i.e. a *method*, *function*, or *constructor*
2. A ``float`` equal to the time interval between each function called

For example,

.. code-block:: python

    from pycat.core import Scheduler

    def create_gem():
        window.create_sprite(Gem)

    Scheduler.update(create_gem, 2)


.. admonition:: Questions

    #. What does the code above do?
    #. How often will the ``create_gem()`` function be called?
    #. Is the time between each call exact?
    #. How long does it take for the first ``Gem`` to be created?
    #. What if we wanted to create new ``Gems`` at random time intervals?

We can also pass methods to ``Scheduler.update()``.
For example,

.. code-block:: python

    class Ape(Sprite):

        def on_create(self):
            Scheduler.update(self.throw, 2)

        def throw():
            print('throw called')

    window.create_sprite(Ape)

or,

.. code-block:: python

    class Ape(Sprite):
        def throw():
            print('throw called')

    ape = window.create_sprite(Ape)
    Scheduler.update(ape.throw, 2)

.. admonition:: Questions

    #. Is there a difference in behavior in the last two examples?
    #. What is the difference?


The ``Scheduler.cancel_update()`` Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Scheduler.cancel_update(func: Callable)`` is a *static* method that
stops updating a function.

.. code-block:: python

    class Button(Sprite):
        def on_create(self):
            Scheduler.update(self.my_update, 2)

        def my_update(self):
            print('my_update()')

        def on_left_click(self):
            Scheduler.cancel_update(self.my_update)


The ``Scheduler.wait()`` Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Scheduler.wait(delay: float, func: Callable)`` is a *static* method
that calls a function a single time after some delay time. For example,
``Scheduler.wait(5, create_gem)`` calls the ``create_gem`` function after 5 seconds.

.. admonition:: Question

    Could we use ``Scheduler.wait()`` to replicate
    the behavior of ``Scheduler.update()``


Scheduling functions with a ``dt`` argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def my_update_func(dt):
        print("I was last updated", dt, "seconds ago")

    def my_wait_func(dt):
        print("I waited", dt, "seconds")

    Scheduler.update(my_update_func, 2)
    Scheduler.wait(4, my_wait_func)

----------

Animation Cycles
----------------------


.. image:: images/animation_cycle.gif
        :align: center
        :width: 30 %


:download:`lesson_09_images.zip <../_lesson_resources/lesson_09_images.zip>`

#. Implement the animation above using the ``Scheduler``.
#. Implement it using the ``Sprite``'s '``on_update`` method.
#. Let's discuss the advantages and disadvantages of the two approaches.
#. Start planning your project!
