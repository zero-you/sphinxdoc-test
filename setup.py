#!/usr/bin/env python

from distutils.core import setup
from os import path
import re, os
import subprocess

VERSIONFILE = 'mymodule/_version.py'
verstrline = open(VERSIONFILE, 'rt').read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
cmd = 'git rev-parse --verify --short HEAD'
git_hash = subprocess.check_output(cmd, shell=True, encoding='utf-8')
# tag git
gitverstr = 'v' + verstr
tags =  subprocess.check_output('git tag', shell=True, encoding='utf-8')
#if gitverstr not in tags:
#    cmd = 'git tag -a %s %s -m "tagged by setup.py to %s"' % (gitverstr, git_hash, verstr)
#    subprocess.check_output(cmd, shell=True)
# use the git hash in the setup
verstr += ', git hash: %s' % git_hash

setup(name='mymodule',
      version=verstr,
      description='A test module',
      author='zero-you',
      author_email='you.ling.vu@gmail.com',
      license="Apache License 2.0",
      #url='https://zero-you.github.io/sphinxdoc-test',
      url='https://github.com/zero-you/sphinxdoc-test',
      packages=['mymodule'],
      test_suite='test',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
          ]
     )
