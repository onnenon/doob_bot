import os
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()
REQUIREMENTS = []
DEPENDENCY_LINKS = []

os.chdir(os.path.normpath(BASEDIR))

with open(os.path.join(BASEDIR, 'requirements.txt')) as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if ("http://" in line or "https://" in line or "ssh://" in line) and "#egg=" in line:
            parts = line.split("#egg=")
            REQUIREMENTS.append(parts[-1])
            DEPENDENCY_LINKS.append(line)
        elif len(line) and line[0] != "#" and line[0] != "-":
            REQUIREMENTS.append(line)

setup(
    name='doob_bot',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    description='A Simple Discord bot for Raider.io',
    long_description='A simple Discord bot for Raider.io',
    url='https://github.com/onnenon/doob_bot',
    author='Stephen Onnen',
    author_email='stephen.onnen@gmail.com',
    install_requires=REQUIREMENTS,
    dependency_links=DEPENDENCY_LINKS)
