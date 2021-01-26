from setuptools import setup

setup (
    name='hello',
    version='0.1',
    py_modules=['HelloWorld'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=HelloWorld:hello
    ''',
)