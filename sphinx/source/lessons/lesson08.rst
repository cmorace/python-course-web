Lesson 8
################

Download and extract the image files below.
   
:download:`media.zip <../_lesson_resources/lesson_08/L8_media.zip>`


Drawing rects around sprites

.. code-block:: Python

    w = Window(draw_sprite_rects=True)

.. code-block:: Python

    from random import shuffle

    w = Window(draw_sprite_rects=True)

    img_list = 4*['1.png', '2.png', '3.png', '4.png']
    shuffle(img_list)

    for i in range(4):
        for j in range(4):
            s = w.create_sprite(Card, x=100 + j*100, y=500 - i*100)
            s.image = img_list.pop()
