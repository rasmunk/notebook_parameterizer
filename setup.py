import os
from setuptools import setup

here = os.path.dirname(__file__)


def read(path):
    with open(path, 'r') as _file:
        return _file.read()


def read_req(name):
    path = os.path.join(here, name)
    return [req.strip() for req in read(path).splitlines() if req.strip()]


version_ns = {}
with open(os.path.join(here, 'version.py')) as f:
    exec(f.read(), {}, version_ns)

long_description = open('README.rst').read()
setup(
    name='notebook_parameterizer',
    version=version_ns['__version__'],
    description='A tool to generate parameterized Jupyter Notebooks',
    author='Rasmus Munk',
    author_email='rasmus.munk@nbi.ku.dk',
    license='MIT',
    keywords='jupyter notebook parameters',
    long_description=long_description,
    url='https://github.com/rasmunk/notebook_parameterizer',
    packages=['notebook_parameterizer'],
    install_requires=read_req('requirements.txt'),
    extras_require={
        "test": read_req('requirements-dev.txt'),
        "dev": read_req('requirements-dev.txt')
    },
    entry_points={
        'console_scripts': ['notebook_parameterizer = '
                            'notebook_parameterizer.cli:notebook_parameterizer'
                            ]},
    project_urls={
        'Source Code': 'https://github.com/rasmunk/notebook_parameterizer'
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ]
)
