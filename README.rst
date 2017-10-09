piximg
======

A sphinx extension to insert images from pixiv.net to doc

Installation
------------

::

    pip install git+https://github.com/TitanSnow/piximg.git
    
Usage
-----

In sphinx doc source file where you wanna insert a image::

    .. piximg:: <embedId>
       :size: small|medium|large    (optional)
       :border: on|off              (optional)

You can get *embedId* from *シェア* section near the artwork
or the *illust_id* query field in the URL of the page of the artwork.
For example, a URL like this::

    https://www.pixiv.net/member_illust.php?mode=medium&illust_id=62034471
    
Then the *embedId* is just ``62034471``

To enable this extension, add it to ``conf.py`` of your sphinx project:

.. code-block:: python

    # conf.py
    extensions = ['piximg']

Done.

Demo_
-----

.. _Demo: https://titansnow.github.io/piximg
