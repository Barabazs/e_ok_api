e_ok_api
========

[![PyPI version shields.io](https://img.shields.io/pypi/v/e_ok_api.svg)](https://pypi.python.org/pypi/e_ok_api/)
[![Travis - CI ](https://img.shields.io/travis/dotEsuS/e_ok_api.svg)](https://travis-ci.org/dotEsuS/e_ok_api)

Unofficial API wrapper for Liantis [e-OK](https://www.e-ok.be/).

Important
=====

This API wrapper is now obsolete since Liantis updated their API.
I've rewritten the wrapper and will probably update the new one more frequently.
Please use [python-liantis-ess-api](https://github.com/dotEsuS/python-liantis-ess-api).

Usage
=====

```bash
pip install e-ok-api
```	
	
Examples
--------
```python
y = TimeEOK()
y.login('Username', 'Password')
my_user_id = y.get_userid()
print(y.get_remaining_workhours(my_user_id))
```
