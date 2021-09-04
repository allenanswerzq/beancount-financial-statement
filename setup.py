"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='beancount-financial-statement',

    version='0.8.1',

    description='A report generator for beancount financial statement.',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/e7h4n/beancount-financial-statement',

    author='e7h4n',

    author_email='ethan.pw@icloud.com',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial :: Accounting'

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='beancount, financial statement',

    package_dir={'beancount-financial-statement': 'src'},

    packages=['.'],

    python_requires='>=3.6, <4',

    package_data = {
        'templates': ['src/templates/*'],
    },

    install_requires=[
        'logzero==1.7.0',
        'click==8.0.1',
        'pystache==0.5.4',
        'beancount==2.3.4',
    ],

    extras_require={
        'dev': [],
        'test': [
            'coverage',
            'pycodestyle',
            'pyflakes',
            'pylint',
            'flake8',
            'python-coveralls',
            'beautifulsoup4'
        ],
    },

    entry_points={
        'console_scripts': [
            'bean-statement=main:main',
        ],
    },

    project_urls={
        'Bug Reports': 'https://github.com/e7h4n/beancount-financial-statement/issues',
        'Source': 'https://github.com/e7h4n/beancount-financial-statement/',
    },
)
