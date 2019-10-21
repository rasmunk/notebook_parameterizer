import os
from setuptools import setup

here = os.path.dirname(__file__)


def read(path):
    with open(path, 'r') as _file:
        return _file.read()


def read_req(name):
    path = os.path.join(here, name)
    return [req.strip() for req in read(path).splitlines() if req.strip()]


setup(
    name='notebook_parameterizer',
    version='0.0.1',
    description='',
    author='Rasmus Munk',
    author_email='rasmus.munk@nbi.ku.dk',
    license='MIT',
    keywords='jupyter notebook parameters',
    long_description='',
    url='https://github.com/rasmunk/notebook_parameterizer',
    packages=['notebook_parameterizer'],
    install_requires=read_req('requirements.txt'),
    extras_requires={
        "test": read_req('requirements-dev.txt'),
        "dev": read_req('requirements-dev.txt')
    },
    entry_points={
        'console_scripts': ['notebook_parameterizer = '
                            'notebook_parameterizer.cli:notebook_parameterizer'
                            ]},
    project_urls={
        'Source': 'https://github.com/rasmunk/notebook_parameterizer'
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
