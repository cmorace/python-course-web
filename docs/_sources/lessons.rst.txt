*******
Lessons
*******

Lesson 1
########

Resources
*********

Download and extract the image files below.
   
:download:`lesson_01_images.zip <_lesson_resources/lesson_01_images.zip>`

   
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
Properties, also known as member variables, are variables contained inside a particular class like Sprite or Window.

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


Lesson 2
########

Types
********

- ``int`` a whole number

- ``str`` a list of characters

- ``float`` a floating-point (decimal) number

- ``bool`` a boolean value ``True`` or ``False``

- ``Window`` the application window that draws graphics
  
- ``Sprite`` a rectangular image we can manipulate in the window

- ``Color`` the red, green, and blue values that describe a color

Use the ``type()`` function to see an object's type.

Remember: 

- function arguments have specific types.

- properties (member variables) of a class have specific types.

- function return values have a specific type.

Questions:

What is the function ``input()`` 's return value type?
What is the type of the ``x`` and ``y`` properties of a Sprite?


Type Conversion
****************

Implicit Conversion

.. code-block:: python

   x = 3
   y = .14
   z = x + y
   print(z)

Explicit Conversion

.. code-block:: python

   x = '3'
   y = .14
   z = float(x) + y
   print(z)


.. code-block:: python

   x = '3'
   y = .14
   z = x + str(y)
   print(z)

Classes
*******

We can create custom types by defining a **class**. A class defines properties and methods or modifies the properties and methods of an existing class through inheritance.

For example, we can create a class that inherits from the ``Sprite`` class that includes all the properties and methods of a Sprite, plus any additional properties of methods we define. We can also set the specific properties so that all class instances share the same data.

.. code-block:: python

   class Elephant(Sprite):

      def on_create(self):
         self.image = 'elephant.png'

A class is similar to a blueprint or a plan. Just like a house is built from a blueprint, an object is created from a class definition. In pycat, we use the window object to create a new object of type Elephant.

.. code-block:: python

   elephant = window.create_sprite(Elephant)

Loops
******

.. code-block:: python

   for i in range(10)
      print(i)

   




