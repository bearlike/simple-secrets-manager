Simple Secret Manager's documentation
=======================================

Secure storage, and delivery for tokens, passwords, API keys, and other secrets using HTTP API, Swagger UI or Python Package. I wanted a Secrets Manager intended for small scale setups that could also scale well. 

Available secret engines
---------------------------

.. list-table:: 
   :widths: 25 75
   :header-rows: 1

   * - Secret
     - Engine Description
   * - `kv`
     - Key-Value engine is used to store arbitrary secrets.


Available authentication methods
---------------------------------

.. list-table:: 
   :widths: 25 75
   :header-rows: 1

   * - Auth Methods
     - Description
   * - `userpass`
     - Allows users to authenticate using a username and password combination.
   * - `token`
     - Allows users to authenticate using a token. Token generation requires users to be authenticated via 

Contents
--------

.. toctree::

   usage
   api
