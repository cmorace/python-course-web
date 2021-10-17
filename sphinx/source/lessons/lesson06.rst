Lesson 6
########

Download and extract the image files below.
   
:download:`media.zip <../_lesson_resources/lesson_06/L6_media.zip>`


State
======
We can add different behaviors to our sprite's by defining different states. For example, a sprite can perform one type of behavior if it is in one state and another behavior if it is in a different state. Add a custom property to the sprite to store its current state. If only two behaviors are required, a boolean will suffice. For example,

.. code-block:: python

    self.is_in_original_state = True


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

    label = w.create_label():
    label.x = 100
    label.y = 300
    label.text = 'Hello, World!'


will create a new label, set the x and y position, and display 'Hello, World!' in the window.

You can also create a custom Label class very similar to the way you would a custom Sprite class.

.. code-block:: python

    class Hello(Label):
        def on_create(self):
            self.text = 'Hello'

        def on_update(self):
            pass

    window.create_label(Hello)

