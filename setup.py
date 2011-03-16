#!/usr/bin/env python

from distutils.core import setup

setup(name='pamixer',
      version='0.1',
      description='PulseAudio Curses Mixer Application',
      author='Valodim',
      author_email='valodim@mugenguild.com',
      url='http://github.com/valodim/pamixer',
      download_url='http://datatomb.de/~valodim/pamixer-0.1.tar.gz',
      packages=['pamixer', 'pamixer.classes', 'pamixer.screens'],
      scripts=['bin/pamixer'],
      requires=['libpulseaudio(>=0.9.22)']
     )
