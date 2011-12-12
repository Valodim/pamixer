#!/usr/bin/env python

from setuptools import setup

setup(name='pamixer',
      version='0.1.4',
      description='PulseAudio Curses Mixer Application',
      author='Valodim',
      author_email='valodim@mugenguild.com',
      url='http://github.com/valodim/pamixer',
      packages=['pamixer', 'pamixer.classes', 'pamixer.screens'],
      scripts=['bin/pamixer'],
      requires=['libpulseaudio(>=1.1)','argparse'],
      install_requires=['libpulseaudio >=1.1','argparse']
     )
