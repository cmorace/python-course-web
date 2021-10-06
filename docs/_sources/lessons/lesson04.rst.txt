Lesson 4
########


Download and extract the image files below.
   
:download:`lesson_04_images.zip <../_lesson_resources/lesson_04_images.zip>`


Rotation
********

In pycat, each sprite had a rotation property. Rotation is counter-clockwise positive, and by default, has a value of zero, which faces right.

- ``self.rotation = 0`` faces right
- ``self.rotation = 90`` faces up
- ``self.rotation = 180`` faces left
- ``self.rotation = 270`` faces down

Use the sprite's ``move_forward()`` method to move in the direction of its rotation. Sprites also have a special property ``rotation_mode`` which decouples the sprite's image and its ``rotation`` properties. The ``rotation_mode`` property is set like so,

.. code-block:: python

    from pycat.core import RotationMode
    ...
    sprite.rotation_mode = Rotation_Mode.RIGHT_LEFT

The ``Rotation_Mode.RIGHT_LEFT`` setting allows the sprite to move in any direction, but the sprite's image will be constrained to face either right or left. The possible values for ``sprite.rotation_mode`` are

- RotationMode.ALL_AROUND
- RotationMode.RIGHT_LEFT
- RotationMode.MIRROR
- RotationMode.NO_ROTATION

Collision Detection
********************

Collision detection determines if two or more sprites are touching one another. The ``Sprite`` class has many methods for determining collisions with other sprites. We usually use these methods inside the ``on_update`` method to check for collisions repeatedly. Some useful collision detection methods are:

- ``self.is_touching_any_sprite()`` returns true if this sprite is touching any other visible sprite in the window.
- ``self.is_touching_sprite(other_sprite: Sprite)`` returns true if this sprite touches the other sprite passed as an argument.
- ``self.is_touching_sprite_with_tag(tag: str)`` returns true if this sprite touches a sprite with a given tag using the ``sprite.add_tag(tag: str)`` method.


Keyword arguments
*****************
Keyword arguments, or kwargs, are arguments passed with a specific name. For example, we previously used a keyword argument in ``window = Window(background_image='img.png')`` to set the window's background image.  For convenience purposes, the window's method ``create_sprite()`` also accepts keyword arguments to set many of a sprite's properties. For example,

.. code-block:: python

    sprite = window.create_sprite()
    sprite.x = 100
    sprite.y = 200
    sprite.image = 'img.png'

is equavilent to 

.. code-block:: python

    sprite = window.create_sprite(x=100, y=200, image='img.png')

Note that the sprite properties are set after the sprite's ``on_create()`` method is called.



More Sprite Properties
***********************

Here is a list of more sprite properties,

- ``sprite.x``
- ``sprite.y``
- ``sprite.scale``
- ``sprite.rotation``
- ``sprite.color``
- ``sprite.opacity``
- ``sprite.rotation_mode``
- ``sprite.position``

