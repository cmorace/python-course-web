Lesson 1
########

Resources
*********

Download and extract the image files below.
   
:download:`lesson_01_images.zip <../_lesson_resources/lesson_01_images.zip>`

   
Import Statements
*****************

Import statements allow us to import code from outside the file we are currently working on. For example, Window and Sprite are pieces of code that we have already written and would like to re-use.

.. code-block:: python

   from pycat.core import Window, Sprite
   
Variables
*****************
Variables let us store and manipulate data. They store simple data like a number or a string of characters or more complex objects like a Window or a Sprite.
  
.. code-block:: python

   message = 'enter your name'
   number = 100
   window = Window()
   elephant = window.create_sprite()

Properties
*****************
Properties, also known as member variables, are variables contained inside a particular Class like Sprite or Window. For example, below ``image``, ``x``, ``y``, and ``scale`` are properties of the Sprite class.

.. code-block:: python
      
   elephant.image = 'elephant.png'
   elephant.x = 500
   elephant.y = 400
   elephant.scale = 1.5


Functions
*****************

Functions define a sub-routine in our program. They are handy to eliminate duplicate code and make our programs easier to understand and maintain. The data we pass into functions are called **arguments**. The data that we receive from functions are called **return values**. They do not do anything unless they are *called*.

Two functions in the Python programming language are ``input()`` and ``print()``.
      
.. code-block:: python

   age = input('enter your age:')
   print('your age is', age)

Methods
*******
Methods, also known as member functions, are functions contained inside a particular class. Thus, we usually need an instance of the class to call them.

The method ``create_sprite()`` is a member of the ``Window`` class and ``goto_random_position()`` is a method in the the ``Sprite`` class.

.. code-block:: python
   
   elephant = window.create_sprite()
   elephant.goto_random_position()
      
Conditional Statements
***********************

Conditional statements change the flow of our code based on some logic.

.. code-block:: python

   size = input('big or small? )
   if size == 'big':
      elephant.scale = 2
   elif size == 'small':
      elephant.scale = 0.5
   else:
      print('Sorry, I only understand big or small.')

