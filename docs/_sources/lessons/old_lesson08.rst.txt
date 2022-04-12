Lesson 8
################

Download and extract the image files below.
   
:download:`media.zip <../_lesson_resources/lesson_08/L8_media.zip>`


Drawing Sprite Rects
-----------------------

.. code-block:: Python

    w = Window(draw_sprite_rects=True)



Card Randomization and Grid Layout
------------------------------------

.. code-block:: Python

    from random import shuffle

    w = Window(draw_sprite_rects=True)

    img_list = 4*['1.png', '2.png', '3.png', '4.png']
    shuffle(img_list)

    for i in range(4):
        for j in range(4):
            s = w.create_sprite(Card, x=100 + j*100, y=500 - i*100)
            s.image = img_list.pop()


Add Clicked Cards to List
-----------------------------

When should clicked cards be added to the list

- when the card is clicked

.. code-block:: python

    if len(clicked_cards) < 2 and self not in clicked_cards:
        clicked_cards.append(self)



