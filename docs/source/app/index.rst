================
拡張機能を試す
================

ブロック図
-----------

.. blockdiag::

    blockdiag {
        A -> B -> C;
        A -> E -> F;
    }

.. seqdiag::

    seqdiag {
        browser  -> webserver [label = "GET /index.html"];
        browser <-- webserver;
        browser  -> webserver [label = "POST /blog/comment"];
                    webserver  -> database [label = "INSERT comment"];
                    webserver <-- database;
        browser <-- webserver;
    }


インライン表示::

 $ pip install sphinx

If you want to install it from source, grab the git repository and run setup.py::

 $ git clone git://github.com/django-extensions/django-extensions.git
 $ cd django-extensions
 $ python setup.py install

ｺｰﾄﾞ表示::
.. code-block:: python
 def add(a, b):
    return none
