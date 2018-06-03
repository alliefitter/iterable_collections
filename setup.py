import sys
from setuptools import setup

setup(
    name='iterable_collections',
    version='0.1.3',
    packages=['iterable_collections'],
    url='',
    license='MIT License',
    author='Allie Fitter',
    author_email='fitterj@gmail.com',
    description='A collections pipeline tool for iterable objects with support for iteration with `dict.items`',
    keywords=['collection', 'map', 'filter', 'pipeline', 'linq', 'scala'],
    data_files=[(
        'lib/python{}.{}/site-packages/iterable_collections'.format(*sys.version_info[:2]),
        [
            "iterable_collections/collection.pyi",
            "iterable_collections/strategy.pyi",
            "iterable_collections/factory.pyi",
            "iterable_collections/utils.pyi"
        ]
    )]
)
