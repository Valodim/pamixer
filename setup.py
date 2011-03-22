#!/usr/bin/env python

from setuptools import setup

setup(name='pamixer',
      version='0.1.3',
      description='PulseAudio Curses Mixer Application',
      author='Valodim',
      author_email='valodim@mugenguild.com',
      url='http://github.com/valodim/pamixer',
      packages=['pamixer', 'pamixer.classes', 'pamixer.screens'],
      scripts=['bin/pamixer'],
      requires=['libpulseaudio(>=0.9.22)','argparse'],
      install_requires=['libpulseaudio >=0.9.22.1','argparse']
     )
