Lesson 8
***************************

Stopwatch Decomposition
=========================

1. A label to show the running time
2. A start button to start/pause the running time
3. A reset button that sets the running time to 0

.. admonition:: Exercise

   1. Implement a basic stopwatch GUI. You do not have to change the time label. Only show the components on the screen.
   2. Use print statements to check button clicks with the ``on_left_click`` method.

---------------------------

Extending the ``Label`` Class
==================================

We can *extend* the ``Label`` class,
similar to how we *extend* the ``Sprite`` class.

.. code-block:: python

    from pycat.core import Label

    class AwesomeLabel(Label):
        def on_create(self):
            pass

        def on_update(self, dt):
            pass


The ``on_update``'s ``dt`` Parameter
======================================

The ``on_update`` method is called **approximately** 60 times per second.
If we need to know the precise time since the previous ``on_update``, we
can check it using the ``dt`` parameter.

.. code-block:: python

    def on_update(self, dt):
        print('time since previous on_update:', dt)

.. admonition:: Exercise 

   1. Write a custom class extending ``Label``.
   2. Create an instance of your class with ``window.create_label(YourLabelClassName)``
   3. add a *property* to your Label class to store the running time.
   4. update the running time with the ``dt`` property
   5. update ``self.text`` to show the current running time.

   Note: When you finish, your stopwatch time will increase automatically.
   You do not need to implement start/pause/reset yet.

------------------------------

Controlling the Stopwatch State
=================================

The stopwatch can be in one of two *states*.
The behavior of the stopwatch is different
depending on the current state.
Either it is running (the time is increasing),
or it is not running (the time is not increasing).

- How/Where should we store the current state of our stopwatch?
- What *event* changes the stopwatch's state?
- Where do we define the different behaviors?

.. admonition:: Exercise

    Add pause/start, and reset functionality to your stopwatch program. Can you find a python function to show fewer digits of the running time?

-------------------------------

Extensions
=================

After you finish the stopwatch,
think of an original idea with time as a central theme and create it!

Some suggestions are:

- Visualize the running time graphically.
- Add sound effects
- Implement a count-down timer. Use ``input`` to get the total time.



