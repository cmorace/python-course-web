Lesson 7
#########

Download and extract the image files below.
   
:download:`media.zip <../_lesson_resources/lesson_06/L6_media.zip>`


State
======
We can add behavior to our sprite's by defining different states. For example, a sprite can perform one type of behavior if it is in one state, and perform another behavior if it is in a different state. Add a custom property to the sprite to store its current state. If only two behaviors are required, a boolean will suffice. For example,

.. code-block:: python

    self.is_in_original_state = True

Then, in ``on_update`` use a conditional to define the different behaviors. For example,

.. code-block:: python

    def on_update(self, dt):
        if self.is_in_original_state:
            self.x += 1
        else:
            self.x -= 1


Mouse Click Event Handler
===========================

In Pycat, when a sprite is clicked with the left mouse button, the ``on_left_click()`` event handler is called.

.. code-block:: python
    
    def on_left_click(self):
        pass

Tagging Sprites
================

.. code-block:: python

    self.add_tag('alien')

.. code-block:: python

    if self.is_touching_any_sprite_with_tag('alien'):
        print("I touched an alien!")


Labels
========

Labels display strings on the screen. The Label API is very similar to the Sprite's API. For example,

.. code-block:: python

    label = w.create_label()
    label.x = 100
    label.y = 300
    label.text = 'Hello, World!'


will create a new label, set the x and y position, and display 'Hello, World!' in the window.

You can also create a custom Label class very similar to the way you would a custom Sprite class.

.. code-block:: python

    class Hello(Label):
        def on_create(self):
            self.text = 'Hello'

        def on_update(self, dt):
            pass

    window.create_label(Hello)

Sound Effects
===============

You can use the pycat ``Player`` class to play different sounds. First you must find a ``.wav`` sound file you would like to play in your game. `Scratch <www.scratch.mit.edu>`_ has many good sound effects that you can download.

.. code-block:: python

    sound = Player('die.wav')
    sound.play()