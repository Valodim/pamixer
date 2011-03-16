#!/usr/bin/env python

from setuptools import setup

setup(name='pamixer',
      version='0.1.1',
      description='PulseAudio Curses Mixer Application',
      author='Valodim',
      author_email='valodim@mugenguild.com',
      url='http://github.com/valodim/pamixer',
      download_url='http://datatomb.de/~valodim/pamixer-0.1.1.tar.gz',
      packages=['pamixer', 'pamixer.classes', 'pamixer.screens'],
      scripts=['bin/pamixer'],
      install_requires=['libpulseaudio >=0.9.22','argparse']
     )
