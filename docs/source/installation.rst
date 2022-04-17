Installation
============

.. _installation:


Automated Install: `docker-compose <https://docs.docker.com/compose/install/>`__ (Recommended)
------------------------------------------------------------------------------------------------

1. Edit and Run the `stack <https://github.com/bearlike/simple-secrets-manager/blob/main/docker-compose.yml>`__ by executing
   ``docker-compose up -d``.

Manual Install
---------------

1. Clone our repository and run

.. code-block:: console

   $ git clone --depth 1 https://github.com/bearlike/simple-secrets-manager simple-secrets-manager
   $ cd "simple-secrets-manager"

2. Start a Mongo database server.
3. Create a ``.env`` file in the project root with environment variables. You can refer Docker environment variables for configurations. 

.. code-block:: console

   # Must atleast have database connection string
   CONNECTION_STRING=mongodb://username:password@mongo.hostname:27017

4. Install the required python packages by executing
   
.. code-block:: console

   $ pip3 install -r requirements.txt

1. You will need atleast ``python3.7``. Start the server by running
   ``server.py``.
2. Visit the application via ``http://server_hostname:5000/api``
   (default port is ``5000``) to visit the Swagger UI.