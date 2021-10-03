Lesson 3
########

Jupyter Notebooks 
******************

Run the ``jupyter notebook`` command to get started. See the tutorial for a list of shortcuts `here <../_notebooks/tutorials/jupyter_tutorial.rst>`_.


The Update Design Pattern
**************************

Each sprite created has an update function called repeatedly from the time created until the time deleted or if the application is closed.

The Sprite Life-Cyle
=====================

1. ``sprite = window.create_sprite()``
    The window creates a new sprite object and calls the sprites ``on_create()`` method. Then it returns the .sprite object.
2. The ``on_update(self, dt)`` method is called repeatedly at about 60 frames per second. If you subclass the sprite, you can define a custom ``on_update(self, dt)`` method to add new behavior (e.g., movement, collision detection, image and color changed, etc.) to your sprite. The ``dt`` argument can tell us the precise time since the last ``on_update()`` was called.


Keyboard Interaction
*********************

The ``KeyCode`` class
=====================

Each key that can be pressed on a keyboard is defined by a constant value defined by the ``KeyCode`` class.

Checking For Key Events
=======================

In a sprite's ``on_update`` method we can detect three possible types of key events. We use ``KeyCode`` constant values to check for specific keys.

1. ``window.is_key_down(KeyCode.A)``
2. ``window.is_key_press(KeyCode.B)``
3. ``window.is_key_up(KeyCode.C)``

What is the difference? 
When would we want to use one vs. the other?

These three methods all return boolean values and are used together with an `if` statement to detect the correct key event. For example, the code below will continuously move a sprite to the left while a user holds down the ``A`` key.

.. code-block:: python
    
    def on_update(self, dt):
        if window.is_key_press(KeyCode.A):
            self.x -= 5

