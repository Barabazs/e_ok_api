========
e_ok_api
========


.. image:: https://img.shields.io/pypi/v/e_ok_api.svg
        :target: https://pypi.python.org/pypi/e_ok_api

.. _e-OK: http://www.e-ok.be/

Unofficial API wrapper for Liantis e-OK_.

Usage
=====

.. code-block:: bash

	$ pip install e-ok-api
	
	
Examples
--------
.. code-block:: python

	y = TimeEOK()
	y.login('Username', 'Password')
	my_user_id = y.get_userid()
	print(y.get_remaining_workhours(my_user_id))
