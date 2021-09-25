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
