* ``swagger.yaml``: REST API Swagger definition
* ``app.py``: basic rest endpoints
* ``requirements.txt``: list of required Python libraries
* ``Dockerfile``: to build the example as a runnable Docker image
* ``test.sh``: shell script to execute example HTTP requests against the pet shop API


Running Locally
===============

You can run the Python application directly on your local operating system:

.. code-block:: bash

    $ sudo pip3 install -r requirements.txt
    $ ./app.py # start the HTTP server


Using OAuth2 Security
=====================

To enable OAuth2 security (token verification), you need to set the environment variable TOKENINFO_URL

.. code-block:: bash

    $ docker run -d -p 8080:8080 -e connexion-example

Using Connexion with a WSGI container
=====================================

You can use the Flask WSGI app with any WSGI container, e.g. `using Flask with uWSGI`_:

.. code-block:: bash

    $ sudo pip3 install uwsgi
    $ uwsgi --http :8080 -w app

You can run uwsgi with a large number of worker processes to get high concurrency.
This obviously makes no sense for the in-memory pet store example (every worker would have its own pet store dictionary):

.. code-block:: bash

    $ uwsgi --http :8080 -w app -p 16  # use 16 worker processes

See the `uWSGI documentation`_ for more information.

.. _Connexion: https://pypi.python.org/pypi/connexion
.. _Flask: http://flask.pocoo.org/
.. _Swagger 2.0 Specification: https://github.com/swagger-api/swagger-spec/blob/master/versions/2.0.md
.. _/ui/: http://localhost:8080/ui/
.. _using Flask with uWSGI: http://flask.pocoo.org/docs/latest/deploying/uwsgi/
.. _uWSGI documentation: https://uwsgi-docs.readthedocs.org/
