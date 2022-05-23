************************
Lesson 14
************************


Top-Down Shooter


The ``Player`` Class
==================================

.. code:: python

    from pycat.core import Color, Sprite, Window

    window = Window()


    class Player(Sprite):

        def on_create(self):
            self.color = Color.AMBER
            self.scale = 30
            self.speed = 10

        def on_update(self, dt):
            if window.is_key_pressed('w'):
                self.y += self.speed
            # fill in code for keys A, S, D


    player = window.create_sprite(Player)
    window.run()

Extensions:

- set your player's initial position
- add a key to make your player teleport
- add a method to reset your player's position
- add properties to store your player's hp, strength, defense, magic, etc.

-----------------------------------------------


The ``PlayerBullet`` Class
==================================

We will fire bullets from the player whenever the mouse is clicked.


Implement your ``PlayerBullet`` class.

- Set ``self.scale``, ``self.color``, ``self.position``
- Add a new property for bullet speed e.g. ``self.speed``
- Set rotation with ``self.point_toward_mouse_cursor()``
- Bullets move foward, i.e. ``self.move_forward(self.speed)``
- ``self.delete()`` if ``self.is_touching_window_edge()``


Add the following method to your Player class.

.. code:: python

    def on_left_click_anywhere(self):
        window.create_sprite(PlayerBullet)


Extensions:

- Give your player a maximum number of bullets they can fire
- Add a power property to your ``Bullet`` class
- Add a ``PowerUp`` class that the player can collect to increase power


---------------------------------------------------

The ``Enemy`` Class
==========================

In the ``Enemy`` class:

- Enemys start at a random position i.e. ``self.goto_random_position()``
- Enemys start with a random rotation, i.e. ``self.rotation = randint(0, 360)``
- Add a speed property and move each enemy forward
- Delete an an enemy when they touch the window's edge

You will need the ``Scheduler`` class and the ``randint`` function.

.. code:: python

    from pycat.core import Scheduler
    from random import randint

Spawn the enemies using the ``Scheduler.update()`` method.

.. code:: python

    def spawn_enemy():
        window.create_sprite(Enemy)


    Scheduler.update(spawn_enemy, delay=1)


Extensions:

- Spawn enemies only if they are farther than some distance from the player.
  You can use the method ``self.distance_to(player.position)``
- Spawn enemies on the window edge.
  How can you keep them from being immediately deleted?

------------------------------------------------------------

``PlayerBullet`` - ``Enemy`` Interaction
=============================================

- ``self.add_tag('pbullet')`` to our ``PlayerBullet`` class
- delete enemies if ``self.is_touching_any_sprite_with_tag('pbullet')``

Extensions:

- add hp to your ``Enemy`` class so that they die after multiple hits
- When an enemy is hit you could also

    - change color, and/or opacity
    - create a particle effect animation

-----------------------------------------------------

The ``EnemyBullet`` Class
==================================

Create an ``EnemyBullet`` class with properties:

- ``self.color``
- ``self.scale``
- ``self.speed``

The enemy bullets should be deleted if:

- ``self.is_touching_window_edge()``
- ``self.is_touching_sprite(player)``

We want each of our enemies to fire bullets at the player every 2 seconds.

- add a ``self.time`` to the ``Enemy`` class
- update ``self.time`` in ``on_update(self, dt)``
- if ``self.time > 2`` then create a bullet and set it's position/rotation

--------------------------

``EnemyBullet`` - ``Player`` Interaction
=============================================

- ``self.add_tag('ebullet')`` to our ``EnemyBullet`` class
- delete player if ``self.is_touching_any_sprite_with_tag('ebullet')``

Extensions:

- add hp to your ``Player`` class so that they die after multiple hits
- When a player is hit you could also:

    - change color, and/or opacity
    - create a particle effect animation
