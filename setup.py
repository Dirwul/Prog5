from setuptools import setup, find_packages

setup(
    name='dirwulpackage',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        '__init__', 'calculator', 'calculator_template'
    ],
)
