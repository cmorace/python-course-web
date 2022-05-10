******************************************
Lesson 12
******************************************

Review Lists, Loops, and Functions
============================================

List Initialization
----------------------

.. code-block:: python

    a = [0, 0, 0]
    b = 3 * [0]
    c = []
    c.append(0)
    c.append(0)
    c.append(0)
    print(a)
    print(b)
    print(c)

Accessing List Elements by Index
----------------------------------

.. code-block:: python

    a = [2, 0, 3]
    print(a[0])
    print(a[3])


The ``len()`` Function
------------------------
.. code-block:: python

    a = [2, 0, 3]
    a.append(10000)
    print(len(a))


For Loops with ``range()``
----------------------------------
.. code-block:: python

    for counter in range(5):
        print(counter)

    for counter in range(1, 5):
        print(counter)

    for counter in range(1, 5, 2):
        print(counter)




Functions
----------------------------------

.. code-block:: python

    def foo():
        print("printint inside the foo function")


    def say_hello(name: str):
        print("hello", name)

Exercise 1
---------------


.. admonition:: Exercise 1

    Define a function named ``print_numbers`` that prints the numbers 0-10.

    Extensions:

        1. Write a function ``print_numbers_up_to(n: int)`` that prints the numbers 0-n.
        2. Write a function ``print_numbers_between(a: int, b: int)`` that prints the numbers a-b.
        3. 2. Write a function ``print_even_numbers_between(a: int, b: int)`` that prints the even numbers between a and b

-----------------------------

Iterating Over a List
=========================

.. code-block:: python

    index = 0
    names = ['Charles', 'Capri', 'Lucas', 'Tim', 'Yong', 'Justyna']
    print(names[index])


    for index in range(3):
        print(index)

How can we print out all of the names in the ``names`` list?


Exercise 2
---------------


.. admonition:: Exercise 2

    Define a function named ``print_list(any_list: List[Any])`` that takes a list as an argument and prints out all of the lists elements.

    Extensions:

        1. Write a function to print the first half of a list.
        2. Write a function to print the second half of a list.
        3. Write a function to print put rounded numbers from a list of floats.
        4. Write a function to print a list in reverse order.
        5. Write a function to print the square of each number in a list.

--------------------


Conditions in For Loops
===========================

Exercise 3
---------------


.. admonition:: Exercise 3

    Define a function named ``print_element_in_list(any_list: List[Any], element)`` that takes a list as an argument and prints out the element if it is in the list.

    Extensions:

        1. Write a function to print the indices of an element if it is in a list.
        2. Write a function to print the elements between two numbers ``a`` and ``b``.
        3. Write a function to print put all the even numbers in a list.
        4. Write a function to print out all of the prime numbers in a list.


--------------------


Return Values from Functions
===============================

.. code-block:: python

    name = input('What is your name')

    def give_me_5() -> int
        return 5

    hand = give_me_5()
    print(hand)

    def roll_die() -> int:
        return random.randint(1,6)

    random_side = roll_die()

    def is_adult(age: int) -> bool:
        return age >= 18


Exercise 4
---------------


.. admonition:: Exercise 4

    Define a function named ``roll_die(sides: int) -> int`` that returns a random int between 1 and ``sides``.

    Extensions:

        1. Write a function to returns the first element in a list
        2. Write a function to returns the last element in a list
        3. Write a function that returns the number of elements in a list with the value equal to ``v`` where ``v`` is an argument.
        4. Write a function that returns True if a string starts with the letter 't'
        5. Write a function that returns True if a string starts with the letter ``c`` where ``c`` is and argument.
        6. Write a function that returns a list of length ``n`` with random elements between 1 and 100.
        7. Write a function that returns a list of length ``n`` with random elements between ``a`` and ``b`` where ``a`` and ``b`` are arguments.


Using ``return`` to Stop Execution
-----------------------------------

Exercise 5
---------------

.. admonition:: Exercise 5

    Define a function named ``is_in_list(lst: List[int], element: int) -> bool`` that returns a True if and only if ``element`` is found in ``lst``.

    Extensions:

        1. Write a function that returns True if an element is not in a list.
        2. Write a function that returns True if two lists have at least one element in common.



Python's ``in`` Keyword
-----------------------------

