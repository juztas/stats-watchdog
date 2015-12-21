# -*- coding: utf-8 -*-
try:
    from setuptools import setup
    extra = dict(test_suite="tests.test.suite")
except ImportError:
    from distutils.core import setup
    extra = {}

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]

setup(
    name='ofng-watchdog',
    version='0.0.1',
    author='Beraldo Leal',
    author_email='beraldo@ncc.unesp.br',
    packages=[],
    url='http://github.com/of-ng/stats-watchdog/',
    data_files=[('/usr/local/share/rrd/ofng', '')],
    license='LICENSE.md',
    description='Python Daemon to collect OpenFlow Flow stats and save in RRD format.',
    install_requires=install_requires,
    scripts=['scripts/ofng-watchdog'],
    keywords = ['odl', 'opendayligh', 'sdn', 'openflow', 'python', 'stats', 'statistics', 'flow'],
    platforms = "Posix; MacOS X;",
    classifiers = ["Development Status :: 2 - Pre-Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Operating System :: POSIX",
                   "Topic :: Internet",
                   "Topic :: System :: Networking",
                   "Programming Language :: Python :: 2.7"],
    **extra
)
