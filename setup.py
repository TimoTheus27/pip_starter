## example for pip project creations:
## https://github.com/shuds13/pyexample

from setuptools import setup

setup(
    name='pyexample',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/shuds13/pyexample',
    author='Timo Gerth',
    author_email='timogerth@gmail.com',
    packages=['src'],
    install_requires=[
        'setuptools',
        'sqlite3',                     
        'numpy',                            
    ],

    classifiers=[
        'Development Status :: 1 - Planning',       
        'Programming Language :: Python :: 3.8.9',
    ],
)