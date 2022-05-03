************************************************
Lesson 11
************************************************

Lists
======================
Lists in Python (also known as arrays in other programming languages)
are very powerful **data structure**.

- stores a **collection** of objects or values
- the objects stored in a list are called **elements**
- the elements are **ordered** (i.e., there is a first, second, etc. element)
- the elements in a list should usually have the same **type**

Initialization
------------------------

.. code-block:: Python

    a = []
    b = list()
    student_names = ['Justyna', 'Yong', 'Tim', 'Lucas', 'Capri']
    daily_covid_cases = [14, 90, 200, 598, 1184]
    temperatures = [100.5, 68.1, 87.0, 66.2]
    animation_states = [WAIT, WARN, ATTACK, DIE]
    colors = [Color.RED, Color.GREEN, Color.BLUE]
    images = ['apple.jpg', 'ninja.png', 'sword.tga', 'background.bmp']

Accessing Elements by Index
------------------------------
Each element in the list has an **index**, an integer value
corresponding to the element's position in the list.

.. code-block:: Python

    student_names = ['Justyna', 'Yong', 'Tim', 'Lucas', 'Capri']
    print(student_names)
    print(student_names[0])
    # print(student_names[1])
    # print(student_names[2])
    # print(student_names[3])
    # print(student_names[4])
    # print(student_names[5])


Part 1: Basic Slideshow
=========================

.. admonition:: Exercise 1

    Download and extract the zip file below for some sample images.

    :download:`L11_media.zip <../_lesson_resources/lesson_11/L11_media.zip>`

    1. Create a list of three file names. For example,

       .. code-block:: python

           images = ['1.jpg',
                     '2.jpg',
                     '3.jpg',
                    ]

    2. Set the ``window.background_image = images[0]``

    3. Create three buttons (``Sprites``) that change the background image when clicked.

    Extension:
        If you finish the basic slideshow early, try this for a challenge.
        Make a copy of your python file and create a list of captions.
        Change to the different captions when you change the images.


-------------------


Part 2: Slideshow with Next Button
=======================================

What if we want more than three images in the list?

Let's implement a "next button" that switches to the next image in the list.
But we need our program to "remember" the **index** of the current image.

How can we "remember" the current index?

.. admonition:: Exercise 2

    1. Add more images to your list. For example,

       .. code-block:: python

           images = ['1.jpg',
                     '2.jpg',
                     '3.jpg',
                     '4.jpg',
                     '5.jpg',
                     '6.jpg',
                    ]

    2. Add a ``NextButton(Sprite)`` class that remembers the index of the current image and
       changes to the next photo in the list each time it is clicked.


    Extension:

       - Fix the index out of bounds error.
       - Modify your program to go back to the first image after the last

-------------------


Part 3: Infinite Slideshow
===============================

If we are showing the last image in the list,
what happens when we hit the next button?

Can you come up with a solution to fix the ``IndexError`` problem?

What if we don't know the number of elements in the list?

The ``len()`` Function
------------------------

The ``len()`` function returns the number of elements in a list. For example,

.. code-block:: Python

    images = ['1.jpg',
              '2.jpg',
              '3.jpg',
              '4.jpg',
              '5.jpg',
              '6.jpg',
             ]
    print(len(images)) # will print 6

Using the ``len()`` function is much better than using an integer literal,
because if we add or remove elements from our list, our program will still work.

.. admonition:: Exercise 3

    Use the ``len()`` function to fix the ``IndexError`` index out of range problem.

    Extension: Use the mod operator ``%`` instead of an if statement.

-------------------


Part 4: Slideshow with Previous and Next Button
================================================

What if we want to add a previous button?



Scope: Global vs. Local Variables and the ``global`` Keyword
---------------------------------------------------------------

Since the ``current_index`` variable must be modified in
two different classes (previous button and next button),
we must define it in the **global** scope. That is,
outside of two classes where we access and modify it.
If we need to set a global variable using ``=``, ``+=``, ``%=``, etc.
within a class or function, we must use the ``global`` keyword.
For example,

.. code-block:: python

    current_index = 0

    class NextButton(Sprite):
        def on_left_click():
            global current_index
            current_index += 1

If we don't use the ``global`` keyword in the example above,
we will get an error. Other times we may not get an error but
get unexpected results.

.. warning::

    It is considered good practice to limit the *scope* of variables
    as much as possible. Global variables are generally a bad idea.
    Why? Because global variables make programs more difficult to debug.
    Before using a global variable, you should ask yourself if there
    is another way to solve your problem.

.. admonition:: Exercise 4

    Add a ``PreviousButton`` class that changes the background image to
    the previous index when clicked.

    Extensions:

    - Could you use a single class for the Previous and Next Buttons? How?
    - Add any extensions from the previous exercises
    - Add "like" and "dislike" buttons and add elements
      to the two new lists or tracks the number of liked and disliked images.
    - Add a button that changes the background to a random image.
