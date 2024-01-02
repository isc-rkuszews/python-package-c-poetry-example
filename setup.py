# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bobtest', 'bobtest.math']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bobtest',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Bob Kuszewski',
    'author_email': 'rkuszews@intersystems.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
