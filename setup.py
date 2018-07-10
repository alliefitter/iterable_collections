import sys
from setuptools import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='iterable_collections',
    version='0.1.6',
    packages=['iterable_collections'],
    license='MIT License',
    author='Allie Fitter',
    author_email='fitterj@gmail.com',
    description='A collections pipeline tool for iterable objects with support for iteration with `dict.items`',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords=['collection', 'map', 'filter', 'pipeline', 'linq', 'scala'],
    url='https://github.com/alliefitter/iterable_collections',
    data_files=[(
        'lib/python{}.{}/site-packages/iterable_collections'.format(*sys.version_info[:2]),
        [
            "iterable_collections/collection.pyi",
            "iterable_collections/strategy.pyi",
            "iterable_collections/factory.pyi",
            "iterable_collections/utils.pyi"
        ]
    )],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    )
)
