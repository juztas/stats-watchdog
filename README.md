# OpenFlow Next Generation - watchdog

This is a component of of-ng project. This component is responsible for collect
statistics about the flows installed on switches and generate `rrd` files for future plotting.

Currently this only supports OpenDaylight, but the idea is that this component
should be controller independent.

This project uses the `python-odl` library to communicate with OpenDaylight.

### Downloading the source code

```
$ sudo mkdir -p /usr/local/src/of-ng/
$ sudo git clone https://github.com/of-ng/stats-watchdog.git
$ cd /usr/local/src/of-ng/stats-watchdog/
```

### Edit your config file

Edit the file `stats-watchdog/settings/default.py` and configure the variables
properly.

## Installing

This is just a daemon that runs in background to collect the stats. To install
run the following command:

```
$ sudo python2.7 setup.py install
```

## Running

To start your daemon, just run:

```
$ cd /usr/local/src/of-ng/stats-watchdog/
$ sudo su
# export PYTHONPATH=.:$PYTHONPATH
# ofng-watchdog start 
```

Please, check if the `rrd` files are been generated at
`/usr/local/share/rrd/ofng`.

## Authors

This is a collaborative project between SPRACE (From São Paulo State University
\- Unesp) and Caltech (California Institute of Technology).

For a complete list of people, please see the AUTHORS.md file.
