Lesson 14
==================


What's new?
   - new mouse event handler for the Sprite class: ``on_left_click_anywhere(self)``
   - ``self.point_toward_mouse_cursor()`` will set a sprite's rotation/direction

Final project template and decomposition

1. Implementing the Player class

    .. code:: python

        from pycat.core import Color, KeyCode, Sprite, Window

        window = Window()


        class Player(Sprite):

            def on_create(self):
                self.color = Color.AMBER
                self.scale = 30
                self.speed = 10

            def on_update(self, dt):
                if window.is_key_pressed(KeyCode.W):
                    self.y += self.speed
                # fill in code for keys A, S, D


        player = window.create_sprite(Player)
        window.run()

    Extensions:

    - set your player's initial position
    - add a key to make your player teleport
    - add a method to reset your player's position
    - add properties to store your player's hp, strength, defense, magic, etc.


2. Shooting Bullets with ``on_left_click_anywhere()``
   
   We will fire bullets whenever the mouse is clicked.
   Add the following method to your Player class.
   
   .. code:: python

        def on_left_click_anywhere(self):            
            window.create_sprite(Bullet)

   Now implement your ``Bullet`` class.

   - What is the bullet size i.e. ``self.scale``?
   - What is the bullet color i.e. ``self.color``?
   - What is the bullet starting position i.e ``self.position``?
   - Add a new property for bullet speed i.e. ``self.speed``
   - To set the rotation to shoot towards the mouse cursor, use ``self.point_toward_mouse_cursor()``.
   - Make each bullet move foward to the mouse cursor with ``self.move_forward(self.speed)`` and call ``self.delete()`` if ``self.touching_window_edge()``

   Extensions:

   - Give your player a maximum number of bullets they can fire
   - Add a power property to your ``Bullet`` class
   - Add a ``PowerUp`` class that the player can collect to increase power

3. Add an ``Enemy`` class and generate some enemies.

   We will need a little help. Import the ``Scheduler`` class and the ``random`` module.

   .. code:: python
      
        from pycat.core import Color, KeyCode, Scheduler, Sprite, Window
        import random

   In the ``Enemy`` class:
   
   - Start each enemy at a random starting position i.e. ``self.goto_random_position()``
   - Start each enemy with a random rotation, i.e. ``self.rotation = random.randint(0, 360)``
   - Add a speed property and move each enemy forward
   - Delete an an enemy when they touch the window's edge

   Spawn the enemies using the ``Scheduler.update()`` method.

   .. code:: python

      def spawn_enemy():
          window.create_sprite(Enemy)


      Scheduler.update(spawn_enemy, delay=1)

   Remember that this code must be outside any class (in the global scope).


   Extension:

   - only spawn enemies if they are farther than some distance from the player. You can use the method ``self.distance_to(player.position)``
   - only spawn enemies on the window edge. How can you keep them from being immediately deleted?

4. Have the player's bullets kill enemies

   - ``self.add_tag('bullet')`` in our ``Bullet`` class
   - ``self.delete()`` if ``self.touching_any_sprite_with_tag('bullet')`` in our ``Enemy`` class.

   Extensions: 
   
   - add hp to your ``Enemy`` class so that they die after multiple hits
   - if an enemny touches the player, reduce their hp, change color, and/or opacity

5. Make your enemies shoot bullets at the player

    Create an ``EnemyBullet`` class with properties:

       - ``self.color``
       - ``self.scale``
       - ``self.speed``

    The enemy bullets should ``self.move_forward(self.speed)`` and be deleted if:
    
       - ``self.touching_window_edge()`` or,
       - ``self.touching_sprite(player)``

    We want each of our enemies to fire bullets at the player every 2 seconds.
    
       - add a ``self.time`` to the ``Enemy`` class
       - update ``self.time`` in ``on_update(self, dt)``
       - if ``self.time > 2`` then create a bullet and set it's position and rotation
