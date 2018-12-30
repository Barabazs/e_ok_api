e_ok_api
========

[![PyPI version shields.io](https://img.shields.io/pypi/v/e_ok_api.svg)](https://pypi.python.org/pypi/e_ok_api/)
[![Travis - CI ](https://img.shields.io/travis/dotEsuS/e_ok_api.svg)](https://travis-ci.org/dotEsuS/e_ok_api)

Unofficial API wrapper for Liantis [e-OK](https://www.e-ok.be/).

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
